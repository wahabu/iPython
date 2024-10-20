class Rectangle:
  base = int(input("Input a base: "))
  height = int(input("Input a height: "))
  
  def getArea(self):
   return self.base * self.height

rect = Rectangle()
area = rect.getArea()
print(area)