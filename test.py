import math
import time

from qdvis.writer import LogWriter

writer = LogWriter()
for i in range(100):
    time.sleep(4)
    y = math.exp(i)
    writer.add_scalar(x_value=i, y_value=y)
