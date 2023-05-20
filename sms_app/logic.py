# import some stuff
from . import db

# this file uses whatever logic we have to return a question number that comes next

answer = "yEs"
te = "val == 'yes'"
y = 1
n = 2

def tester(val, cond, yes, no):
    val = val.lower()
    if eval(cond) == True:
        return yes
    elif eval(cond) == False: 
        return no
    


