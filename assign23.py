n=7
visit=[]
print("Enter the number of visitors:\n")
for i in range(n):
    visit.append(int(input()))
for i in visit:
    print(f"Number of Visitors of a day are",i)
high=max(visit)
low=min(visit)
higher=visit.index(high)+1
lower=visit.index(low)+1
print("Highest traffic on day ",higher)
print("Lowest traffic on day ",lower)
