number = range(2,101)
number_stasisc = []
for i in number:
    running = True
    for j in range(2,i):
        if i % j == 0:
            running = False
    if running:
        number_stasisc.append(i)
print(number_stasisc)










