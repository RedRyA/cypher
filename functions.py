
import random

LETTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
codex={}
mixPhrase=[]
decodePhrase = []

# START
def start():
    select=input("Encode or Decode? \n").lower()
    
    phrase =input("Please enter a phrase. \n").lower()

    if select=='encode':
        encode(phrase)
    elif select =='decode':
        decode(phrase)
    else:
        start() 

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
 
 # DECODE
def change():
        old=input("Letter to change: \n")
        new=input(f'Change {old} to ? \n')
        codex[old]=new
        print('Codex ',codex)
        print('Original: ',mixPhrase)
        for j in range(len(decodePhrase)):
            if decodePhrase[j] == old:
                decodePhrase[j] = new
                
            
        print('New: ',decodePhrase)
        change()

def  decode(phrase):
    for i in phrase:
        mixPhrase.append(i)
        decodePhrase.append(i)
    choice = input('Change or revert \n').lower()
    if choice == 'change':
        change()
    
   

        
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

