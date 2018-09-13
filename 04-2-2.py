# 2) 숫자의 총합

number = input("숫자 입력 (콤마로 구분) : ")
number = number.split(',')

sum = 0
for i in number :
    sum += (int(i))


print("숫자 총합 : "+ str(sum))  
