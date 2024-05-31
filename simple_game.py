from simple_engine import *
import time

def main():
    square = [(50, 50, 100, 50),
              (50, 50, 50, 100),
              (50, 100, 100, 100),
              (100, 100, 100, 150),
              (100, 150, 50, 150)]
    
    simple_init()
    simple_display(640, 480, 2)
    simple_background(255, 0, 0, 255)
    for i in square:
        simple_line(0, 255, 255, 0, i[0], i[1], i[2], i[3])

    simple_update()
    time.sleep(15)
    simple_exit()
    
if __name__ == "__main__":
    main()
