# Calculator

class FourCal :

    # 생성자
    def __init__(self,first,second):
        self.first = first
        self.second = second

    # 생성자와 동일한 기능을 가진 메소드
    '''def setdata(self,first,second):
        self.first = first
        self.second = second'''

    def sum(self) :
        result = self.first + self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result


# 클래스의 상속

class MoreFourCal(FourCal) :
    def pow(self):
        result = self.first ** self.second
        return result


# 클래스 오버라이드

class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

        
