class Reader:
    def __init__(self,file):
        self.file = open(file,'r')
        self.is_done = False

    def read_char(self):
        res = self.file.read()
        self.res = ''
        for i in res:
            if i.isalpha() :
                self.res += i
        self.is_done = True
        return self.res

reader = Reader('day3.txt')

while not reader.is_done:
    print(reader.read_char(), end='')