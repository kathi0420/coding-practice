def commonCharacters(strings):
    # Write your code here.
    result = []
    charCounts = {}
    numStrings = len(strings)
    for string in strings:
        currentSet = set()
        for char in string:
            if not (char in currentSet):
                charCounts[char] = charCounts.get(char, 0) +1
                currentSet.add(char)
    
    for char, count in charCounts.items():
        if count == numStrings:
            result.append(char)
    
    return result


def commonCharacters2(strings):
    return set.intersection([{c for c in string} for string in strings])