num1 = int(input("enter a number :"))
num1 = num1
reverse = 0
remainder = 0
while num1 > 0 :
 remainder = num1 % 10
 reverse = reverse * 10+remainder
 num1 = int(num1//10) 

if remainder == reverse :
  print("number is palindrom")
else :
  print("number is not palindrom")