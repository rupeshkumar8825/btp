# in this we have to automate the formation of linear programming and then use the linprog 
# function in order to solve the linear programming to give the correct answer for this purpose 

from math import comb
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

# do note that for mthe value of m < r it does not make sense because we will not be able to fetch the data items by accessing each server atmost one time we will have to access atleast one of the server for more than one time hence m < r does not make sense and we will not be entering these values in the input format 

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



print("The matrix is as follows \n\n");
print(A);

# now we have to calculate the linear program based on the 