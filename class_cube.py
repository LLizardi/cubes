import numpy as np


class cube():
     
    xb = 0.5

    R = xb
    r = xb*(np.sqrt(3)-1)/(np.sqrt(3)+1)
    directions_corners = np.array([[1.,1.,1.],[1.,-1.,1.],[-1.,1.,1.],[-1.,-1.,1.]])/np.sqrt(3)
    directions_corners = np.reshape(np.append(directions_corners,directions_corners*-1.),(8,3))
    
    corners_origin = xb*np.sqrt(3)*directions_corners.copy() 
    center_small_origin = (R+r)*directions_corners.copy()

    def __init__(self,center=[0,0,0],m=[1,1,1]):
        self.center = np.array([center])
        self.m = np.reshape(np.array([m]),(1,3))
        self.corners = self.corners_origin + self.center
        self.centers_small = self.center_small_origin + self.center

    def __str__(self):
        return str('Cube at {0} with M={1}'.format(self.center[0],self.m[0]))

    def __repr__(self):
        return str('(center,M) = ({0},{1})'.format(self.center[0],self.m[0]))

    def distance_center_origin(self):
        
        return self.distance_to_origin(self.center)[0]

    def distance_corner_origin(self):
        return max(self.distance_to_origin(self.corners))


    def set_m(self,m_new=[1,1,1]):
        self.m = np.reshape(np.array([m_new]),(1,3))

    def is_inside(self,radius=0):
        return self.distance_corner_origin()<=radius

    def move(self,vec_displ=[0,0,0]):
        self.center = np.array(self.center+vec_displ)
        self.corners = self.corners_origin + self.center
        self.centers_small = self.center_small_origin + self.center

    def are_touching(self,other):
        resta = self.center-other.center
        resta = np.sqrt(np.sum((resta*resta),axis = 1))[0]
        
        if abs(resta-1.)<=1e-8:
            return 1
        else:
            return 0
    
    def integration_clase(self,other):
        
        if abs((self.center - other.center).sum())<1e-6:
            return 0
        m1 = self.m/np.dot(self.m,self.m.T)
        
        m2 = other.m/np.dot(other.m,other.m.T)
        
        centers_small_1 = self.center_small_origin + self.center
        centers_small_2 = self.center_small_origin + other.center
        
        M_Energies = (self.R**6)*self.dipolar(self.center,other.center,m1,m2)#big-big
        M_Energies += 2*(self.r**3)*(self.R**3)*self.dipolar(self.center,centers_small_2,m1,m2)#big-small
        M_Energies += (self.r**6)*self.dipolar(centers_small_1,centers_small_2,m1,m2)#small-small
            
            
        return M_Energies 

    
    @staticmethod
    def dipolar(D1,D2,m1,m2):
        energy = 0.
        for d1 in D1:

            for d2 in D2:
                rv = d2-d1
                r = np.sqrt(np.dot(rv,rv.T))
                r3 = r*r*r
                r5 = r3*r*r
                energy +=  np.dot(m1,m2.T)/r3-3*np.dot(m1,rv)*np.dot(m2,rv)/r5
       
        return energy.sum()

    
    @staticmethod
    def distance_to_origin(array):
        return np.sqrt(np.sum(array*array,axis=1))

