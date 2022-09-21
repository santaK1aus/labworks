def allpali(s):
	s1=set()
	i=0
	length=len(s)
	while(i<length):
		pa=s[i]
		s1.add(pa)
		j=1
		while((i+j)<length and (i-j)>-1):
			if s[i+j]!=s[i-j]:
				break
			pa=s[i-j]+pa+s[i+j]
			s1.add(pa)
			j+=1
		j=0
		pa=''
		while((i+j+1)<length and (i-j)>-1):
			if s[i-j]!=s[i+1+j]:
				break
			pa=s[i-j]+pa+s[i+1+j]
			s1.add(pa)
			j+=1
		i+=1
	lw=list(sorted(s1))
	rs=''.join(lw)
	return rs
	
#print(allpali('abbab'))
length=int(input())
s=input('')
q=int(input(''))
ps=allpali(s)
while(q>=0):
	s=input().split(' ')
	a=int(s[0])
	b=int(s[1])
	if a<1 or b>len(ps):
		print('-1')
	else:
		print(ps[a-1:b])
	q-=1

