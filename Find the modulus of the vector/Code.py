def det(m):
    return m[0][0]*m[1][1]*m[2][2]+m[0][1]*m[1][2]*m[2][0]+m[1][0]*m[0][2]*m[2][1]- \
           (m[2][0]*m[1][1]*m[0][2]+m[0][1]*m[1][0]*m[2][2]+m[0][0]*m[1][2]*m[2][1])
 
a = [[0.34, 0.71, 0.63], [0.71, -0.65, -0.18], [1.17, -2.35, 0.75]]
m1 = [[2.08, 0.71, 0.63], [0.17, -0.65, -0.18], [1.28, -2.35, 0.75]]
m2 = [[0.34, 2.08, 0.63], [0.71, 0.17, -0.18], [1.17, 1.28, 0.75]]
m3 = [[0.34, 0.71, 2.08], [0.71, -0.65, 0.17], [1.17, -2.35, 1.28]]
 
x = [0, 0, 0]
y = []
 
d0 = det(a)
 
d1 = det(m1)
x[0] = d1/d0
y.append(2*x[0]-3)
d2 = det(m2)
x[1] = d2/d0
y.append(2*x[1]-3)
d3 = det(m3)
x[2] = d3/d0
y.append(2*x[2]-3)
print('x =', x)
print('y = |2X-3| =', y)
 
print((y[0]**2+y[1]**2+y[2]**2)**0.5)