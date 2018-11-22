import matplotlib.pyplot as plt

f=open(r"C:\Users\Admin\PycharmProjects\Matlib\venv\Countries","r")
cntr=f.readlines()

f.close()
f=open(r"C:\Users\Admin\PycharmProjects\Matlib\NPW","r")
npw=f.readlines()
for i in range(13):
    npw[i]=int(npw[i])
f.close()
f=open(r"C:\Users\Admin\PycharmProjects\Matlib\GDP","r")
gdp=f.readlines()
for i in range(13):
    gdp[i]=int(gdp[i])
f.close()
f=open(r"C:\Users\Admin\PycharmProjects\Matlib\Population","r")
ppl=f.readlines()
for i in range(13):
    ppl[i]=int(ppl[i]) 
f.close()

plt.plot(cntr,npw)

plt.show()
plt.scatter(npw,gdp)
plt.show()
plt.scatter(npw,ppl)
plt.show()