def partition(list): 
    if len(list) <= 1:
        return list
    else:
        pivot=list[0]
        left=[]
        right=[]
        middle=[]
        for i in list:
            if i < pivot:
                left.append(i)
            elif i==pivot:
                middle.append(i)
            else:
                right.append(i)

        return partition(left)+middle+partition(right)
       
alist=[8,14,5,6,7,9]
partition(alist)

[5, 6, 7, 8, 9, 14]       
