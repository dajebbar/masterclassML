import numpy as np


'''
    Index et sélection:
        - Saisir un seul élément
        - Saisir une tranche d'éléments
        - Broadcast de sélections
        - Indexation et sélection en 2-dimensions
        - Sélection conditionnelle
'''
def main():
    arr = np.arange(11)
    # Saisir un seul élément
    print(arr[5])
    # Saisir une tranche d'éléments
    print(arr[:3])
    print(arr[7:-1])
    # Broadcast de sélections
    arr[:3] = -100
    print(arr) # -100 was broadcasted into arr (like diffusion)
    slice_of_arr = arr.copy()[:5] # like a reference if not copy
    print(slice_of_arr)
    slice_of_arr[:] = 0
    print(slice_of_arr)
    print(arr)
    # Indexation et sélection en 2-dimensions
    np.random.seed(42)
    arr_2d = np.random.randint(2, 50, size=(3, 3))
    print(arr_2d)
    print(arr_2d[1, 1])
    print(arr_2d[:, -1])
    print(arr_2d[:-1, 1:])
    # Sélection conditionnelle
    arr = np.random.randn(5, 5) * 10
    print(arr)
    cond = (0 < arr)  & (arr < 7)
    print()
    print(np.sort(arr[cond]))
    cond = arr < 0
    print(np.sum(arr[cond]))

if __name__=='__main__':
    main()