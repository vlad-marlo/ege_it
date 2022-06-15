# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y)
bools = [bool(i) for i in range(2)]
print('x y z w F')
bool_to_str = lambda b: str(int(b))
for x in bools:
    for y in bools:
        for z in bools:
            for w in bools:
                print(*map(bool_to_str, [x, y, z, w, (not (x and y) or (not z or w)) and ((w or x) or not y)]))
