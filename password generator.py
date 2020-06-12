import numpy
p="abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*_+/*-=<>,./?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=list(p)
po=numpy.random.randint(0,len(p),8)
password=l[po[0]]+l[po[1]]+l[po[2]]+l[po[3]]+l[po[4]]+l[po[5]]+l[po[6]]
print (password)