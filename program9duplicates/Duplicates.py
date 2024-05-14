some_list=['a','b','c','b','d','m','n','n']
lst=[]
count=0
for i in some_list:
    count=0
    for j in some_list:
        if i==j:
            count+=1
            if count==2:
                if i not in lst:
                    lst.append(i)
print(lst)