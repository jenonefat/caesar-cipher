def get_permutations(string):
    '''

    string (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    Returns: a list of all permutations of the given string

    Example:
    string input: 'abc'
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    '''
    # converting string into all lowercase
    s = string.lower()
    result = []
    # base case: string with one letter only has one possible permutation
    if len(s) == 1:
        return s

    # iterating over letters in string & associated index
    for i, char in enumerate(s):
        # indexing to isolate the other letters in the string
        other_chars = s[:i] + s[i+1:]
        # make continuous recursive calls until base case is met
        permutations_remaining = get_permutations(other_chars)
        # once base case is satisfied, flow passes back to previous scope & adds char to permutation
        # until char from original recursive call is added to the permutation
        for perm in permutations_remaining:
            result.append(char + perm)

    return result



# if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

        # example_input = 'cut'
        # print(f'Input: {example_input}')
        # print(f'Expected Output: [cut,ctu,tcu,tuc,uct, utc] ')
        # print(f'Actual Output: {get_permutations(example_input)}')



