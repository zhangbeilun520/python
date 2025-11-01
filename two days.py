import random
number = random.sample(range(1000000),100)
numbers_line = []
running = True
while running:
    if(len(number)) == 0:
        running = False
    else:
        a = max(number)
        number.remove(a)
    numbers_line.append(a)
line = sorted(numbers_line)
print(line)


a = 1
b = 1
count = 0
number_line = [1,1]
while count < 100:
        c = a + b
        number_line.append(c)
        a = b
        b = c
        count += 1
print(number_line)






