from django.utils.translation import get_language
from googletrans import Translator

translator = Translator()


def translate_this(text: str, original_language='en') -> str:
    translated_language = get_language()[:2]
    if original_language == translated_language:
        return text

    try:
        result = translator.translate(
            text,
            src=original_language,
            dest=translated_language
        )
        return result.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text
