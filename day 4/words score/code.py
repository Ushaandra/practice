def score_words(s):
    v=['a','e','i','o','u','y']
    score=0
    for i in s:
        count=0
        for j in i:
            if j in v:
                count+=1
        if count%2==0:
            score+=2
        else:
            score+=1
    print(score)
n=int(input())
s=input().split()
b=score_words(s)
        
            
