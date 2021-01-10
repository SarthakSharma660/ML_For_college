import random
# Q1 Import NumPy as np
import numpy as np
# 2. Create an array of 10 zeros 

arr=np.zeros(10)
print(arr)
# 3. Create an array of 10 ones 
arr2=np.ones(10)
print(arr2)
# 4. Create an array of 10 fives 
arr3=np.ones(10)*5
print(f"array of ten 5 {arr3}")
# Create an array of the integers from 10 to 50
arr4=np.arange(10,51,1)
print("array of numbers between 10 and 50{arr4}")

# 6. Create an array of all the even integers from 10 to 50 
arr5=np.arange(10,51,2)
print(f"even numbers between 10  nad 50 :\n{arr5}")        

# 7. Create a 3x3 matrix with values ranging from 0 to 8    
arr6=np.arange(0,9).reshape(3,3)   
# 8. Create a 3x3 identity matrix
arr7=np.identity(3)
print(f"identity matrix \n{arr7}")
# 9. Use NumPy to generate a random number between 0 and 1 
num=np.random.rand(1)
print(f"random number b/w 1 and 0 is\n :{num}")

# 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution 
arr8=np.random.normal(0,1,25)
print(f"array of 25 random sample \n:{arr8}")

# 12. Create an array of 20 linearly spaced points between 0 and 1: 
arr9=np.linspace(0,1,20,True,False)
print(f"20 linerarly spaced points are \n:{arr9}")