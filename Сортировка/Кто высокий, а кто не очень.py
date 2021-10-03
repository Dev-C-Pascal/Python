
F, D = map(int, input().split())
a=D*25.4
b=F*12*25.4
c=(a+b)/1000
print(F,"'",D,'"'" = ",float('{:.2f}'.format(c)),"m.",sep='')
