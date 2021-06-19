# import csv
# with open('./resource/sample2.csv','r', encoding='euc-kr') as f:
#     reader = csv.reader(f, delimiter='|')
#     next(reader)
#     print(reader)
#     print(type(reader))
#     print(dir(reader))

#     for c in reader:
#         print(c)

# with open('./resource/sample1.csv','r', encoding='euc-kr') as f:
#     reader = csv.DictReader(f)

#     for c in reader:
#         for k, v in c.items():
#             print(k,v)
#         print('==============')

# w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
# with open('./resource/sample3.csv', 'w', newline='') as f:
#     wt = csv.writer(f, delimiter='|')
#     wt.writerows(w)

import pandas as pd
xlsx = pd.read_excel('./resource/sample.xlsx')

#상위 데이터 확인
print(xlsx.head())
print()
print(xlsx.tail())
print()

print(xlsx.shape) # 행, 열

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)