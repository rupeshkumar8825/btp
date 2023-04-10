# in this i will be writing the code to solve the linear programming using python for this purpose 
# and also i will be automating the process for this purpose.
from scipy.optimize import linprog

# we have to convert the maximisation problem into a minimization problem for this purpose 
# in order to solve the LP using the python 

# do note that linprog does not allow maximization. So we have to convert it to a minimization problem for this purpose. 
# Also note that linprog() does not allow (>=). So we need to make appropriate changes again for this purpose. 




# The linear equation that we will be solving is as follows 
# maximize = z = 2x + y 
# subject to : 2y + x <= 22 , -5y + 4x <= 15, -y + 4x <= 12, -y + 4x = 16, x>=0 , y>= 0



# steps are as follows to solve the LP 
# first we have to define the objective function array 
objFunction = [-2, -1]

# defining the coefficients of LHS using the array for this purpose (inequalities) 
lhsInEqualityCoefficient = [[2, 1], [-5, 4], [-1, 4]]

# defining the coefficient of RHS for this purpose (inequalities)
rhsInEqualityCoefficient = [22, 15, 12]

# defining the array for coefficient of LHS (equalities)
lhsEqualityCoefficient = [[-1, 4]];

# defining the array for coefficient of RHS (equalities)
rhsEqualityCoefficient = [16];


# now we have to define the boundary of the decision variables 
boundary = [(0, float('inf')), (0, float('inf'))]

# do note that linprog function always takes the 0 to inf as default boundary conditions for the decision variables 

# now we will be calling the linprog function to solve this linear programming for this purpose 
optimizationValue = linprog(c = objFunction, A_ub=lhsInEqualityCoefficient, b_ub=rhsInEqualityCoefficient,  bounds=boundary, method='simplex')


# say everything went fine 
print("The optimized value for this are as follows \n\n");
print(optimizationValue)
