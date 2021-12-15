st = input().strip().split(' -> ')
for i in range(int(input())):

    word = input()
    ind = st.index(word)
    if ind > 0:
        if ind < len(st) - 1:
            print(st[ind - 1], word, st[ind + 1], sep=' -> ')
        else:
            print(st[ind - 1], word, sep=' -> ')
    else:
        print(word, st[ind + 1], sep=' -> ')
