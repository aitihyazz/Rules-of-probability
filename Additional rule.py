def probaorb(a,b,allpossibleoutcome):
    proba=len(a)/len(allpossibleoutcome)
    probb=len(b)/len(allpossibleoutcome)
    inter= a.intersection(b)
    probinter=len(inter)/len(allpossibleoutcome)
    return (proba +probb -probinter)
even={2,4,6}
greatethantwo={3,4,5,6}
allpossibleroll={1,2,3,4,5,6}
print("Prob of getting a even num greater than 2")
print(probaorb(even,greatethantwo,allpossibleroll))