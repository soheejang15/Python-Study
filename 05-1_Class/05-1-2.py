# 2) Calculator 2
class Calculator :
    # default 값으로 지정해 둘 수 있음.
    def __init__(self,init_value = 0) :
        self.value = init_value

    def add(self, val) :
        self.value += val
        
