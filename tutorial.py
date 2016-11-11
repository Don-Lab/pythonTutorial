#Python tutorial

"""
-Python is a general programming language meaning it can be used for different purposes.
-Indentation is IMPORTANT
"""

#single line comment
"""
multi
line
comment
"""

#declaring variables
varInt = 34 #data type: int
varStr = "Text" #data type: string
varFlo = 3.14 #data type: float (decimal)
varBoo = True #data type: boolian (bool) only 'True' or 'False'

#Print
print(varInt) #print variables
print("Hello World") #print strings directly
print(57) #print int

"""
operators (used especially in conditionals('if' and 'else'))

==  sees if two things are equal "of value and can apply to strings and variables

===  sees if value is equal and data type is the same

>  greater than

>=  greater than or equal to

<  less than

<=  less than or equal to

!=  not equal to
"""

#if/else statement
#only runs the statement that is true
x = 75
y = 37
if x >= y: 
    print("\'x\' is greater than \'y\'")  #   \' makes the quote mark show
elif x == y: 
    print("They are equal")     #will not show because it is not true
else:
    print("\'y\' is greator than \'x\'")    #y being greater than x is the only other option
	
#while loop
#while the condition is true, it will loop
t = 10
while t >= 0:
    print("While loop")
    t -= 1 #  -= subtracts the value following value and assigns it to the variable

#for loop
#loop the following 10 times
for x in range(10):
	print("for loop")
	
#lists (arrays)
listInt = [12, 23, 43, 64, 65, 7, 67, 58]
#printing lists
for listInt in listInt:  #loop thought the amount of items in the list
	print(listInt) #print the item in the list
	
#def (functions)
#run blocks of code when called
def add(a, b): #command funcName(parameter):
	return print(a + b)

add(5, 4)
#parameters are variables for functions to use (not all variables used in functions must be parameters)

#dictionary
"""
dictionaryName {
	"key1": "value1",
	"key2": "value2",
	"key3": "value3"
}
"""
lunch = {
	"main" : "Hot Pocket",  #separate items with a comma
	"side" : "chips"
}
print(lunch["main"]) #call with dictionaryName[Key]