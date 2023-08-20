def minRewards(scores):
    numScores = len(scores)
    rewards = [1 for i in scores] # Initialize rewards to 1 for all students
    if numScores < 2:
        return rewards
    
    changes = True
    while (changes):
        changes = False
        for i in range(numScores-1):
            if (scores[i] > scores[i+1] and rewards[i] <= rewards[i+1]):
                changes = True
                rewards[i] += 1
            elif (scores[i] < scores[i+1] and rewards[i] >= rewards[i+1]):
                changes = True
                rewards[i+1] += 1
    return rewards


testScores = [8,4,2,1,3,6,7,9,5]

rewards = minRewards(testScores)
print(rewards)