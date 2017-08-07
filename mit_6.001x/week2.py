def oddTuples(input):
    tup = ()
    for index in range(len(input)):
        if index % 2 == 0:
            tup += input[index:index+1]
        index = index + 1
    return tup

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    largest = len(max(aDict.values()))
    for key in aDict.keys():
        if len(aDict[key]) == largest:
            return key
        
def fibonacci(n, d, s):
    if n in d:
        return d[n]

    d[n] = fibonacci(n-1, d, 'fib1') + fibonacci(n-2, d, 'fib2')
    return d[n]


assert oddTuples(('I', 'am', 'a', 'test', 'tuple')) == ('I', 'a', 'tuple')
assert oddTuples(('my', 'name', 'is', 'sumeet')) == ('my', 'is')

assert biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}) == 'b'
print(fibonacci(12, {0:0, 1:1}, ''))
