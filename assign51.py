#print all prime numbers
def prime_num(start ,end):
    for n in range(start,end+1):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                print(n)
start=int(input("Enter starting number:\n"))
end=int(input("Enter ending number:\n"))
prime_num(start,end)
