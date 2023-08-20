def threeNumberSum(array, targetSum):
    
    array = sorted(array)
    result = []
    
    for currentIndex, current in enumerate(array):
        if currentIndex > len(array)-2: 
            break
        leftIndex = currentIndex+1
        rightIndex = len(array)-1

        while(leftIndex < rightIndex):
            sum = current+array[leftIndex]+array[rightIndex]
            if sum == targetSum:
                result.append([current, array[leftIndex], array[rightIndex]])
                leftIndex += 1

            if (sum > targetSum):
                rightIndex -= 1
            
            if (sum < targetSum):
                leftIndex += 1

    return result


a = [12, 3, 1, 2, -6, 5, -8, 6]
result = threeNumberSum(a, 0)
print(result)