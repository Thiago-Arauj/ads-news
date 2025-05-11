import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_news(section: str = 'world', limit: int = 20, offset: int = 0) -> dict:
    # Key for the api
    params = {
        'api-key': os.getenv('API_KEY'),
        'limit': limit,
        'offset': offset
    }

    response = requests.get(
        os.getenv('API_URL')
        + section
        + '.json',
        params=params
    )

    if response.status_code == 200:
        data = response.json()

        return data

    else:
        print(f"Error getting news: {response.status_code}")


def formated_news() -> dict:
    sections = [
        'science',
        'business',
        'world',
        'health'
    ]
    limit = 20
    offset = 0
    batches = 0

    while batches < 5:
        for section in sections:
            batch = get_news(section=section, limit=limit, offset=offset)

            
