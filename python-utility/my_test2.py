import os
import os as o
from os import path
from os import path as p

out1 = os.path.basename("/home/pi")
print(out1)
out2 = o.path.basename("/home/pi")
print(out2)
out3 = path.basename("/home/pi")
print(out3)
out4 = p.basename("/home/pi")
print(out4)

