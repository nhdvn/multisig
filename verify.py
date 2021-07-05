
from demo.curve import *

# y^2 = x^3 - 2x + 15 mod 307 
# order = 311

P = Point(97, 200, E)
R = Point(81, 201, E)
e = hash_signature(P, R, 'tomato')
e = bytes_to_long(e)

print(308 * G == R + P * e)