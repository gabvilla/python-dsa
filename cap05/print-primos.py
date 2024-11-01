primos = []

for num in range(2, 31):
   isPrimo = True
   i = 2
   while i <= num // 2:
      if num % i == 0:
         isPrimo = False
         break
      i += 1
   if isPrimo:
      primos.append(num)

print(primos)