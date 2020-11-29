R = [125,171,24323,38037,67387,125963,206558,396695,579229,826869,1213515,1465973,1884054,2163815,2653410,3031562,3453339,3820098,4135091]
I = [6511,19649,16013,47660,90134,164879,278980,355087,476895,558789,548218,632192,698317,815986,733970,719655,640373,572438,521984]
D = [242,1140,2741,6410,11625,20082,29314,39797,50058,59656,70524,80251,91377,101136,111189,120498,127517,135857,142161]
N = []
lamb = 3.72*10**(-4)
n = 209500000
mu = 1.76*10**(-4)
beta = 1.8181
for i in range(len(I)):
	N.append(1+(lamb-mu)*i)
for i in range(len(I)):
	I[i] = I[i]/(N[i]*n)
	R[i] = R[i]/(N[i]*n)
	D[i] = D[i]/(N[i]*n)
dI = []
dR = []
dD = []
for i in range(len(I)-1):
	dI.append(I[i+1] - I[i])
	dR.append(R[i+1] - R[i])
	dD.append(D[i+1] - D[i])

E = []
S = []
for i in range(len(dI)):
	e = (dI[i] + dR[i]+dD[i]+mu*(I[i]+R[i]))/beta
	S.append(N[i] - (e + I[i] + R[i] + D[i] + (lamb - mu)*i))
	E.append(e)
dS = []
for i in range(len(S) - 1):
	dS.append(S[i+1] - S[i])
alph = 0
gam = 0
delt = 0
for i in range(len(dS)):
	alph +=  (lamb*N[i] - dS[i] - mu*S[i])/((S[i]*E[i] + S[i]*I[i])*len(dS))
	gam += (dR[i] + mu*R[i])/(I[i]*len(dS))
	delt += dD[i]/(I[i]*len(dS))
print(alph,gam,delt)