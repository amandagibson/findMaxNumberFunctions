def findMaximumNumber(firstNumber, secondNumber):
  if firstNumber > secondNumber:
    print(f"{firstNumber} is greater than {secondNumber}!")
  elif secondNumber > firstNumber:
    print(f"{secondNumber} is greater than {firstNumber}!")
  else:
    print("Both numbers are equal!")

print("Enter the first number: ")
firstNumber = int(input())
print("Enter the second number: ")
secondNumber = int(input())

findMaximumNumber(firstNumber, secondNumber)