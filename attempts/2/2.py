#  (¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w.
convert = lambda x: str(int(x))
bools = [bool(i) for i in range(2)]
print('x y z w F')
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                print(*map(convert, [
                    x,
                    y,
                    z,
                    w,
                    (not x and not y) or (y == z) or not w
                ]))
