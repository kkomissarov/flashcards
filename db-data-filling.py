from googletrans import Translator
from models import Word
from db_config import db_session
from pprint import pprint


def get_word_data(word):
    translator = Translator()
    translate = translator.translate(word, src='en', dest='ru')
    other_translations = translate.extra_data.get('all-translations')
    examples = translate.extra_data.get('examples')

    return {
        'word': word,
        'translate': translate.text,
        'other_translations': ', '.join(other_translations[0][1]) if other_translations else None,
        'example': examples[0][0][0] if examples else None
    }


if __name__ == '__main__':
    # with open('words.txt') as words_file:
    #     word_list = words_file.read().splitlines()
    #
    # for word in word_list:
    #     word_data = get_word_data(word)
    #     word = Word(**word_data)
    #     db_session.add(word)
    #     db_session.commit()
    #     print(word, 'OK')


    translator = Translator()
    translate = translator.translate('word', src='en', dest='ru')
    # print(translate)
