import pytest

import numpy as np
import quadratic

def test_quadratic():
    x1,x2 = quadratic.quadratic(a = 0.001, b = 1000, c= 0.001)
    assert(np.abs(x1-(-1e-6)) < 1e-10)
    assert(np.abs(x2-(-0.999999999999e+6)) < 1e-10)
    
    x1,x2 = quadratic.quadratic(a = 0.001, b = -1000, c= 0.001)
    assert(np.abs(x1-(0.999999999999e+6)) < 1e-10)
    assert(np.abs(x2-(1e-6)) < 1e-10)
    
    x1,x2 = quadratic.quadratic(a = 1, b = 8, c= 12)
    assert(np.abs(x1-( -2 )) < 1e-10)
    assert(np.abs(x2-( - 6 )) < 1e-10)


