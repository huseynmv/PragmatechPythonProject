def birthdayCakeCandles(ar):

    ar.sort()

    result = ar.count(ar[len(ar)-1])
    print (result)

arr = [4,3,2,1]

birthdayCakeCandles(arr)