my_list = [0,-2,4,7,9,3,10]
# Write a Python function to multiply all the numbers in a list.
sum = 1
for i in my_list:
    sum=sum*i
print (sum)

# Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

summ=0
for i in my_list:
    summ+=i
print(summ)

#  Write a Python program to select the odd items of a list.

odd=[number for number in my_list if number%2==1]
print(odd)

# Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

e=input("Birinci ededi daxil edin : ")
f=input("Ikinci ededi daxil edin : ")
g=input("Ucuncu ededi daxil edin : ")
h=input("Dorduncu ededi daxil edin : ")

if e>=f and e>=g and e>=h :
    print("En boyuk eded : ", e)
elif f>=e and f>=g and f>=h :
    print ("En boyuk eded : ", f)
elif g>=e and g>=f and g>=h : 
    print("En boyuk eded : ", g)
else:
    print("En boyuk eded", h)
# Write a Python program to check a list is empty or not.

list=[1,2,3]
def foo(a):
    if len(a)==0:
        print ("list boshdur")
    else:
        print("list bosh deyil")

foo(list)

#  Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin

max = my_list[0]
min = my_list[0]
for i in my_list:
    if i > max:
        max=i
    elif i <=min:
        min = i

print(max)
print(min)



# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

a=int(input('Birinci eded: '))
b=int(input('ikinci eded: '))
c=int(input('ucuncu eded: '))
d=int(input('dorduncu eded: '))

if a==b and a==c and a==d:
    print("kvardatin sahesi = ", a*a)
else :
    print('perimetr = ', a+b+c+d)

# Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.

def returnDay(self):
    days = ["bazar ertesi", "cershenbe axshami", "cershenbe", "cume axsham", "cume", "shenbe", "bazar"]

    if self < 1 or self > 7:
        print('None')
    else:
        for i in days :
            day = days[self-1]
        print(day)
returnDay(3)


# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

sample = ['abc', 'xyz', 'aba', '1221']

say = 0
for i in sample:
    if len(i) > 1 and i[0] == i[-1]:
        say += 1
print(say)


#  Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

menu = ["alma", "armud", "heyva", "nar"]
print (menu)

h = input("qiymetini bilmek istediyiizizn adini yazin: ")
if h=="alma":
    print ("3manat")
elif h=="armud":
    print ("1manat")
elif h=="heyva":
    print ("2manat")
elif h=="nar":
    print ("pulsuz")
else:
    print ("bu meyve menuda yoxdur")


ad = input("Adinizi daxil edin: ")
if len(ad)>3 and len(ad)<11:
    soyad = input('Soyadinizi daxil edin: ')
    if len(soyad)>5 and len(soyad)<15:
        il=(input("Dogum ilinizi daxil edin: "))
        if len(il)==4:
            email=input("Emailinizi daxil edin: ")
            if email.endswith("@gmail.com") and len(email)>10 and len(email)<22:
                password=input("Shifrenizi yazin: ")
                if len(password)>6 and len(password)<13:
                    confirm = input("Shifrenizi tesdiqleyin: ")
                    if confirm==password:
                        print("Qeydiyyat tamamlandi")
                        detallar=input("Detallara baxmaq isteyirsinizmi? he/yox ")
                        if detallar=="he"or detallar=="He":
                            print(f'Ad : {ad}, Soyad : {soyad}, Dogum ili : {il}, Email : {email}, Password : {password}')
                        else:
                            print(f'Ugurlar {ad}')
                    else:
                        print("Daxil etdiyiniz shifreleer eyni deyil")
                else:
                    print("Shifreniz uzunlugu 6 ve 13 arasi olmalidir")
            else:
                print("Emailiniz yanlishdir")

        else:
            print("Dogum ilinin uzunlugu 4 olmalidir")
    else:
        print("Soyadin uzunlugu 5 ve 15 araliginda olmalidir")
else:
    print("Adin uzunlugu 3 ve 11 arasinda olmalidir")



# my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.


my_text = "write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."

newStr = my_text.split()
print (newStr)
sorted = sorted(newStr)
print(" ".join(sorted))


