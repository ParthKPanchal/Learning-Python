sub1=int(input("English subject marks :"))
sub2=int(input("Math subject marks :"))
sub3=int(input("Science subject marks :"))

#Check for total percentage
total_percentage = ((sub1+sub2+sub3)/300)*100

if(total_percentage>=40 and sub1 >=33 and sub2 >=33 and sub3 >=33):
    print("You are passed", total_percentage)

else:
    print("Try again next year",total_percentage)