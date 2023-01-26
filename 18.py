def dh(s, t):
if len(s) != len(t):
 return -1
 return sum(es != et for es, et in zip(s, t))
def dhplus(s, t):
 sprime = s+’.’*(len(t)-1)
 tprime = ’.’*(len(s)-1)+t
 dist = max(len(s), len(t))
 for x in range(len(s)+len(t)-1):
 sprime = sprime[-1]+sprime[:-1]
 pardist = dh(sprime, tprime)
 dist = min(dist, pardist)
 return dist


 #non funziona