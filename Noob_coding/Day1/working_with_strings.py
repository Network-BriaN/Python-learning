phrase = "giraffe academy"      		#store string inside a variable
print(phrase+ " is stupid")     		#concatenation

print(phrase.upper())          		#built-in function to convert entire string into upper/lower case
                                		#() are called paranthesis

print(phrase.islower())         		#returns boolean value of true coz the phrase is entirely lower
print(phrase.isupper())         		#returns boolean value of false coz the phrase is entirely lower
print(phrase.upper().isupper()) 		#converts phrase into upper and then return bool true

print(len(phrase))              		#returns number of char in the string
print(phrase[2])                		#returns the char in the position specified
print(phrase.index("f"))        		#returns the index value of the first character
print(phrase.index("acad"))     		#returns the start of the given word
#print(phrase.index("x"))       		#return error as x is not present in the phrase
print(phrase.replace("giraffe", "sloth"))  	#replace a certain string

print("Giraffe\nacademy")       #the string after \n will pe print on new line
print("Giraffe\"Academy")       #literally prints the string " after \ ignoring its use
print("Giraffe\ academy")       #normal use
