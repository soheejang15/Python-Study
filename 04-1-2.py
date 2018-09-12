# 2) 평균값 계산
# 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성

def average(*args) :
    add = 0
    
    for i in args :
        add += i

    avg =  add / len(args)
    return avg


    

    
