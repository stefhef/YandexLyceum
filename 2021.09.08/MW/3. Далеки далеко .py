import sys

dct = ['далек', 'далека', 'далеку',
       'далеков', 'далеки', 'далекам', 'далеками', 'далеком', 'далеке', 'далеках']
print(len(tuple(filter(lambda x: x is True, list(map(lambda x: any(list(filter(
    lambda st: st in dct,
    x.strip().lower().replace('.', '').replace('!', '').replace('?', '').split()))), sys.stdin))))))
