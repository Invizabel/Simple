import ctypes
import os
import sys

# global constants
SDL_INIT_EVENTS = 0x0001
SDL_INIT_VIDEO = 0x0002
SDL_QUIT = 0x100

# initialize sdl
def simple_init():
    global sdl
    sdl = ctypes.CDLL("libSDL2.so")
    sdl.SDL_Init(0x00000001 | 0x00000010 | 0x00000020 | 0x00000200 | 0x00001000 | 0x00002000 | 0x00004000 | 0x00008000 | 0x00100000)

# change background color
def simple_background(r, g, b, a):
    sdl.SDL_SetRenderDrawColor(sdl_renderer, r, g, b, a)
    sdl.SDL_RenderClear(sdl_renderer)
    
# create window and renderer (credit: https://gist.github.com/NickBeeuwsaert/29780f01debf60dedc8a)
def simple_display(width, height, flags):
    global sdl_window
    global sdl_renderer
    sdl_window, sdl_renderer = ctypes.c_void_p(), ctypes.c_void_p()
    sdl.SDL_CreateWindowAndRenderer(width, height, flags, ctypes.byref(sdl_window), ctypes.byref(sdl_renderer))

# draw line
def simple_line(r, g, b, a, x1, y1, x2, y2):
    sdl.SDL_SetRenderDrawColor(sdl_renderer, r, g, b, a)
    sdl.SDL_RenderDrawLine(sdl_renderer, x1, y1, x2, y2)

# update the display
def simple_update():
    sdl.SDL_RenderPresent(sdl_renderer)

# exit sdl and clean up
def simple_exit():
    sdl.SDL_DestroyRenderer(sdl_renderer)
    sdl.SDL_DestroyWindow(sdl_window)
    sys.exit()


    
