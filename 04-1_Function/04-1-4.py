# 4) 피보나치
# n 이하까지의 피보나치 수열 출력

def fibo (n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return (fibo(n-1))+(fibo(n-2))
