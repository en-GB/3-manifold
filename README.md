# This is a fork of the project 3-manifold to update the roomgen.py to add random rooms sizes

# Original README :

# 3-manifold


https://www.youtube.com/watch?v=CBPTcUxIISQ

i made this around 2016



to run, execute 3_less.c

if your not using windows you probably have to change the compiler flags at the top

the level is defined in roomgen.py starting on line 421

# other maps

https://github.com/PyMaster22/manifold-maps

# windows build instructions:

- install this: https://www.msys2.org/ (make sure you follow steps 5-7 aswell)
- open mingw64 (c:/msys64/mingw64 is the default install location)
- to install clang type in ``pacman -S mingw-w64-x86_64-clang`` and press enter 
- to install glfw type in ``pacman -S mingw-w64-x86_64-glfw`` and press enter
- then drag 3_less.c into the window and press enter

# debian/ubuntu build instructions
- `apt install libglfw3-dev`
- `apt install clang`
- `python3 3_roomgen.py`
- `clang 3_less.c -std=c99 -Wall -Werror -Wno-unused -lglfw -lm -ldl`

# arch linux build instructions:

- `pacman -S glfw-x11`
    - or if you use wayland `pacman -S glfw-wayland`
- `pacman -S clang`
- `python3 3_roomgen.py`
- `clang 3_less.c -std=c99 -Wall -Werror -Wno-unused -lglfw -lm -ldl`


these were contributed by other people so i dont know if they work

