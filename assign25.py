#inventory stock comparision
opens=[100,150,90,45]
close=[90,45,100,16]
print("Opening Stock is :",opens)
print("Closing Stock is :",close)
for i in range(len(opens)):
    if close[i]>opens[i]:
        print(f"Product{i+1}: Closing Stock increased ")
    elif opens[i]>close[i]:
        print(f"Product{i+1}: Closing Stock reduced")
    else:
        print(f"Product{i+1}: No changes")
    
