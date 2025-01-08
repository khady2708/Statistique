def init_mat(rows,cols):
   return [([0]*cols) for i in range(rows)]


def mul(a,b):
   c = init_mat(len(a),len(b[0]))
   for i in range(len(a)):
       for j in range(len(b[0])):
           for k in range(len(a[0])):
               c[i][j] += a[i][k] * b[k][j]
   return c

N=100
a= init_mat(N,N)
b= init_mat(N,N)
c= mul(a,b)

print(c)