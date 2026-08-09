
Student =input("Enter student name: ")
sub1= int(input("Enter frist subject marks: "))
sub2= int(input("Enter second subject marks: "))
sub3= int(input("Enter third subject marks: "))
sub4= int(input("Enter fourth subject marks: "))
sub5= int(input("Enter fifth subject marks: "))
totalmarks = sub1+sub2+sub3+sub4+sub5
percentage = (totalmarks)/5
if(percentage>=90):
          print("A grade")
elif(percentage>=80):
    print("B grade")
elif(percentage>=70):
    print("C grade")
elif(percentage>=60):
    print("D grade")
else:
    print("Fail")

print(Student)
print(totalmarks)
print(percentage)

 
           
