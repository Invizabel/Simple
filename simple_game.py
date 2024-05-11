from simple_engine import *

def main():
    #sdl_init()
    window, render = sdl_window("hello", 640, 480, 2)
    input()
    sdl_exit(window, render)
    
if __name__ == "__main__":
    main()
