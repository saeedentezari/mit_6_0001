# Problem Set 4A
# Creator: Saeed Entezari

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string recursively.

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence
    
    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    result = []
    # base case
    if len(sequence) == 1:
        return [sequence]
    # recursive case
    else:
        for i in range(len(sequence)):
            result += [sequence[i] + per for per in get_permutations(sequence[:i]+sequence[i+1:])]
        return result

if __name__ == '__main__':
    
    print(get_permutations('abc'))