import re


totalSum = 0
n = "one two three four five six seven eight nine".split()

pattern = "(?=(" + "|".join(n) + "|\\d))"

def f(x):
  if x in n:
    return str(n.index(x) + 1)
  return x


for x in open('day1/example.txt'):
  digits = [*map(f, re.findall(pattern, x))]

  totalSum += int(digits[0] + digits[-1])


print(totalSum)


