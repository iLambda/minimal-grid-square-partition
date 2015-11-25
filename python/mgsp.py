"""msgp.py

This algorithm separates a set of 2D integer-composed points and returns
a space partition only made of rectangles. This algorithm can be used to
separate complicated shapes into a bunch of rectangles."""


"""separate(M, m0):
        * M : the set of points to separate
        * m0 : a point where the algorithm will start its course

This function separates a set of point into rectangles. Given a rectangle is
represented by the cartesian product [|a;b|]*[|c;d|], then the method returns
a set of tuples formatted as ((a, b), (c, d)).
"""
def separate(M, m0):
    P = []          # The partition (now empty)
    R = set(M)      # M/union(p in P)
    m = m0          # The current point treated
    c = 0

    while len(R) > 0:                   # Is there untreated points ?
        m = next(iter(R)) if c != 0 else m  # Selecting a dot
        rB = get_rect(R, m);           # Get the rectangle that contains the point
        P.append(rB);                       # Add it to the partition

        rE = [[(i,j) for i in range(rB[0][0], rB[0][1] + 1)] for j in range(rB[1][0], rB[1][1] + 1)];
        r = sum(rE, [])                     # Build the set of points that belong to the rectangle
        R -= set(r)                         # Removing it from R
        c = c+1                             # Continue
    return P

"""get_rect(M, m0):
        * M : the set of points to separate
        * m : the point

This function returns a tuple ((a,b), (c,d)) which represents the rectangle
[|a;b|]*[|c;d|]. This rectangle is a rectangle that is included in M and
contains m.
"""
def get_rect(M, m):
    if not m in M: raise Exception('m is not in M')

    n, p = m[1] - 1, m[1] + 1
    x, y, w, h = 0, 0, 0, 0

    wI = get_width_interval(M, m);
    hI = get_height_interval(M, m);

    while (m[0], p) in M and get_width_interval(M, (m[0], p)) == wI: p = p+1
    while (m[0], n) in M and get_width_interval(M, (m[0], n)) == wI: n = n-1

    return (wI, (n+1, p-1));

"""get_width_interval(M, m):
        * M : the set of points to separate
        * m : the point

This function returns a tuple (p, n) where p (respectively n) is the number of
elements on the horizontal axis at the right (respectively left) of m.
"""
def get_width_interval(M, m):
    if not m in M: raise Exception('m is not in M')

    p, n = 1, 1
    while (m[0] + p, m[1]) in M: p = p+1
    while (m[0] - n, m[1]) in M: n = n+1
    return (m[0] - (n - 1), m[0] + (p - 1));

"""get_height_interval(M, m):
        * M : the set of points to separate
        * m : the point

This function returns a tuple (p, n) where p (respectively n) is the number of
elements on the vertical axis on the top (respectively bottom) of m.
"""
def get_height_interval(M, m):
    if not m in M: raise Exception('m is not in M')

    p, n = 1, 1
    while (m[0], m[1] + p) in M: p = p+1
    while (m[0], m[1] - n) in M: n = n+1
    return (m[1] - (n - 1), m[1] + (p - 1));
