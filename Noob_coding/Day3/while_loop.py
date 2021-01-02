MonthConversions = {
    "jan" : "January",      #numbers can also be used for keys
    "feb" : "February",
    "mar" : "March",
    "apr" : "April",
    "may" : "May",
    "jun" : "June",
    "jul" : "July",
    "aug" : "August",
    "sept" : "September",
    "oct" : "October",
    "nov" : "November",
    "dec" : "December",
}
m = str(input("Enter the starting three letters of your month: "))
print(MonthConversions.get("dec"))      #first way of getting te key
print(MonthConversions[m])              #other way of getting the key

n = str(input("Enter the starting three letters of another month: "))
print(MonthConversions.get(n , "Not Valid"))        #to pass a default definition when keys dont match
