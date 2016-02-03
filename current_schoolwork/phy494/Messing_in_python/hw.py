import numpy as np
z = np.array([ [ 0.0 , 0.0 , 0.0 ] , [ 1.34234 , 1.34234 , 0.0 ],
              [ 1.34234 , 0.0 , 1.34234 ] , [ 0.0 , 1.34234 , 1.34234 ] ])
x = np.array([1.34234,-1.34234,-1.34234])
positions2 = ([[1.5, -1.5, 3], [-1.5, -1.5, -3]])
t_ = np.array([-1.5, 1.5, 3])

def translate(coordinates = positions2,t = t_):
    l2 = 0
    l1,l2 = np.shape(coordinates)

    for i in range(0,l1):

        for n in range(0,l2):


            coordinates[i][n] = coordinates[i][n] + t[n]
    return coordinates
