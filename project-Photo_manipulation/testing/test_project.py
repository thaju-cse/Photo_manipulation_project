from project import cinematic,bw,drawing
from datetime import datetime
import os
import sys

def test_project():
    # inputs = [
    #     ['Images/input/art.jpeg','art.jpeg'],
    #     ['Images/input/eye_bw.jpeg','eye_bw.jpeg'],
    #     ['Images/input/eye_col.jpeg','eye_col.jpeg'],
    #     ['Images/input/rose_bw.jpeg','rose_bw.jpeg'],
    #     ['Images/input/sand.jpeg','sand.jpeg']
    # ]
    inputs = [
        ['art.jpeg','art.jpeg'],
        ['eye_bw.jpeg','eye_bw.jpeg'],
        ['eye_col.jpeg','eye_col.jpeg'],
        ['rose_bw.jpeg','rose_bw.jpeg'],
        ['sand.jpeg','sand.jpeg']
    ]

    stamp = 'test_project_' + str(datetime.now())[8:10] + str(datetime.now())[-15:-13] +str(datetime.now())[-6:] +'/'
    try:
        os.makedirs(stamp+'cinematic')
        os.makedirs(stamp+'bw')
        os.makedirs(stamp+'drawing')
    except:
        print("Cannot create directory !!!")
        sys.exit()
    for value in inputs:
        # stamp = 'test_project_' + str(datetime.now())[8:10] + str(datetime.now())[-15:-13] +str(datetime.now())[-6:] +'/'
        # try:
        #     os.makedirs(stamp+'cinematic')
        #     os.makedirs(stamp+'bw')
        #     os.makedirs(stamp+'drawing')
        # except:
        #     print("Cannot create directory !!!")
        #     sys.exit()
        I , J = value[0],value[1]
        # out = stamp+'art.jpeg'
        # assert cinematic ('Images/input/art.jpeg',out) == 0
        assert cinematic(I,stamp+'cinematic/'+J) == 1
        assert bw(I, stamp+'bw/'+J) == 1
        assert drawing(I, stamp+'drawing/'+J) == 1


if __name__ == "__main__":
    test_project()
