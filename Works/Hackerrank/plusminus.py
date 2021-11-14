def plusMinus(arr):
    a = 0
    b = 0
    c = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            a += 1
        elif arr[i] < 0 :
            b +=1
        else:
            c += 1

    print("%f"%(a / len(arr)))
    print("%f"%(b / len(arr)))
    print("%f"%(c / len(arr)))
    
my_arr = [0,-2,-3,5,7,6,5,9]

plusMinus(my_arr)