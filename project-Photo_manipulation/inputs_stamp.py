from datetime import datetime

''' Test cases inputs as constants
'''
inputs = [
            ['Images/input/art.jpeg','art.jpeg'],
            ['Images/input/eye_bw.jpeg','eye_bw.jpeg'],
            ['Images/input/eye_col.jpeg','eye_col.jpeg'],
            ['Images/input/rose_bw.jpeg','rose_bw.jpeg'],
            ['Images/input/sand.jpeg','sand.jpeg']
        ]
stamp = 'test_project_' + str(datetime.now())[8:10] + str(datetime.now())[-15:-13] +str(datetime.now())[-6:] +'/'
