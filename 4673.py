num = set(range(1,10001))
set_num = set()


for i in range(1,10001):
    for j in str(i):
        i += int(j)
    set_num.add(i)

self_num = num - set_num

for k in sorted(self_num):
    print(k)