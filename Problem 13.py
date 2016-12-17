# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

total = 0
with open('numbers.txt') as my_file:
   for line in my_file:
      total += int(line)
total_2 = 0
print(total)
total = str(total)
total = ' '.join(total)
total = total.split()
for i in range(10):
   total_2 += int(total[i])


print(total_2)