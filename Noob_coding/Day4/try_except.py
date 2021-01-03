#error handling

try :
    ans1 = 10/0
    ans2 = int(input("Enter an Integer : "))
    print(ans2)

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid input")
