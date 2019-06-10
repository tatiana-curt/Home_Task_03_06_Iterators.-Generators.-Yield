import json

class Countries_gen:
    def __init__(self, path):
        with open(path) as new:
            self.data = json.load(new)
            # print(self.data)
            self.data = [countri['name']['common'] for countri in self.data]
            self.i = -1
            # print(self.data)
            # print(len(self.data))

    def __iter__(self):
        return self

    def __next__(self):
        # print(self.data)
        self.i += 1
        if self.i < len(self.data):
            with open('links.txt', 'a', encoding='utf-8') as f:
                f.write('{} - https://en.wikipedia.org/wiki/{}\n'.format(self.data[self.i], self.data[self.i].replace(" ", "_")))
                # print('{} - https://en.wikipedia.org/wiki/{}'.format(self.data[self.i], self.data[self.i].replace(" ", "_")))
        else:
            raise StopIteration


# my_iter = Countries_gen('countries.json')
# for item in my_iter:
#     pass
# ____________________________________________________Задание 2__________________________________________________
import hashlib
import shutil

shutil.copyfile(r'links.txt', r'copy_links.txt') #Создаю копию так как 2-ое задание выполняется по умолчанию на файле из первого задания "links.txt"

def generator_md5(path='links.txt'):
    i = 1
    while i != 0:
        with open(path, 'r') as f:
            data = f.readline()
            md5 = hashlib.md5(data.encode('utf-8')).hexdigest()
            yield md5, data
            lines = f.readlines()
            if len(lines) == 0:
                i=0
            else:
               with open(path, "w") as f:
                   for line in lines:
                       f.write(line)
#
my_gener = generator_md5()

for md5_item, data_item in my_gener:
    print(md5_item, data_item)
    with open('md5.txt', 'a', encoding='utf-8') as f:
        f.write('{} - {}\n'.format(md5_item, data_item))



# _____________Вариант Маши_______________________

# def md5_generator(path='links.txt'):
#     with open(path, 'rb') as file:
#         strings = file.readlines()
#         # print(type(strings))
#         for string in strings:
#             yield hashlib.md5(string)
# #
# for string in md5_generator('countries.json'):
#     print(string.hexdigest())
#
# # string = md5_generator('links.txt')
# # print(string.__next__().hexdigest())
# # print(string.__next__().hexdigest())
# # print(string.__next__().hexdigest())