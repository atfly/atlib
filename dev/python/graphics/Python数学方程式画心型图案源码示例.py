
"""
'17*x^2 - 16*|x|*y + 17*y^2 = 225'
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-5.0, 5.0, 0.1)
Y = np.arange(-5.0, 5.0, 0.1)

#www.iplaypy.com

x, y = np.meshgrid(X, Y)
f = 17 * x ** 2 - 16 * np.abs(x) * y + 17 * y ** 2 - 225

fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()

"""
'(x^2+y^2+y)^2 = x^2 + y^2'
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-2.0, 2.0, 0.05)
Y = np.arange(-2.0, 2.0, 0.05)

x, y = np.meshgrid(X, Y)
f = (x ** 2 + y ** 2 + y) ** 2 - x ** 2 - y ** 2

fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()
"""
'8*x^2 - 9*|x|*y + 8*y^2 = 17'
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-2.5, 2.5, 0.05)
Y = np.arange(-2.5, 2.5, 0.05)

x, y = np.meshgrid(X, Y)
f = 8 * x ** 2 - 9 * np.abs(x) * y + 8 * y ** 2 - 17
fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()
"""
'(x^2 + y^2 - 1)^3 - x^2*y^3 = 0'
"""
import numpy as np
import matplotlib.pyplot as plt
import math
X = np.arange(-2.0, 2.0, 0.05)
Y = np.arange(-2.0, 2.0, 0.05)

x, y = np.meshgrid(X, Y)

f = (x ** 2 + y ** 2 - 1) ** 2 * (x ** 2 + y ** 2 - 1)- x ** 2 *  y ** 2 * y
fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()