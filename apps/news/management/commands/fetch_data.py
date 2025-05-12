# your_app/management/commands/import_third_party_news.py
import requests
import os
from django.conf import settings
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.db import transaction
from datetime import datetime
from apps.news.models import ThirdPartyNews

load_dotenv()


class Command(BaseCommand):
    help = 'Fetches news from API and stores in ThirdPartyNews model'

    def get_news(
            self,
            section: str = 'world',
            limit: int = 20,
            offset: int = 0
    ) -> dict:
        """Fetch news from API with error handling"""
        params = {
            'api-key': os.getenv('API_KEY'),
            'limit': limit,
            'offset': offset
        }

        try:
            response = requests.get(
                os.getenv('API_URL') + section + '.json',
                params=params,
                timeout=10  # Add timeout to prevent hanging
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(
                f"Error getting {section} news: {str(e)}"
            ))
            return None

    def handle(self, *args, **options):
        sections = settings.THIRD_PARTY_NEWS_CONFIG['SECTIONS']
        limit = settings.THIRD_PARTY_NEWS_CONFIG['BATCH_SIZE']
        batches = settings.THIRD_PARTY_NEWS_CONFIG['MAX_BATCHES']
        total_processed = 0

        try:
            with transaction.atomic():
                for batch_num in range(batches):
                    offset = batch_num * limit
                    batch_stats = {}

                    for section in sections:
                        self.stdout.write(
                            f"Fetching {section} news, "
                            "batch {batch_num + 1}..."
                        )

                        data = self.get_news(
                            section=section,
                            limit=limit,
                            offset=offset
                        )

                        if not data or 'results' not in data:
                            continue

                        section_count = 0
                        for article in data['results']:
                            # Skip if required fields are missing
                            if not all([
                                article.get('uri'),
                                article.get('title'),
                                article.get('url')
                            ]):
                                continue

                            # Format published date (handle different possible formats)
                            published_date = None
                            if 'published_date' in article:
                                try:
                                    published_date = datetime.strptime(
                                        article['published_date'],
                                        '%Y-%m-%dT%H:%M:%S%z'
                                    )
                                except ValueError:
                                    try:
                                        published_date = datetime.strptime(
                                            article['published_date'],
                                            '%Y-%m-%d %H:%M:%S'
                                        )
                                    except ValueError:
                                        pass

                            # Get image URL (handle missing multimedia)
                            image_url = ''
                            if article.get('multimedia'):
                                for media in article['multimedia']:
                                    if (media.get('format') == 'thumbLarge'
                                            and media.get('url')):
                                        image_url = media['url']
                                        break

                            ThirdPartyNews.objects.update_or_create(
                                news_url=article['url'],
                                defaults={
                                    'section': section,
                                    'title': article['title'],
                                    'abstract': article.get('abstract', ''),
                                    'image_url': image_url,
                                    'published_date': published_date,
                                }
                            )
                            section_count += 1

                        batch_stats[section] = section_count
                        total_processed += section_count

                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Batch {batch_num + 1} results:\n" +
                            "\n".join([f"{k}: {v} articles"
                                       for k, v in batch_stats.items()])
                        )
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"\nFinished! Total articles processed: {total_processed}"
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error occurred: {str(e)}"))
