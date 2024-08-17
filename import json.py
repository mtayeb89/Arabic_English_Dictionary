import json
from pystyle import *
print(Box.Lines('[+]Welcome to my Github Account'))
Write.Print('[-] this program for Dictionary \n',Col.purple)
print(Box.DoubleCube('Mahmoud Eltayeb'))
while True:
    word=input('Please Enter your word: ')
    f=open('The Oxford English Arabic Dictionary.json','r',encoding='utf-8')
    learn=json.load(f)
    if word in learn:
        print(f"The English translation for '{word}' is: {learn[word]}")
    else:
        print(f"Sorry, the word '{word}' is not found in the dictionary.")