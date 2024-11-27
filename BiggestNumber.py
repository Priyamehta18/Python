num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))
num4=int(input("Enter the fourth number : "))

if num1>num2 and num1>num3 and num1>num4:
    big=num1
elif num2>num3 and num2>num4:
    big=num2
elif num3>num4:
    big=num3
else:
    big=num4
    
if num1<num2 and num1<num3 and num1<num4:
    small=num1
elif num2<num3 and num2<num4:
    small=num2
elif num3<num4:
    small=num3
else:
    small=num4
print("Biggest number is", big , "and" ,"smallest number is", small,".") 


        