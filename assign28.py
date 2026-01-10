#online exam score
score=[96,86,95,98,88,92]
total_score=sum(score)
print("Total Score is:",total_score)
avg=total_score/len(score)
print("Average Score is:",avg)
count=0
for i in range(len(score)):
    if score[i]>avg:
        count+=1
print("Count of scores above average is:",count)
