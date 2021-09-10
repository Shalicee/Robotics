import numpy as np
import math 

#This program computes the rotation matrices for a rotation on the X, Y, and Z axes.
def main():
    print("This program computes the rotation matrices for a rotation on the X, Y, and Z axes.")
    theta = float(input("Please enter the angle in degrees: "))
    rotX(theta)
    rotY(theta)
    rotZ(theta)

#computes the rotation matrix for a roation around the x axis
def rotX(theta):
    print("Rotation matrix around X axis:")

    Rx = np.round(np.array([[1,0,0], [0, math.cos(math.radians(theta)) , -math.sin(math.radians(theta))], [0, math.sin(math.radians(theta)), math.cos(math.radians(theta))]]),3)
    print (Rx) #prints  matrix Rz

#computes the rotation matrix for a roation around the y axis
def rotY(theta):
    print("Rotation matrix around Y axis:")
    
    Ry = np.round(np.array([[math.cos(math.radians(theta)), 0, math.sin(math.radians(theta))], [0,1,0], [-math.sin(math.radians(theta)), 0, math.cos(math.radians(theta))]]),3)
    print (Ry) #prints matrix Ry

#computes the rotation matrix for a roation around the z axis
def rotZ(theta):
    print("Rotation matrix around Z axis:")

    Rz = np.round(np.array([[math.cos(math.radians(theta)), -math.sin(math.radians(theta)), 0], [math.sin(math.radians(theta)), math.cos(math.radians(theta)), 0], [0,0,1]]),3)
    print (Rz)  #prints matrix Rz

if __name__ == "__main__":
    main()