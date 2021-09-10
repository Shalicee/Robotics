#This program generates random matricies of varying sizes every time it runs it returns the calculations of various matrix operations
# this program uses matricies of up to sixe 10*10

#import the needed packages
import numpy as np
import random

#begins the main funtion
def main() :

    print("This program generates random matricies every time it is ran it returns the calculations of various matrix operations")
    
    c= random.randint(1,10) #holds the value of the number of columns
    r= random.randint(1,10) #holds the value of the number of rows
    
    #Creates 8 different random matricies using the row and column variables
    A= np.random.randint(10, size = (r,c))
    B= np.random.randint(10, size = (c,r))
    C= np.random.randint(10, size = (r,c))
    D= np.random.randint(10, size = (c,r))
    E= np.random.randint(10, size = (r,c))    
    F= np.random.randint(10, size = (c,r))
    G= np.random.randint(10, size = (r,c))
    H= np.random.randint(10, size = (c,c))

    # creates 4 vectors 
    p= np.random.randint(10, size = c)
    q= np.random.randint(10, size = r)
    p1= np.random.randint(10, size = 3)
    p2= np.random.randint(10, size = 3)
    
    #makes a call to each function every time the program executes
    AB(A,B)
    Ap(A,p)
    transposeAp(A,q) 
    inverseAp(H,p)
    p1xp2(p1, p2)
    transposep1p2(p1, p2)
    A7(A,B,C,D,E,F,G)



#this function multiplies the elements of two matricies A and B
def AB(A,B) :
    #print the original matix and vector
    print("AB: \n")
    print(A, "*")
    print(B)
    
    try :
        print("Output: ")
        print (A.dot(B)) #calculates and prints the dot product of A and B
    except ValueError:  # multiplies the matrixes
        print("Incompatible dimensions! In order to multiply two matricies, the number of columns in the first matrix must be equal to the number of rows in the second.")
    
         
#this function multiplies a matrix A with a vector p
def Ap(A,p) :
    #print the original matrix and vector
    print("Ap: \n")
    print(A, "*")
    print(p)

    try :
        print("Output: ")
        print (A.dot(p)) #calculates and prints the dot product of A and p
    except ValueError: #throws an exception if the dimension values are incompatible
        print("Incompatible dimensions! In order to find the product, the number of elements in vector p must be equal to the number of columns in matrix A.")
        
#this function calculates the product of the transpose of a matrix and a vector
def transposeAp(A,p) :
    print("Transpose(A)p: \n")
    print(A, "T  *")
    print(p)

    try :
        print("Output: ")      
        print ((np.transpose(A)).dot(p)) #returns the product of the transpose of A and the vector p
    except ValueError:
        print("Incompatible dimensions! In order to find the product of the transpose of A and p, the number of elements in vector p must be equal to the number of rows in matrix A.")
        
    

#this function calculates the product of the inverse of a matrix and a vector
def inverseAp(A,p) :
    print("InverseA(p): \n")
    print(A, "^-1  *")
    print(p)
    
    try :
        print("Output: ")
        print (np.linalg.inv(A).dot(p))
    except ValueError:
        print("Incompatible dimensions! ")
        
#this function calculates the cross product of two vectors
def p1xp2(p1, p2) :
    
    #prints the original vectors
    print("p1Xp2: \n")
    print(p1)
    print("X")
    print(p2)

    try :
        print ("Output: ")
        print (np.cross(p1,p2)) #calculates the cross product
    except ValueError: #throws an exception if the dimensions are incompatible 
        print("Incompatimle dimensions")

#calculates the product of the transpose of p1 and p2
def transposep1p2(p1, p2) :
    
    #prints the original matrix and vector
    print("transpose(p1)p2: \n")
    print(p1)
    print("T  *")
    print(p2)

    try:
        print("Output: ")
        print ((np.transpose(p1)).dot(p2)) #calculates and prints the product of the transpose of p1 and p2
    except ValueError: #throws an exception if the values do nao match
        print("Incompatible Dimensions")

#this function calculates and prints the product of 7 matricies
def A7(A,B,C,D,E,F,G) :
    print("A1A2A3A4A5A6A7: \n")
    #print each matrix
    print(A, "*")
    print(B, "*")
    print(C, "*")
    print(D, "*")
    print(E, "*")
    print(F, "*")
    print(G)

    try:   
       print ("Output: ")
       print (A.dot(B.dot(C.dot(D.dot(E.dot(F.dot(G))))))) #computes the dot product of 7 matricies
    except ValueError: #throws an exception if the valuse are incompatible 
        print("Incompatible dimensions.")
if __name__ == "__main__":
    main()