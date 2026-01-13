#sum of even and odd numbers in list
def sum_eo(lst):
    even = 0
    odd = 0
    for n in lst:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print("Sum of Even numbers:", even)
    print("Sum of Odd numbers:", odd)
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter number: ")))
sum_eo(lst)
