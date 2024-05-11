from simple_engine import *

def main():
    #sdl_init()
    window, renderer = sdl_window("simple", 640, 480, 2)
    input()
    sdl_exit(window, renderer)
    
if __name__ == "__main__":
    main()
