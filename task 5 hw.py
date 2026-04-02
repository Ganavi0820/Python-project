a=int(input("enter the marks"))
if(a>=90) and (a<=100):
    print("The grade is A+")
elif(a>=89) and (a<=90):
    print("the grade is A")
elif(a>=71) and (a<=80):
    print("the grade is B")
elif(a>35) and (a<=70):
    print("the grade is C")
elif(a>=0) and (a<=35):
    print("the student is failed")
else:
    print("invalid marks")