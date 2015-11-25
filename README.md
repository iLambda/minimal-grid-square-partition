# minimal-grid-square-partition
An algorithm that separates a set of 2D points with integer coordinates and returns a partition of this set composed only with rectangles.
Big thanks to [devspaceship](https://github.com/devspaceship "devspaceship")'s idea for an iterative implementation of this algorithm.

##Python

To use, add mgsp.py to your project, and just type at the beggining of your script :  
```python
import mgsp
```

###mgsp.separate(M, m0):
- M : the set of points to separate
- m0 : a point where the algorithm will start its course

This function separates a set of point into rectangles. Given a rectangle is
represented by the cartesian product [|a;b|]x[|c;d|], then the method returns
a set of tuples formatted as ((a, b), (c, d)).

####mgsp.get_rect(M, m0):
- M : the set of points to separate
- m : the point

This function returns a tuple ((a,b), (c,d)) which represents the rectangle
[|a;b|]x[|c;d|]. This rectangle is a rectangle that is included in M and
contains m.

####mgsp.get_width_interval(M, m):
- M : the set of points to separate
- m : the point

This function returns a tuple (p, n) where p (respectively n) is the number of
elements on the horizontal axis at the right (respectively left) of m.

####mgsp.get_height_interval(M, m):
- M : the set of points to separate
- m : the point

This function returns a tuple (p, n) where p (respectively n) is the number of
elements on the vertical axis on the top (respectively bottom) of m.
