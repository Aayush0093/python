def highest_even(li):
    evens=[]
    for i in li:
        if i%2==0:
            evens.append(i)

    max=0
    for i in evens:
        if(i>max):
            max=i

    return max

print(highest_even([10,2,3,4,8,110]))