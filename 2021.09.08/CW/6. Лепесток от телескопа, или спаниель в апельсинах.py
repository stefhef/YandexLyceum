import sys


def from_word_ro_dict(word):
    return {let: word.count(let) for let in word}


def check_word(word):
    word_dict = from_word_ro_dict(line)
    for let in word_dict:
        if let in key_dict:
            if key_dict[let] >= word_dict[let]:
                continue
            else:
                return False
        else:
            return False
    return True


key_word = next(sys.stdin).strip()
key_dict = from_word_ro_dict(key_word)
result = []
for line in sys.stdin:
    line = line.strip()
    if check_word(line):
        result.append(line)

print(len(result))
print('\n'.join(result))
