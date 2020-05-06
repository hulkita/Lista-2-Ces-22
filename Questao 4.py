
def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def share_diagonal(x0, y0, x1, y1):
       """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
       dy = abs(y1 - y0)  # Calc the absolute y distance
       dx = abs(x1 - x0)  # CXalc the absolute x distance
       return dx == dy  # They clash if dx == dy

def main():
    import random
    import time
    rng = random.Random()   # Instantiate a generator
    sizes = [35]
    for size in sizes:


        bd = list(range(size))     # Generate the initial permutation
        num_found = 0
        tries = 0
        tentativas = []
        tempos = []
        start = time.time()
        while num_found < 10:
            rng.shuffle(bd)
            tries += 1
            if not has_clashes(bd):
                tentativas.append(tries)
                tries = 0
                num_found += 1

        end = time.time()
        total_time = end - start
        media_tries = sum(tentativas) / len(tentativas)
        print("Found '{2} queens' solution {0} in \n{1} tries and {3} seconds average.".format(bd, media_tries, size,
                                                                                            total_time / 10))
main()





