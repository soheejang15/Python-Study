# 3) Calculator 3
class Calculator :
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val
