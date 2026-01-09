#tuple
roll_no=(67,42,66,53)
print(roll_no[2])
print(roll_no[-3])
print(roll_no[1:3:2])

#methods
print(roll_no.count(66))
print(roll_no.index(42))
print(roll_no)

#deleting an element
rol=list(roll_no)
rol.pop()
roll_no=tuple(rol)
print(roll_no)

