f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close()

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c)

with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content)

with open('./resource/review.txt', 'r') as f:
    line = f.readline()

    while line:
        print(line ,end =' ')
        line = f.readline()


with open('./resource/review.txt', 'r') as f:
    content = f.readlines()
    print(content)

score = []
with open('./resource/score.txt', 'r') as f:
    
    for line in f:
        score.append(int(line))
    print(score)
print("평균은 : {:6.3}".format(sum(score)/len(score)))

with open('./resource/text.txt', 'a') as f:
    f.write('Good bye')

from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'cho\n',]