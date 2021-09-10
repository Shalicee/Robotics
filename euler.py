#This program computes the two combinations of rotations for Euler Angle rotation and Roll-Pitch-Yaw rotation.

import numpy as np
import math 

def main():
    print ("This program computes the two combinations of rotations for Euler Angle rotation and Roll-Pitch-Yaw rotation.")
    print ("Please enter the angles in degrees: ")
    theta1 = float(input("Theta1: ")) #holds the value of theta1
    theta2 = float(input("Theta2: ")) #holds the value of theta2
    theta3 = float(input("Theta3: ")) #holds the value of theta3
    
    euler(theta1, theta2, theta3) #makes a call to the euler function 
    RPY(theta1, theta2, theta3)   #makes a call to the rpy function 

#computes the rotational matrix for euler angle rotation 
def euler(theta1, theta2, theta3):
    Rx = rotZ(theta1)   #calls the function to rotate around the z axis using theta1
    Ry = rotY(theta2)   #calls the function to rotate around the y axis using theta2
    Rz = rotZ(theta3)   #calls the function to rotate around the z axis using theta3
    euler = np.round(Rx.dot(Ry.dot(Rz)),3)  #computes the dot product ZYZ
    print ("Euler: ")
    print (euler)
#computes the roatational matrix for rpy rotaion 
def RPY(theta1, theta2, theta3):
    Rx = rotX(theta3)   #calls the function to rotate around the x axis using theta3
    Ry = rotY(theta2)   #calls the function to rotate around the y axis using theta2
    Rz = rotZ(theta1)   #calls the function to rotate around the z axis using theta1
    RPY = np.round(Rz.dot(Ry.dot(Rx)),3) #computes the dot product ZYX
    print ("RPY: ")
    print (RPY)

#computes the rotaion matrix for a rotation around the x axis 
def rotX(theta):

    Rx = np.round(np.array([[1,0,0], [0, math.cos(math.radians(theta)) , -math.sin(math.radians(theta))], [0, math.sin(math.radians(theta)), math.cos(math.radians(theta))]]),3)
    return (Rx) #returns the matrix Rx
#computes the rotaion matrix for a rotaion around the y axis 
def rotY(theta):
    
    Ry = np.round(np.array([[math.cos(math.radians(theta)), 0, math.sin(math.radians(theta))], [0,1,0], [-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]]),3)
    return (Ry) #returns matrix Ry
#computes the rotation matrix for a roation around the z axis
def rotZ(theta):

    Rz = np.round(np.array([[math.cos(math.radians(theta)), -math.sin(math.radians(theta)), 0], [math.sin(math.radians(theta)), math.cos(math.radians(theta)), 0], [0,0,1]]),3)
    return (Rz) #returns matrix Rz



if __name__ == "__main__":
    main()