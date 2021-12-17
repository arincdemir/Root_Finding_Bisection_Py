# Root_Finding_Bisection_Py
My implementation of the bisection root finding algorithm in python

The function has default values x = -10^6 x = 10^6 as the bracket to look for a root in. If you think that the root you are looking for exists in another bracket of numbers, you can change the startX and endX parameters.

The algorithm constantly divides the bracket into half and stops when the maxIterations is reached or a root is found. If the root is not found for f(x) = 0, it gives the closest value to the root found until max number of iterations is reached.
