import random

_list = 'abcdefghijklmnopqrstuvwxyz'
str1_5 = ''
str6_10 = ''
for i in range(5):
    str1_5 = str1_5 + random.choice('2468')
for i in range(5):
    str6_10 = str6_10 + random.choice('abcdefghijklmnopqrstuvwxyz')
str11_12 = 'AB'
for i in str1_5:
    if i == '8':
        str11_12 = 'XY'
print(str1_5 + str6_10 + str11_12)