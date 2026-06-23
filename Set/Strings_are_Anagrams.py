s="listen"
t="silent"

s1=set()
s2=set()

for i in s:
    s1.add(i)

for j in t:
    s2.add(j)

s3= s1-s2 

if len(s3)==0:
    print("yes ")