for x in range(151):
    print(x)

for x in range(5, 1005, 5):
    print(x)

for x in range(1,101):
    if x % 5 == 0:
        print("Coding")
    elif x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)

sum = 0
for x in range(1,50000,2):
    sum += x
print(sum)

for x in range(2018, 0 , -4):
    print(x)

def flexible_counter(low_num, high_num, mult):
    for x in range(low_num, high_num + 1):
        if x % mult == 0:
            print(x)
flexible_counter(2, 9, 3)