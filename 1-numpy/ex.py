import numpy as np

def main():
    # array with 10 zeros
    arr_10 = np.zeros(10)
    print(arr_10)
    # array with 10 zeros
    arr_1_10 = np.ones(10)
    print(arr_1_10)
    # array from 10 to 50
    a = np.arange(10, 51)
    print(a)
    # array from 10 to 50 evens
    a = np.arange(10, 51, 2)
    print(a)
    # matrix (3,3) 0-8
    a = np.arange(9).reshape(3, 3)
    print(a)
    # identity
    a = np.eye(3)
    print(a)
    # normal distribution
    a = np.random.randn(25)
    print(a)
    # mat
    a = np.linspace(0, 1, 100)
    print(np.round(a, 3))
    
    # mat
    mat = np.arange(1,26).reshape(5,5)
    print(mat[2:, 1:])
    print(mat[3,-1])
    print(mat[:3, 1])
    print(mat[-1])
    print(mat[3:])
    
    # stats
    print(mat.sum())
    print(mat.std())
    print(mat.sum(axis=0))
    print('**' * 10)
    print(mat)
    print(mat.max(axis=1))

if __name__=='__main__':
    main()