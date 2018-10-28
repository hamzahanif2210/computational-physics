import matplotlib.pyplot as plt 

t=[1,3,4,7,8,10]
P = [2.1,4.6,5.4,6.1,6.4,6.6]
V = [6.1,5.8,5.5,5.0,4.9,2.3]

plt.plot(t,P , label = 'Graph of P')
plt.plot(t,V, label = 'Graph of V')
plt.title('Two graphs in one ')
plt.xlim(0,12)
plt.ylim(1,7.3)
plt.xlabel('t')
plt.ylabel('P and V')
plt.legend(loc='best')
plt.grid(True)
plt.show()