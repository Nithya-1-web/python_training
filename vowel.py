text=input("enter a string :")

vowels="aeiouAEIOU"

print("vowels in the string are:")
for char in  text:
    if char in vowels:
        print(char)
