
class Myrange:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start +=1
        print(self.start)
        if self.start == self.end:
            raise StopIteration
        return self.start


my_range = Myrange(1, 10)
# my_range = my_range.__iter__()
# my_range.__next__()

# for item in my_range:
#   print(item)

def myrange(start, end):
    while start < end:
        yield  start
        start += 1
        
