
import random

LETTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
codex={}
mixPhrase=[]

# START
def start():
    phrase =input("Please enter a phrase. \n").lower()
    encode(phrase)

# This function encrypts the phrase
# ENCODE
def encode(phrase):
    for i in phrase:
        if i.isalpha():
            if i not in codex:
                ranLet=random.choice(LETTER)
                if i == ranLet:
                    encode(phrase)
                codex[i]=ranLet
                mixPhrase.append(ranLet)
                if len(LETTER) >0:
                    LETTER.remove(ranLet)
            elif i in codex:
                mixPhrase.append(codex.get(i))
        else:
            mixPhrase.append(i) 

    key=random.choice(list(codex.items()))
    write(key,phrase) 

    print("Your hint is "+ str(key))     
    print(' '.join(mixPhrase))
 
    
# The "key" parameter right now is the hint a user gets and may be used later for a decode function.
# WRITE
def write(key,phrase):
    f=open("crypto.txt",'a+')
    f.write('Phrase: ')
    
    for j in phrase:
        f.write(j)

    f.write('\n')
    f.write('Jumble: ')
    for i in mixPhrase:
    
        f.write(i)
    f.write('\n')

    f.write('Key: ')
    f.write(str(key))
    f.write('\n')
    f.close()

