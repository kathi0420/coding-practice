
print("hello")

def spiralTraverse(array):
    # Write your code here.
    import math
    spiral_output = []
    if (array == None):
        return spiral_output
    
    num_rows = len(array)
    num_cols = len(array[0])
    min_dim = min(num_rows, num_cols)

    if (num_rows == 1):
        for col in range(num_cols):
            spiral_output.append(array[0][col])
        return spiral_output
    
    if (num_cols == 1):
        for row in range(num_rows):
            spiral_output.append(array[row][0])
        return spiral_output

    for depth in range(math.ceil(min_dim/2)):
        r1 = depth
        r2 = num_rows - depth
        c1 = depth
        c2 = num_cols - depth

        for col in range(c1, c2):
            spiral_output.append(array[r1][col])

        for row in range(r1+1, r2):
            spiral_output.append(array[row][c2-1])
        
        for col in range(c2-2, c1-1, -1):
            if ((r2-1) != r1):
                spiral_output.append(array[r2-1][col])
        
        for row in range(r2-2, r1, -1):
            if (c2-1) != c1:
                spiral_output.append(array[row][c1])

    return spiral_output


test1 = [[3, 2], [5, 3]]

array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

def spiral(arr):
    spiral_output = []

    while (arr):
        spiral_output += arr.pop(0)
        arr = list(zip(*arr))[::-1]
    
    return spiral_output



out = spiral(array)
print (out)