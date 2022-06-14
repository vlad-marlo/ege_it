# ((x ∧ ¬y) → (¬z ∨ ¬w)) ∧ ((w → x) ∨ y)
bools = [bool(i) for i in range(2)]
reworked = lambda x: str(int(x))
answer = lambda x, y, z, w: (not (x or not y) or not (z and w))
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                print(
                    ' | '.join(
                        list(map(reworked, [
                                x,
                                y,
                                z,
                                w,
                                ((not (x and not y) or (not z or not w)) and ((not w or x) or y))
                            ]
                            )
                        )))

