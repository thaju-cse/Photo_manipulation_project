from project import cinematic, bw, drawing
import os
import sys
from inputs_stamp import inputs, stamp


def test_cinematic():
    try:
        os.makedirs(stamp+'cinematic')
    except:
        print("Cannot create directory !!!")
        sys.exit()
    for value in inputs:
        I, J = value[0], value[1]
        assert cinematic(I, stamp+'cinematic/'+J) == 1


def test_bw():
    try:
        os.makedirs(stamp+'bw')
    except:
        print("Cannot create directory !!!")
        sys.exit()
    for value in inputs:
        I, J = value[0], value[1]
        assert bw(I, stamp+'bw/'+J) == 1


def test_drawing():
    try:
        os.makedirs(stamp+'drawing')
    except:
        print("Cannot create directory !!!")
        sys.exit()
    for value in inputs:
        I, J = value[0], value[1]
        assert drawing(I, stamp+'drawing/'+J) == 1


def main():
    # inputs = [
    #         ['Images/input/art.jpeg','art.jpeg'],
    #         ['Images/input/eye_bw.jpeg','eye_bw.jpeg'],
    #         ['Images/input/eye_col.jpeg','eye_col.jpeg'],
    #         ['Images/input/rose_bw.jpeg','rose_bw.jpeg'],
    #         ['Images/input/sand.jpeg','sand.jpeg']
    #     ]
    # stp = 'test_project_' + str(datetime.now())[8:10] + str(datetime.now())[-15:-13] +str(datetime.now())[-6:] +'/'
    test_cinematic()
    test_bw()
    test_drawing()


if __name__ == "__main__":
    main()
