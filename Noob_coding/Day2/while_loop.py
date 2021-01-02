import time                         #for delay
i = 10

while i >= 1:                       #if true, jump to next statement; else, escape the loop
    print(str(i)+ " secs to go")
    time.sleep(1)                   #setting delay for 1 sec after every countdown
    i -= 1

time.sleep(1)                       #setting delay for 1 sec after while loop
print()
print()
print("BOOOOMMMM!!!!!!")
