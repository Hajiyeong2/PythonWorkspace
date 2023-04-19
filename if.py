pocket = ['paper,', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
     print("택시를 타고가라")
else:
    print("걸어가라")
mylist = ['one', 'two', 'three']
for i in mylist:
    print(i)
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
add = 0 
for i in range(1, 11): 
    add = add + i 
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print()
