# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

number = 2**1000
s_number = str(number)
total = 0
for n in s_number:
   total += int(n)
print(total)