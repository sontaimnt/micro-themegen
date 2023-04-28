# dependencies

from os import chdir, getlogin , mkdir
from os.path import isdir

# hardcode path
MICRO_CONFIG_PATH = f"/home/{getlogin()}/.config/micro/colorschemes"

# check if MICRO_CONFIG_PATH exists
if isdir(MICRO_CONFIG_PATH) == True:
    pass
else:
    mkdir(MICRO_CONFIG_PATH)
    pass 

# scheme name
color_name = str(input("enter the name of your theme:- "))

# ask colors
print("enter the colors in hex values:-")
color_bg = str(input("enter background color:- "))
color_fg1 = str(input("enter foreground1 color:- "))
color_fg2 = str(input("enter foreground2 color:- "))
color_red = str(input("enter red color:- "))
color_orange = str(input("enter orange color:- "))
color_yellow = str(input("enter yellow color:- "))
color_green = str(input("enter green color:- "))
color_blue = str(input("enter blue color:- "))
color_cyan = str(input("enter cyan color:- "))
color_magenta = str(input("enter magenta color:- "))

FILE_STRUCTURE = f'''
color-link default "{color_fg1},{color_bg}"
color-link comment "{color_fg2}"

color-link identifier "{color_green}"
color-link identifier.class "{color_cyan}"
color-link identifier.var "{color_fg2}"

color-link constant "{color_blue}"
color-link constant.number "{color_fg1}"
color-link constant.string "{color_yellow}"

color-link symbol "{color_magenta}"
color-link symbol.brackets "{color_fg1}"
color-link symbol.tag "{color_blue}"

color-link type "italic {color_cyan}"
color-link type.keyword "{color_magenta}"

color-link special "{color_magenta}"
color-link statement "{color_magenta}"
color-link preproc "{color_magenta}"

color-link underlined "{color_magenta}"
color-link error "bold {color_red}"
color-link todo "bold {color_magenta}"

color-link diff-added "{color_green}"
color-link diff-modified "{color_orange}"
color-link diff-deleted "{color_red}"

color-link gutter-error "{color_red}"
color-link gutter-warning "{color_yellow}"

color-link statusline "{color_bg},{color_fg1}"
color-link tabbar "{color_bg},{color_fg1}"
color-link indent-char "{color_fg1}"
color-link line-number "{color_fg1}"
color-link current-line-number "{color_fg1}"

color-link cursor-line "{color_fg2},{color_fg1}"
color-link color-column "{color_fg2}"
color-link type.extended "default"
'''

file = MICRO_CONFIG_PATH+"/"+f"{color_name}"+".theme"
config = open(file, "x")
config.write(FILE_STRUCTURE)
