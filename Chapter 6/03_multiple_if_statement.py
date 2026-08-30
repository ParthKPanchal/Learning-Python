age = int(input("Enter your age: "))

# If statement no 1
if(age==0):
    print("You age can not be zero")
    
print("End of if statement no 1")

# If statement no 2
if(age>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(age<0):
    print("You are entering invalid age")

else:
    print("You are below the age of consent")

print("End of if statement no 2")