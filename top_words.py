import os
import chardet


PATH_TO_FILES_DIR = 'news_files/'
WORDS_MIN_LENGTH = 7
TOP_NUMBER = 10


def get_filelist():
    filelist = os.listdir(path=PATH_TO_FILES_DIR)
    return filelist


def encode_data():
    with open(PATH_TO_FILES_DIR + file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        encoded_text = data.decode(result['encoding'])
    return encoded_text


def convert_text_to_words_dict():
    encoded_text = encode_data()

    words_list = encoded_text.lower().strip().split(sep=" ")
    words_dict_with_counter = {}
    for word in words_list:
        if len(word) >= WORDS_MIN_LENGTH:
            word_count = encoded_text.count(word) 
            words_dict_with_counter[word] = word_count
    return words_dict_with_counter


def sort_words():
    words_dict_with_counter = convert_text_to_words_dict()

    words_list_sorted = sorted(words_dict_with_counter.items(), key=lambda x: x[1], reverse=True)
    return words_list_sorted


def print_popular_words():
    words_list_sorted = sort_words()

    item = 0
    print('*** ТОР ' + str(TOP_NUMBER) + ' слов' + ' длиннее ' + str(WORDS_MIN_LENGTH - 1) +
          ' символов' + ' для файла ' + file_name + ' ***')
    for popular_word in words_list_sorted:
        if item > (TOP_NUMBER - 1):
            break
        item += 1
        print(popular_word[0] + " — " + str(popular_word[1]))
    print("=" * 20)


for file_name in get_filelist():
    print_popular_words()

