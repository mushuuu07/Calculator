num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(" 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n");
ch = int(input("Enter the choice Mathematical Operator:"))
if (ch == 1):
     ans = num1 + num2
     print("Sum =",ans)
elif (ch == 2):
     ans = num1 - num2
     print("Sub =",ans)
elif (ch == 3):
     ans = num1 * num2
     print("Mul =",ans)
elif (ch == 4):
     ans = num1 / num2
     print("Div =",ans)
else:
     print("Invalid Choice")