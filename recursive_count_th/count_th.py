'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        #Can't have a th if there is 1 or 0 characters
        return 0
    elif word[0:2] == 'th':
        return count_th(word[1:] ) + 1
    else:
        return count_th(word[1:])
