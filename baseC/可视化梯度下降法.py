def target_function(x):
    return (4*x**2)

import matplotlib.pyplot as plt


x = [i for i in range(100)]
# 1 2 3 4 5
#-5 -4 -3 -2 -1
x2 = [-i for i in x[::-1]]
del x2[99]
x3 = x2+x

print(x3)
y = [target_function(j) for j in x3]
print(y)
def length(x):
    return (x**2)**(1/2)

def secant(f,x0,dx = 0.001):
    return   (f(x0+dx)-f(x0)) / dx
i = 0
x0=-78
xs = [x0]
ys = [target_function(x0)]
grids = []
l = 0.023
grid = secant(f=target_function,x0=x0)
print(grid)
while length(grid)>0.00001 and i<200:
    i=i+1
    grid = secant(f=target_function,x0=x0)
    if length(grid) < 0.001:
        l = 0.093
    nextx0= x0-grid*l
    nexty0 = target_function(nextx0)
    xs.append(nextx0)
    ys.append(nexty0)
    grids.append(grid)
    x0 = nextx0

print("{}ii".format(i))
print(xs[70:100])
print(ys[70:100])
print(grids[70:100])
    


# plt.plot(x3,y)
# plt.scatter(xs,ys)
# plt.show()