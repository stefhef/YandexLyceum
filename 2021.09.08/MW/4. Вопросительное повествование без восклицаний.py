import sys

d = {'.': set(),
     '!': set(),
     '?': set()}

text = sys.stdin.read().strip().lower()
st = ''


def add_word(sentence: str, type='.'):
    global d, st
    sent: set = d[type]
    for word in sentence.split():
        sent.add(word)
    st = ''


for letter in text:
    if letter == '?':
        add_word(st, type='?')
    elif letter == '!':
        add_word(st, type='!')
    elif letter == '.':
        add_word(st)
    else:
        st += letter

print(' '.join(sorted(list((d['.'] & d['?']) - d['!']))))
