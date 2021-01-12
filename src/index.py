import re



def solve(s,*a):
	l=len(a)
	if (l!=len(s)):
		raise RuntimeError
	ov=[]
	m=[]
	om=[]
	o={}
	for i,k in enumerate(a):
		m+=[[0 for _ in range(0,l)]]
		om+=[[(1 if i==j else 0) for j in range(0,l)]]
		if (len(a)==0):
			raise RuntimeError
		for e in k.replace("-","+-").split("+"):
			if (len(e)==0):
				continue
			v=1
			for n in re.findall(r"-?[0-9]*(?:\.[0-9]+)?",e):
				if (len(n)==0):
					continue
				if (n=="-"):
					v=-v
				else:
					v*=float(n)
			n=re.sub(r"[0-9\.\-]","",e)
			if (len(n)>1):
				raise RuntimeError
			if (n not in ov):
				ov+=[n]
				o[n]=0
			m[-1][ov.index(n)]=v
	for i in range(0,l):
		if (m[i][i]==0):
			raise RuntimeError
		t=1/m[i][i]
		for j in range(0,l):
			m[i][j]*=t
			om[i][j]*=t
		for j in range(0,l):
			if (i==j):
				continue
			t=m[j][i]
			for k in range(0,l):
				m[j][k]=m[j][k]-t*m[i][k]
				om[j][k]=om[j][k]-t*om[i][k]
				if (i==l-1):
					o[ov[j]]+=om[j][k]*s[k]
	return o



print(solve([5,6,7],"a+b+4c","-8b+c","a+b"))
