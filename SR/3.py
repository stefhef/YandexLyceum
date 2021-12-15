def depart(*args, func):
    if not args:
        raise AttributeError('No arguments')
    for num in args:

        if not str(num).isdigit():
            raise TypeError('Not only integer')
        if len(str(num)) > 2:
            raise TooLargeError('Too large numbers')

    return sorted(set(filter(func, args)))


class TooLargeError(BaseException):
    pass
