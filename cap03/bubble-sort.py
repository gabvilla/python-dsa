numbers = [23, 93, -123, 0.98, 0, 10, 1000, 20000, 30, 0.434221, -2000, 30]
listLength = len(numbers)

for i in range(listLength):
   for j in range(0, listLength - 1):
      if numbers[j] > numbers[j + 1]:
         numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

         
print(numbers)