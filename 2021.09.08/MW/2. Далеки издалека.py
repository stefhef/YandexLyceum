import sys

print(len(tuple(filter(lambda x: x is True, list(map(lambda x: any(list(filter(
    lambda st: st.startswith('далек'),
    x.strip().lower().replace('.', '').replace('!', '').replace('?', '').split()))), sys.stdin))))))
