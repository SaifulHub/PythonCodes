text= input("Enter your text :")
lettercount=0
digitcount=0
wordcount=0

for t in text:
    t= t.lower()
    if t>= 'a' and t<='z':
        lettercount=lettercount+1
    elif t>='0' and t<='9':
        digitcount=digitcount+1
    elif t==' ':
        wordcount=wordcount+1
print(lettercount)
print(digitcount)
print(wordcount+1)