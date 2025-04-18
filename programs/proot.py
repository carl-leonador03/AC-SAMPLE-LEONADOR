def isPrime(x) -> bool:
    """Check if the number is a prime number"""
    return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))

def getPrimitiveRoots(q) -> dict:
    """Calculate for any primitive roots for q. Returns a dict because why not"""
    roots = {}
    temp_roots = []

    # Basically calculate all values of x for r^x mod q
    for r in range(1, q):
        for x in range(1, q):
            result = (r ** x) % q

            temp_roots.append(result)
        
        roots = roots | {r : temp_roots }
        temp_roots = []
    
    return roots

def isPrimitive(q, g) -> tuple:
    """Checks if the number (g) given is a primitive number of q. Returns a tuple."""
    primitive_roots = getPrimitiveRoots(q)
    actual_proots = []

    for root in primitive_roots:
        # If the values of r^x are all different, add to the list
        if all(primitive_roots[root].count(x) == 1 for x in primitive_roots[root]):
            actual_proots.append(root)

    if g in actual_proots:
        return True, actual_proots
    else:
        return False, actual_proots

def main(g, q):
    # g must be less than q
    if g <= q:
        raise ValueError("g must be less than q")
    
    # q must be a prime number
    if not isPrime(q):
        raise ValueError(f"{q} is not a prime number!")
    
    # Get all primitive roots of q
    proots = getPrimitiveRoots(q)

    # clean it off (remove all duplicates)
    for pr in proots:
        if any([proots[pr].count(x) > 1 for x in proots[pr]]):
            new_ = []
            for x in proots[pr]:
                if x not in new_:
                    new_.append(x)
                else:
                    break
            
            proots[pr] = new_
    
    # Check if g is a primitive root of q
    aproots = isPrimitive(q, g)

    # Print out the calculation results
    for root in proots:
        for i, r in enumerate(proots[root]):
            if i != len(proots[root]) - 1:
                print(f"{root}^{i+1} mod {q} = {r}", end=", ")
            else:
                print(f"{root}^{i+1} mod {q} = {r}", end="")
        
        if root in aproots[1]:
            print(f" ==> {root} is primitive root of {q},")
        else:
            print(",")
    
    # Print out the final result
    if aproots[0]:
        print(f"{g} is primitive root: ", aproots[0], " ", aproots[1], sep = "")
    else:
        print(f"{g} is NOT primitive root of {q} - List of Primitive roots:", aproots[1])

if __name__ == '__main__':
    q = int(input())
    g = int(input())

    try:
        main(g, q)
    except ValueError as err:
        print(str(err))
