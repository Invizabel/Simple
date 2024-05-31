from simple_engine import *
import time

def main():
    simple_init()
    simple_display(640, 480, 2)
    simple_background(255, 0, 0, 255)
    simple_line(0, 255, 255, 0, 0, 0, 100, 100)
    simple_update()
    time.sleep(15)
    simple_exit()
    
if __name__ == "__main__":
    main()
