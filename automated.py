# in this we have to automate the formation of linear programming and then use the linprog 
# function in order to solve the linear programming to give the correct answer for this purpose 

from math import comb
import numpy as np;
import math
from scipy.optimize import linprog

# defining the input format 
# the input will be for N(n, k, m : r)
n = int (input("Enter the value of n total number of data points"));
k = int(input("Enter the value of k total number of multiset requests "));
m = int(input("Enter the value of m total number of servers "));
r = int(input("Enter the value of r max multiplicity of each element"));


print("the input that i got is as follows \n\n");
print("n = ", n);
print("k = ", k);
print("m = ", m);
print("r = ", r);

# defining the function to find the matrix A 
def findMatrixA(n, k, m, r):
    # now we have to calculate the matrix A 
    A = [];
    firstRow = [];
    secondRow = [];
    i = 0;
    # using the for loop to calculate the value of hte first of the matrix A for this purpose
    while(1):
        upValue = m-r-i;
        downValue = k-i-1-r;

        if(downValue == 0 or upValue == 0):
            # then we just have to append 1 at the end and break from this while loop for this purpose 
            firstRow.append(1)
            break;

        # else we have to find the value and append it at the end of firstRow         
        currentVal = comb(m-r-i, k-i-1-r);
        firstRow.append(currentVal);
        i = i+1;


    secondRow = [1]*len(firstRow)
    A.append(firstRow)
    A.append(secondRow)

    # say everything went fine 
    return A;



# defining the function to find the value of row vector C 
def findRowVectorC(n, k, m, r):
    c = [];

    temp = k-r
    # using the for loop for this purpose 
    while(temp):
        c.append(temp)
        temp = temp-1;

    # say everything went fine 
    return c;




# defining the function to find the value of column vector b 
def findColumnVectorb(n, k, m, r):
    b = [];
    b.append(math.floor((k-1)/r)*comb(m, k-1))
    b.append(n)

    # say everything went fine 
    return b;




# defining the function to find the Atranspose for solving the dual of the original problem 
def findAtransposeMatrix(A):
    Atranspose = np.array(A).T.tolist();
    # now we also have to multiply all the elements with -1 because linprog only supports the <= 
    Atranspose = (np.array(Atranspose) * -1).tolist();

    # say everything went fine 
    return Atranspose;





# defining the function to find the value using first set of constraints 
def findUsingFirstSetOfConstraints(n, k, m, r):
    # do note that for mthe value of m < r it does not make sense because we will not be able to fetch the data items by accessing each server atmost one time we will have to access atleast one of the server for more than one time hence m < r does not make sense and we will not be entering these values in the input format 

    A = findMatrixA(n, k, m, r);

    # now we have to calculate c = (k-r, k-r-1, ...... 1)
    c = findRowVectorC(n, k, m, r);
    


    # now we have to calculate value of b 
    b = findColumnVectorb(n, k, m, r);
   
    # we have to find the transpose of A to solve its dual problem 
    Atranspose = findAtransposeMatrix(A);

    # similarly we have to multiply all the elements of c with -1 
    c = (np.array(c)*-1).tolist();


    # print("The array c is \n", c);
    print("The matrix is as follows \n\n");
    print(A);
    print("The array b is \n", b);
    print("The updated c\n", c)
    print("The transpose of A is as follows\n", Atranspose);

    


    # and now we can use the linprog function in order to solve the LP formed above using the first set of constraints for this purpose 
    # we will be filling these fields based on the dual LP that will be formed 
    objectiveFunction = b;
    lhsInEqualityCoefficient = Atranspose
    rhsInEqualityCoefficient = c 
    boundary = [(0, float('inf'))]*len(b)

    print("The final LP is as follows \n\n");
    print("The objectiveFunction = ", objectiveFunction)
    print("The lhsInEqualityCoefficient = ", lhsInEqualityCoefficient)
    print("The rhsInEqualityCoefficient = ", rhsInEqualityCoefficient)
    print("The boundary  = ", boundary);


    # now we have to use the linprog function to calculate the optimized value of the linear program for this purpose 
    optimizedValue = linprog(c = objectiveFunction, A_ub=lhsInEqualityCoefficient, b_ub=rhsInEqualityCoefficient,  bounds=boundary, method='simplex')


    # here we have to make the function and then we have to pass the parameters in the function 
    # print("The final optimized value is as follows ", k*n-optimizedValue.fun)
    # say everything went fine 
    return optimizedValue


# defining the function to append the identity matrix at the end of the A 
def appendIdentityAtEnd(A, identityMatrix):
    # using the for loop for this purpose 
    for row in identityMatrix:
        A.append(row)
    
    # say everything went fine 
    return;




# defining the function to find the optimal value using the second set of improved sets of constraints for this purpose 
def findUsingSecondSetOfConstraints(n, k, m, r):
    # first we have to find the A 
    A = findMatrixA(n, k, m, r)
    # Adas = np.array(A).tolist()

    # we have to insert the identity matrix for this purpose 
    identityMatrixLen = k-r
    identityMatrix = np.identity(identityMatrixLen, dtype=int).tolist();
    
    # now we have to append the identity matrix at the end of A 
    # calling the function for this purpose 
    appendIdentityAtEnd(A, identityMatrix);
    Adas = A;
    # Adas
    print("The identity matrix is as follows \n", identityMatrix)
    print("The new A matrix is \n", Adas)
    print("The new A matrix is \n", A)

    # say everything went fine 
    return 1;



optimizedValuesUsingFirstSetOfConstraints =  findUsingFirstSetOfConstraints(n, k, m, r)
optimizedValuesUsingSecondSetOfConstraints = findUsingSecondSetOfConstraints(n, k, m, r)
# print("The value of k*n = ", k*n);
print("The  optimized value is as follows for this purpose\n\n", optimizedValuesUsingFirstSetOfConstraints);
print("\n\n")