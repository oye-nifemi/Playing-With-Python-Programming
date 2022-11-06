import numpy as np

a = np.array([1,2,3,4,5])
print(a)
print(type(a))
print(a.dtype)
print(a.size) # number of elements in the array
print(a.ndim) # the dimensions of the array
print(a.shape) # the dimensions of the array in each dimension

u = np.array([1, 0])
v = np.array([0, 1])
z = u+v # vector addition
y = u-v # vector subtraction
# or np.add(u,v)
# or np.subtract(u,v)
# or np.multiply(u,v)
# or np.divide(u,v)
print(z)
print(y)

x = np.array([1,2])
z = x*2 # vector multiplication with scalar
print(z)
z = x * y # product of two numpy arrays
print(z)

a = np.array([3, 6])
b = np.array([4, 7])
z = np.dot(a, b) # dot product
print(z)

# Universal functions
a = np.array([1,2,-1,4])
z = a.mean() # calculating the mean in the array
print(z)
z = a.max()
print(z)


np.pi # the value of pi
np.sin(a) # sin value to each component of array a

np.linspace(-2,2,num=5) # np.linspace(start_value, end_value, number_of_samples)

# Get the standard deviation of numpy array
standard_deviation=a.std()

# when they have different dimensions, use np.dot(a, b)