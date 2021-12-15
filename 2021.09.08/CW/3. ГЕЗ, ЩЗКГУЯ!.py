negative = False
st, shift = input().strip(), int(input())
if shift < 0:
    shift = -shift
    negative = True
shift %= len(st)
if negative:
    shift = -shift

print(st[shift:] + st[:shift], st, st[-shift:] + st[:-shift], sep='\n')
