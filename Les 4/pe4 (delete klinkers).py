def delete_klinkers(woord):
    'return the given word without vowels'
    result = ''
    for char in woord:
        if char not in 'aeiou':             # aeiou are the vowels
            result = result + char
    return result

print('The result is:' + ' ' + delete_klinkers('vis'))

help(delete_klinkers)