from math import pi, atan, log, sqrt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime as dt
import sys
from itertools import combinations,permutations
from class_cube import cube


def create_mesh(N):
    cubes = []
    if N<=1:
        cubes.append(cube())
        return cubes
    N = (N-1)/2
    for x in np.arange(-N,N + 0.1,1):
        
        for y in np.arange(-N,N + 0.1,1):
            
            for z in np.arange(-N,N + 0.1,1):
                
                cubes.append(cube([x,y,z]))
    
    
    return cubes


def main(N_min,N_max):
    print('{0} {1} {2} {3} {4} {5}'.format('Radius','Total_Energy','Energy_per_Particle','Number_of_Particle','Faces_Touching','Energy_of_central_cube'))
     
    xb = 0.5
    lista = range(N_min,N_max)
    lista3 = [i**3 for i in range(N_min,N_max)]

    cc = 0
    for N in lista3:    
        
        cubes = create_mesh(lista[cc])
        
        indexs2 = combinations(np.arange(N,dtype=np.int),2)
        
        
        
        faces = np.sum(np.array([cubes[i].are_touching(cubes[j]) for i,j in indexs2]))
        energy = 0. 
        energy_norm = 0.
        radii = [i.distance_corner_origin() for i in cubes]
        central_energy = 0.
        print('{0:.5f} {1:.5f} {2:.5f} {3:3.0f} {4:3.0f} {5:.5f}'.format(max(radii),energy,energy_norm,N,faces,central_energy))
        cc += 1

    return True



 
if __name__ == "__main__":
    inicio = dt.now() 
     
    #†his calculation considered the origin in the center of a cube
    main(1,30)
    fin = dt.now()
    print('Elapsed Time: ',fin-inicio)


