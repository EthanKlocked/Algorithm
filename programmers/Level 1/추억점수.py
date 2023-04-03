def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    return [sum(dictionary.get(char, 0) for char in i) for i in photo]
