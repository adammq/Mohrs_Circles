import numpy as np
from numpy import pi as pi
from numpy import cos as cos
from numpy import sin as sin
from numpy import linalg
from matplotlib import pyplot as plt

#inputs
units = input('units: ')

sigX = float(input("sigma-x: "))
sigY = float(input("sigma-y: "))
sigZ = float(input("sigma-z: "))

tauXY = float(input("tau-xy: "))
tauXZ = float(input("tau-xz: "))
tauYZ = float(input("tau-yz: "))

#calculate principal normal stresses and absolute maximum shear stress
Cauchy = np.matrix([[sigX,tauXY,tauXZ],[tauXY,sigY,tauYZ],[tauXZ,tauYZ,sigZ]]);

sig_prncpl = linalg.eigvals(Cauchy)
sig_prncpl = sorted(sig_prncpl,reverse=True)
tau_abs = (sig_prncpl[0]-sig_prncpl[2])/2

#print value outputs
print("\nPrincipal normal stresses:\n" +
	str(round(sig_prncpl[0],2)) + units + "\n" +
	str(round(sig_prncpl[1],2)) + units + "\n" +
	str(round(sig_prncpl[2],2)) + units + "\n")
print("Absolute maximum shear stress:\n" +
	str(round(tau_abs,2))  + units + "\n")

#calculations for plot of Mohr's circle
#radius of circle, corresponding to maximum in-plane shear stresses
R = [abs(sig_prncpl[0] - sig_prncpl[2])/2, 
	 abs(sig_prncpl[0] - sig_prncpl[1])/2, 
	 abs(sig_prncpl[1] - sig_prncpl[2])/2]

#center of circle, corresponding to average in-plane normal stresses
sig_avg = [(sig_prncpl[0] + sig_prncpl[2])/2, 
	 	   (sig_prncpl[0] + sig_prncpl[1])/2, 
	 	   (sig_prncpl[1] + sig_prncpl[2])/2]

#initialize theta
theta = np.linspace(0,2*pi,256)

#create plot
plt.figure(figsize=(10,10),dpi=80)
plt.subplot(1,1,1)

#plot each Mohr's cricle
for i in range(0,len(R)):
	X = R[i]*cos(theta)+sig_avg[i]
	Y = R[i]*sin(theta)
	plt.plot(X,Y,color="blue")

#notable points on graph
#absolute maximum shear stress
plt.plot(sig_avg[0],R[0],marker='o',markersize=6,color="black",
	label="Absolute maximum shear stress\n" + "(" + str(round(R[0],2)) + units + ")")
#principal normal stresses
#maximum
plt.plot(sig_prncpl[0],0,marker='o',markersize=6,color="black",
	label="Principal normal stresses\n" + "(" + str(round(sig_prncpl[0],2)) + units +
	", " + str(round(sig_prncpl[1],2)) + units + ", " + str(round(sig_prncpl[2],2)) +
	units + ")")
#intermediate
plt.plot(sig_prncpl[1],0,marker='o',markersize=6,color="black")
#minimum
plt.plot(sig_prncpl[2],0,marker='o',markersize=6,color="black")
plt.grid(True)

#format axes and grid
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',(sig_prncpl[0]+sig_prncpl[2])/2))
plt.gca().invert_yaxis()
plt.title("Mohr's Circles")
plt.legend(loc='upper left')
plt.show()