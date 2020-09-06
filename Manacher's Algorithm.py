S=input().strip()
if S==reversed(S):
    print(S)
else:
    hashList=[ ]
    for ch in S:
        hashList.append('#')
        hashList.append(ch)
    hashList.append("#")
    noOfPal=[]
    for ctr in range(0,len(hashList)):
        length=0
        left=ctr-1
        right=ctr+1
        while(left>=0 and right<len(hashList)):
            if hashList[left]==hashList[right]:
                length+=1
                left-=1
                right+=1
            else:
                break
        noOfPal.append(length)
    subPalIndex=max(noOfPal)
    middleIndex=noOfPal.index(subPalIndex)
    if subPalIndex==1:
        for ch in hashList:
            if ch!='#':
                print(ch,end=" ")
    else:
        palindromic=[]
        for index in range(middleIndex-subPalIndex,middleIndex+subPalIndex+1):
            palindromic.append(hashList[index])
        for ch in palindromic:
            if ch!='#':
                print(ch,end="")
        
