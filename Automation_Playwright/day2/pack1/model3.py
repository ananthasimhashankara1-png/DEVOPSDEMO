import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pack1.client import client1
from pack1.model2 import model2
from pack1.model1 import model1

model1()
model2()
client1()


