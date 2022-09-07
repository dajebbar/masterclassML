import numpy as np


def main():
    np.random.seed(42)
    arr = np.random.randint(-10, 10, size=10)
    # print(arr)
    # print(arr + 5)
    # print(arr ** 2)
    # print(arr.sum())
    # print(arr.mean())
    # print(arr.std())
    arr2d = np.random.randint(-100, 50, size=(5, 5))
    # print(arr2d)
    # sum of rows
    # print(arr2d.sum(axis=0))
    # sum of cols
    # print(arr2d.sum(axis=1))
    # create a new arr from other arrs
    vec = np.arange(3)
    mat = np.arange(6).reshape(3, 2)
    print(vec)
    print(mat)
    # using concatenate
    a = np.concatenate([vec, vec])
    print()
    print(a)
    # using hstack
    b = np.hstack([vec, vec])
    print(b)
    #  hstack for 2 dim
    c = np.hstack([mat, mat])
    print(c)
    # in 2 dim concatenate works different
    # than hstack
    d = np.concatenate([mat, mat])
    print(d)
    
    # combining vect to mat with column_stack
    e = np.column_stack([vec, mat])
    print(e)
    
    # apply to two vec
    f = np.column_stack([vec, vec])
    print(f)
    
    # vstack for combining vertically
    a = np.vstack([vec, vec])
    print(a)
    
    print()
    print(mat)
    b = np.vstack([mat, mat])
    print(b)
    
    # slicing and filtering
    mat = np.arange(15).reshape(5, 3)
    print(mat)
    print(mat[:, 0])
    print()
    print(mat[[3, 0, 1]])
    
    cond = (mat % 2 == 1)
    print(mat[cond])
    

if __name__=='__main__':
    main()