import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,10,20,25,30]
y1=[20,25,30,35,40]
plt.title("simple graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y, marker="*")
plt.plot(x,y1)
plt.show()