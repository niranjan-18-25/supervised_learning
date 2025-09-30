import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])
array2 = array1[array1 % 2 == 0]
print(array2)

array3 = np.arange(0,101,10)
print(array3)

array4 = np.linspace(0,1,5)
print(array4)

array6 = np.array([1,2,45,46,88,9,-12,32,-53,7,5,6,88,54,6,77,6,467,78,577,78,68])
print('MAX : ',np.max(array6))
print('MIN : ',np.min(array6))
print('SUM : ',np.sum(array6))
print('MEAN : ',np.mean(array6))
print('Squar roots : ',np.sqrt(array6))
print('Standard deviation : ',np.std(array6))
