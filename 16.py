s1 = 'CGAT'*10000
import random
s2 = ''.join([random.choice('CGAT') for i in range(10000)])

import zlib
zs1 = zlib.compress(s1)
zs2 = zlib.compress(s2)
len(zs1)

print(len)