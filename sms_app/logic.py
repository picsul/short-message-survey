# import some stuff
from . import db

# this file uses whatever logic we have to return a question number that comes next

def tester(val, cond, yes, no):
    val = val.lower()
    if eval(cond) == True:
        return yes
    elif eval(cond) == False: 
        return no
    


