import ctypes
import os

# global constants
SDL_INIT_EVENTS = 0x0001
SDL_INIT_VIDEO = 0x0002
SDL_QUIT = 0x100

# global path
sdl3_path = os.path.abspath("dll/SDL3.dll")
sdl3 = ctypes.CDLL(sdl3_path)
sdl3.SDL_Init(0x00000001 | 0x00000010 | 0x00000020 | 0x00000200 | 0x00001000 | 0x00002000 | 0x00004000 | 0x00008000 | 0x00100000)

# create window and renderer (credit: https://gist.github.com/NickBeeuwsaert/29780f01debf60dedc8a)
def sdl_window(title, width, height, flags):
    window, renderer = ctypes.c_void_p(), ctypes.c_void_p()
    sdl3.SDL_CreateWindowAndRenderer(title.encode(), width, height, flags, ctypes.byref(window), ctypes.byref(renderer))
    return window, renderer


# exit sdl and clean up
def sdl_exit(window, render):
    sdl3.SDL_DestroyRenderer(render)
    sdl3.SDL_DestroyWindow(window)
    SDL_QUIT
