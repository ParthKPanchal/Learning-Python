age = int(input("Enter your age: "))
if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(age<0):
    print("You are entering invalid age")

elif(age==0):
    print("You age can not be zero")
    
else:
    print("You are below the age of consent")

print("End of Program")