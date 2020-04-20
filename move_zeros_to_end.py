def move_zeros(arr):
    l = [i for i in arr if isinstance(i,bool) or i!=0]
    l.extend([0] * (len(arr)-len(l)))
    return l

    
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))