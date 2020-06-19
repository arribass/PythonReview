' Author Adrian Arribas'
#Math commands
#abs(value), log(value), log10(value), max(val1, val2),
#min(val1, val2), round(value), sin(value), sqrt(value) --> similar to R
#constant --> e and pi
import math
x = -1
y = 2
mi_valor_pi = 3.14
ang1 = 90
number = 64
print(math.fabs(x))
print(math.log(2,2))
##f strings only work on python3
print(f"The minvalue is : {min(x,y)}")
print(f"The value of pi rounded is  : {round(mi_valor_pi)}")
print(f"The sinus of the angle is : {math.sin(ang1)}")
print(f"the value of the squareroot of {number} is:  {math.sqrt(number)}")
