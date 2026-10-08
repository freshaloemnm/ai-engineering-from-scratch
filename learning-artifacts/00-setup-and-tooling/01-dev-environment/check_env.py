import sys
print(sys.executable)
print(sys.version)

import numpy as np
print(np.__version__)

a = np.array([1,2,3])
print(np.dot(a,a))
