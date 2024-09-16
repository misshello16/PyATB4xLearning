
print (max(10,40,100))

"""Multi line comments"""

#Error will come print (max(10,40,100,"Heloma))

#Variable names
'''False,none,True,as,and,assert,async,await,break,class,continue,def,del,if.elif,else,except,finally,
for,from,global,import,in,is,nonlocal,lamda,not,or,pass,raisereturn,try,while,with,yield'''

""" Python Data types
1. integer (int) -1,2,3
2. float - 1.21,2.56
3. complex - iota - 1+2i
4. Boolean
5. String (str) - "abc"
6. List
7. Advance data type - set, dict,tuple,binary,frozen etc."""

# jhu123=456, _123=56,    ACCEPTED    Python rule: Variable should start with _ or chara
# 123=456,   567yy =-87, $12abd=123, &abc=123,  Complex numbers =2+1j   Syntax error
# "abc" and "ABC" are two different variable as python is a case sensitive language.

Complex_numbers = 2 + 1j
print (Complex_numbers.imag)
print (Complex_numbers.real)

# Python is a dynamic typed language because data type of the variable will be changed in the run time and didn't need to mention the data type.
a=8

a=4
print (a)


a,b,c=1,2,3
print (a,b,c)


#print(max(2,20,020,0020)) - SyntaxError: leading zeros in decimal integer literals are not permitted