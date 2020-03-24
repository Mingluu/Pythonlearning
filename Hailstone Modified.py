def hailstone(a,b,x):
    i = x
    #print(x,':')
    myset = set()
    pattern=[]
    count=0
    while i not in myset:
        myset.add(i)
        #print(myset)
        i = i//2 if i%2==0 else i*a+b
        count += 1
        if count > 10*a*b*x:
            #print('infinite')    
            return None
            
    j=i
    while True:
        pattern.append(j)
        #print(myset)
        j = j//2 if j%2==0 else j*a+b
        if(j == i):
            pattern.append(j)
            break
    return pattern

for a in range(1,11):
    for b in range (1,11):
        setdic= set()
        print('('+str(a)+','+str(b)+'):')
        for x in range (2,11):
            #print(a,b,x)
            pattern = hailstone(a,b,x)
            if pattern != None and hash(frozenset(pattern)) not in setdic:
                setdic.add(hash(frozenset(pattern)))
                print('\tPattern -',pattern)   
        if len(setdic)==0:
            print('\tThere is no cycle in this combination.')
