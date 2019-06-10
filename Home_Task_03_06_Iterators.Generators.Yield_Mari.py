# Задача 1. Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка.

import json

class Country_iter:
    def __init__(self, path, cursor=-1):
        self.path = path
        self.cursor = -1

    @property
    def country_list(self):
        country_list = []
        with open(self.path, encoding='utf-8') as file:
            countries = json.load(file)
            for country in countries:
                country_list.append(country['name']['common'])
        return country_list

    def __iter__(self):
        return (country for country in self.country_list) # а зачем???

    def __next__(self):
        print(self.country_list)
        self.cursor += 1
        if self.cursor == len(self.country_list):
            raise StopIteration
        return self.cursor

    def write_wiki_link(self):
        with open('wiki_links.txt', 'w', encoding='utf-8') as file:
            for country in countries:
                file.write(f'{country} - https://en.wikipedia.org/wiki/{country.replace(" ", "_")}\n')


countries = Country_iter('countries.json')
countries.write_wiki_link()

for itrm in countries:
    print(itrm)

# Задача 2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.

import hashlib

def md5_generator(path):
    with open(path, 'rb') as file:
        strings = file.readlines()
        for string in strings:
            yield hashlib.md5(string)

# for string in md5_generator('countries.json'):
#     print(string.hexdigest())