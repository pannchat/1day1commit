import random
import time
# 사운드 출력필요모듈
# import winsound
import pygame
import sqlite3
import datetime
#DB 생성 & auto commit
conn = sqlite3.connect('./resource/records.db', isolation_level=None)

#cursor 연결
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS records(\
    id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, reg_date text\
)')
words = [] # 영어 단어 리스트 (1000개 로드)

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

# 파이게임 mixer 초기화
pygame.mixer.init() 
good = pygame.mixer.Sound('./sound/good.wav')
bad = pygame.mixer.Sound('./sound/bad.wav')
with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
# print(words)

input("준비 됐으면 enter 키를 눌러주세요.")

start = time.time()
# print(start)

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print("* 문제 #{}".format(n))
    print(q)
    x = input()
    print()
    

    if str(q).strip() == str(x).strip(): #입력확인 공백제거
        print("정답")
        # 정답 사운드 재생
        
        pygame.mixer.Sound.play(good)
        cor_cnt += 1
    else:
        print("오답")
        # 오답 사운드 재생
        pygame.mixer.Sound.play(bad)
    n += 1
end = time.time()
et = end - start
et = format(et,".3f")

if cor_cnt >= 3:
    print("합격")
else :
    print("불합격")
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'reg_date') VALUES(?,?,?)",\
    (cor_cnt,et,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))\
)
print("게임시간 " , et, "초" , "정답 개수 : {}".format(cor_cnt))

if __name__ == "__main__":
    pass