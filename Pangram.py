#Count the occurence of vowels in the string entered by the user
inp=input("Enter the string")
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0

}
for v in inp:
    if v in vowels:
        vowels [v]+=1
print(vowels)
#Method 2
n=input("Enter the string")
vowelslist=["a","e","i","o","u"]
vowels={    
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for p in n:
    if p in vowelslist:
        if p in vowels:
            vowels[p]+=1
        else:
            vowels[p]=1
print(vowels)
#Count the occurence of alphabet in the string entered by the user
inp=input("Enter the string")
alphabet={
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0

    

}
for inp in alphabet:
    if inp in alphabet:
        alphabet[inp]+=1
panagram=True  
for count in alphabet.values():
    if count == 0:
        panagram=False
if panagram:
    print("Entered string is a panagram")
else:
    print("Entered string is not a panagram")




numberstring=input("Enter the number")
numbercount={
    
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}
for num in numberstring:
    if num in numbercount:
        numbercount[num]+=1
panagram=True  
for count in numbercount.values():
    if count == 0:
        panagram=False
if panagram:
    print("Entered number is a panagram")
else:
    print("Entered number is not a panagram")