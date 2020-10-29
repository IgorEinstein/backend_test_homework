class Calculator:
     def __init__(self,first,second,finish):
         self.first = first
         self.second = second
         self.finish = finish

    
     def show(self):
        print(f"Первая {self.first}, вторая: {self.second}")


qqq = Calculator("1","777","5")

qqq.show()