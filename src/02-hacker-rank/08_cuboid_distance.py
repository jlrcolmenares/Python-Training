# You are given three integers X,Y,Z representing the dimensions of a cuboid 
# along with an integer N. You have to print a list of all possible 
# coordinates given (i,j,k) on a 3D grid where the sum of i+j+k != N
# with 0<i<X, 0<j<Y, 0<k<Z

if __name__ == "__main__":
    x = int(input('Introduce X dimension of cuboid: '))
    y = int(input('Introduce Y dimension of cuboid: '))
    z = int(input('Introduce Z dimension of cuboid: '))
    n = int(input('Introduce N integer: '))
    
    # The shortest solution
    array = [ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
    print(array)

    # The understandable version
    # coord_x = range(0,x+1)
    # coord_y = range(0,y+1)
    # coord_z = range(0,z+1)
    # array = []

    # for i in coord_x:
    #     for j in coord_y:
    #         for k in coord_z:
    #             if i+j+k != n:
    #                 array.append([i,j,k])
    #                 print('x:{:2d} - y:{:2d} - z:{:2d}'.format(i,j,k))
    
    # print(array)
    # Esto nos da la solución de una manera poco elegante



 
