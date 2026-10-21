marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=91):
    print("You got A grade")

elif(marks<=90 and marks>=71):
    print("You got B grade")

elif(marks<=70 and marks>=61):
    print("You got C grade")

elif(marks<=60 and marks>=41):
    print("You got D grade")

elif(marks<=40 and marks>=35):
    print("You got E grade")

else:
    print("You got F grade")