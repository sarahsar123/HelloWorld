import math
# 1. volume of rectangleSolid
# 2. volume of sphere
# 3. volume of cylinder
# 4. volume of cone

def rectangleSolid(l,w,h):
  return l*w*h
def sphere(r):
  return (4/3)*r**3
def cylinder(r,h):
  return math.pi*r**2*h
def cone(r,h):
  return (1/3)*r**2*h

choice=int(input(' Choose your volume calculation= '))
if choice==1:
  l=float(input('What is the length= '))
  w=float(input('What is the width= '))
  h=float(input('What is the height= '))
  print(f"volume of rectangle solid =  {rectangleSolid(l,w,h)}")
elif choice==2:
  r=float(input('What is the radius= '))
  print(f"volume of spehere= {sphere(r)}")
elif choice==3:
  r=float(input('What is the radius= '))
  h=float(input('What is the height '))
  print(f"volume of cylinder= {cylinder(r,h)}")
else:
  r=float(input('What is the radius '))
  h=float(input('What is the height '))
  print(f"volume of cone= {cone(r,h)}")