LETTERS = ''.join(map(chr, range(ord('A'), ord('Z') + 1)))
with open('words.txt', 'w') as fp:
    for a in LETTERS:
        for b in LETTERS:
            for c in LETTERS:
                for d in LETTERS:
                    for e in LETTERS:
                        fp.write(a + b + c + d + e + '\n')