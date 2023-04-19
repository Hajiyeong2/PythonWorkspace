a="Life is too short. You need Python"
print(a[0]+a[9]+"v"+a[-9])
print(a[0:4])
today="2023년 4월 10일 월요일"
year = today[0:5]
month = today[6:8]
date = today[9:12]
day = today[13:]
print(year)
print(month)
print(date)
print(day)
str = "저는 {0}학번, {1}입니다.".format(2019, "하지영")
print(str.replace('저는 ',''))
b = [1, 2, ['a', 'b', ['Life', 'is']]]
print(b[2][2][0])
c = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(c[3][0:2])
d=[1,2,3,[78,99]]
print(d.count(99))
dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name'])