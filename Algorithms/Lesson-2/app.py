import math, random
# n natural ədədi verilmişdir. Əgər n ədədi hər hansı bir m natural ədədinin kvadratıdırsa, onda m ədədini çap edin, əks halda No çap edin. Məsələn: User 25 daxil etsə ekrana 5 verilsin 27 daxil etsə, NO yazılsın

number=int(input("Eded daxil edin : "))
root=math.sqrt(number)
if int(root)**2==number:
    print(root)
else:
    print(number)

# User bir ədəd daxil etsin həmin ədədə qədər bütün ədədləri çapa verin.

a=int(input("Eded daxil edin : "))
b=[]
for i in range(1,a):
    b.append(i)
print(b)

# İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin.

string="İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin."
newStr=[]
for i in range(0, len(string), 2):
    newStr.append(string[i].split())
print(newStr)

# Userdən daxil etmısini tələb edin. 1-dən sonra gələn ən kiçik bölünəni çapa verin.



# Userdən bir ədəd daxil etməsini tələb edin. Ekrana həmin ədəddəki ədədlərin hasilini çapa verin.

a=int(input("Eded daxil edin : "))
hasil=1
for i in range(1,a+1):
    hasil=hasil*i
print(hasil)


# 1-50 arasında ədədlərdən 3-ə bölünən ədədlərə three, 5-ə bölünən ədədlərə five, həm 3 və həm də 5-ə bölünənlərə isə ThreeFive print edin. Əgər heç birinə bölünməsə sadəcə ədədin özünü çapa verin.

for i in range(1,51):
    if i%3==0:
        print(f'{i} three')
    elif i%5==0:
        print(f'{i} five')
    elif i%3==0 and i%5==0:
        print(f'{i} threefive')
    else: 
        print(i)


# Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək. Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır. Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.

# Kvadrat tənliyin əmsallarını daxil etsin user. Həmin əmsallara görə tənliyin köklərini daxil edin.

a=int(input('A-ni daxil edin : '))
b=int(input('B-ni daxil edin : '))
c=int(input('C-ni daxil edin : '))
d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('x1 = ',x1)
    print('x2 = ',x2)
elif d<0:
    print('kvadrat tenliyin koku yoxdur')
elif d==0:
    x1=x2=(-b)/(2*a)
    print("Tenliyin kokleri eynidir ",x1)


# Random bir rəqəm götürsün proqram 1-4 aralığında. İstifadəçidən həmin rəqəmi təxmin etməyi istəyin. Hər doğru təxmin etdikcə istifadəçi bir xal qazansın. 5 xala çatanda istifadəçinin 5 xala çatması üçün etdiyi cəhdlərin sayını çapa verin.




texmin = 0
xal = 0

while xal!=5:
    appNumber = random.randint(1,4)
    texminedilen = int(input("Texmin etdiyiniz ededi yazin :  "))
    texmin+=1
    if appNumber == texminedilen:
        xal+=1
        print(f'{xal} xaliniz var.')
    else:
        print("Bextinizi bir daha sinayin")
print(texmin)

#  Harshad or not

def Harshad(x):
    sum=0
    for i in str(x):
        sum=sum+int(i)
    if x%sum==0:
        print("harshad")
    elif x%sum!=0:
        print("Not harshad")

Harshad(15)