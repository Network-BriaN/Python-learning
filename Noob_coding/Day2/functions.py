def sayhi():
    print("Hello user")

print("Top")
sayhi()
print("Bottom")

def say_hi(name,age):                               #passing parameters inside a function
    print("Hello " +name+ ", You are " +str(age))   #for integer passing use str
print()                                             #for spacing
say_hi("Safal", 21)
say_hi("Brian", 20)
