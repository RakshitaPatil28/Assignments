#armstrong number
def armstrong_num(n):
    temp = n
    total = 0
    digit = len(str(n))

    while temp > 0:
        d = temp % 10
        total += d ** digit
        temp //= 10

    if total == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

num = int(input("Enter a number: "))
armstrong_num(num)
