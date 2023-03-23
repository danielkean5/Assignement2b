import math 

diameter = input('Insert Diameter of a circle. \n')

while True:
  if diameter.isnumeric():
    diameter = float(diameter)
    area = math.pi*(diameter/2)**2
    circumfrence = math.pi*diameter
    print("The area of your circle is ",area)
    print("The circumfrence of your cirlce is ",circumfrence)
    break
  else:
    diameter = input('Unsuccesful. \n')