import math
import numpy as np

elevation = np.zeros((3,6),dtype=float)
def calculate(Z,elevation):
    Q=0.01
    while(True):
        v = Q/(math.pi*0.75*0.75/4)
        Re = v*elevation[2]/1.31E-6
        f1 =0.001
        while(True):
            a=-2*math.log10((0.26E-3/elevation[2])/3.7+2.51/(Re*math.sqrt(f1)))
            if 1/math.sqrt(f1) - a < 1E-3:
                f=f1
                break
            f1 += 0.001
        hf = f*elevation[1]/elevation[2]*(v*v)/19.62
        if abs(abs(elevation[0] - Z)-hf) <1 :
            if elevation[0] - Z < 0 :v,Q = v*-1 , Q*-1
            return f,v,Q
            break
        Q += 0.01
# 0:Z 1:L 2:D 3:f 4:v 5:Q
elevation[0,0] , elevation[1,0] , elevation[2,0] = 120 , 100 , 80
elevation[0,1] , elevation[1,1] , elevation[2,1] = 1000 , 4000 , 2000
elevation[0,2] , elevation[1,2] , elevation[2,2] = 0.3, 0.5 , 0.4
index_z = np.argmin(elevation[:,0])
Z=elevation[index_z,0]
while(True):
    for i in range(elevation.shape[0]):
        elevation[i,3:6] = calculate(Z,elevation[i,0:3])
    print(Z,np.sum(elevation[:,5]))
    if abs(np.sum(elevation[:,5])) - 0 < 1E-2 :
        print(elevation)
        print("Qaj",elevation[0,5]," ","Qbj",elevation[1,5]," ","Qcj",elevation[2,5])
        break
    Z += 0.1