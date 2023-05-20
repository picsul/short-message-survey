# import some stuff
from . import db

# this file uses whatever logic we have to return a question number that comes next

def ifelse(cond, yes, no):
    if cond == True:
        return yes
    elif cond == False: 
        return no
