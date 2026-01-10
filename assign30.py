#feedback count dashboard
feed={"Positive": 45, "Neutral": 18, "Negative": 7}
cal=sum(feed.values())
print("Total number of feedback are:",cal)
type=max(feed.values())
print("Value of highest key is:",type)
high=max(feed,key=feed.get)
print("Key of highest value is:",high)








    
