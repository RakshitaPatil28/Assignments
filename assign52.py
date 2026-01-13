#count vowels and consonant in string
def countvc(s):
    vowels="aeiouAEIOU"
    v=0
    c=0
    for i in s:
        if i.isalpha():
            if i in vowels:
                v+=1
            else:
                c+=1
    print("Vowels:",v)
    print("Consonants:",c)
text=input("Enter a string:\n")
countvc(text)
