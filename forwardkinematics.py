import numpy as np
import math 

temp = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

def main():
       
    print("This program computes the forward kinematics matrix based on the DH parameters. \n")
    
    i = int(input("Please enter the number of joints: "))
    
    for x in range (0,i):
        a = int(input("Please enter the length of link %i (a): " %(x+1)))
        alpha = float(input("\nPlease enter the alpha in degrees: "))
        d = int(input("\nPlease enter the joint offset (d): "))
        theta = float(input("\nPlease enter the theta in degrees: "))
        
        tm = transformation_matrix(a,alpha,d,theta)
        if x==0 :
            fkm = forward_kinematic(temp,tm)
        else :
            fkm = forward_kinematic(tm,fkm)
    print(np.round(fkm, 3))

def transformation_matrix(a,alpha,d,theta):
    tm = np.array([[math.cos(math.radians(theta)), -math.sin(math.radians(theta))*math.cos(math.radians(alpha)), math.sin(math.radians(alpha))*math.sin(math.radians(theta)), a*math.cos(math.radians(theta))], [math.sin(math.radians(theta)), math.cos(math.radians(alpha))*math.cos(math.radians(theta)), -math.sin(math.radians(alpha))*math.cos(math.radians(theta)), a*math.sin(math.radians(theta))], [0, math.sin(math.radians(alpha)), math.cos(math.radians(alpha)), d], [0,0,0,1]])
    return(np.round(tm,3))

def forward_kinematic(tm,tm1):
    return tm1.dot(tm)
if __name__ == "__main__":
    main()