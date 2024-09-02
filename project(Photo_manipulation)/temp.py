import os
from datetime import datetime
print(str(datetime.now())[8:10] + str(datetime.now())[-15:-13] + str(datetime.now())[-6:])

os.makedirs('new_one')
