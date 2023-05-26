# Plot different Probability density functions

import numpy as np
import matplotlib.pyplot as plt


# Uniform Distribution
a=3
b=8
x = np.linspace(a,b,10)
y = x*0 + 1/(b-a)
plt.plot(x,y)
plt.title('Uniform Distribution')
plt.show()

plt.close()



# Normal/Gaussian Distribution

def normal(x,m,std):
    return 1/((2*np.pi*std*std)**0.5)*np.exp(-((x-m)**2)/(2*(std**2)))

m1=25; std1=4
m2=25; std2=10
m3=15; std3=4
x = np.linspace(1,50,1000)

y1 = normal(x,m1,std1)
y2 = normal(x,m2,std2)
y3 = normal(x,m3,std3)

plt.plot(x,y1, label='mean=25 std=4')
plt.plot(x,y2, label='mean=25 std=10')
plt.plot(x,y3, label='mean=15 std=4')
plt.legend()
plt.title('Normal Distribution')
plt.show()

plt.close()



# Binomial Distribution

def binomial(x,n,p):
    return [np.math.comb(n,x)*(p**x)*((1-p)**(n-x)) for x in x]

n=100
p1=0.2; p2=0.5; p3=0.8
x = np.arange(n+1)

y1 = binomial(x,n,p1)
y2 = binomial(x,n,p2)
y3 = binomial(x,n,p3)

plt.plot(x,y1, label='p=0.2')
plt.plot(x,y2, label='p=0.5')
plt.plot(x,y3, label='p=0.8')
plt.legend()
plt.title('Binomial Distribution')
plt.show()

plt.close()



# Exponential Distribution

def exponential(x,lmda):
    return lmda*np.exp(-lmda*x)

lmda1=0.5; lmda2=1; lmda3=1.5
x = np.arange(5,step=0.01)

y1 = exponential(x,lmda1)
y2 = exponential(x,lmda2)
y3 = exponential(x,lmda3)


plt.plot(x,y1, label='lmda=0.5')
plt.plot(x,y2, label='lmda=1')
plt.plot(x,y3, label='lmda=1.5')
plt.legend()
plt.title('Exponential Distribution')
plt.show()
