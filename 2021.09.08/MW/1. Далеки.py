import sys

print(len(tuple(filter(lambda st: 'далек' in st,
                       list(map(lambda x:
                                x.strip().lower().replace('.', '').replace('!', '').replace('?', ''),
                                sys.stdin))))))
