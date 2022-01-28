import random

minimum=int(input('minimum length of word to be generated: '))
maximum=int(input('maximum length of word to be generated: '))
wmaximum=int(input('max number of words to be generate in the dictionary: '))
 
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX0123456789'
str=''
file = open("Bruteforce\\sample.txt","w")
for i in range(0,wmaximum):
  for x in random.sample(alphabet,random.randint(minimum,maximum)):
      str+=x
  file.write(str+'\n')
  str=''
file.close()
print ('DONE!')