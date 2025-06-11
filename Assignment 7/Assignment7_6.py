def prime(l1):
    l2 = []
    for num in l1:
        j = 0
        for i in range(2, num):
            if num % i == 0:
                j += 1
        if j == 0 and num > 1:
            l2.append(num)
    return l2

a = int(input("Enter number of elements in a list: "))
l1 = []
for _ in range(a):
    b = int(input("Enter element: "))
    l1.append(b)

l2 = prime(l1)
print("Prime numbers:", l2)
