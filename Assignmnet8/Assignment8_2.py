import threading

def even(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            sum += i
    print("Sum of even factors:", sum)

def odd(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            sum += i
    print("Sum of odd factors:", sum)

num = int(input("Enter a number: "))
t1 = threading.Thread(target=even, args=(num,))
t2 = threading.Thread(target=odd, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
