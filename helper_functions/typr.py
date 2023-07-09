"""Creating this module to house functions that change how print() works
-or rather are custom printing functions using print() and other methods
By: patjcolon
Last updated: 6/28/2023"""

from time import sleep
from .styl import unstyl

# WIP. Needs serious cleaning and some improvements to commenting
def typr(text_to_print: str = "", speed: str = "fast", endline: bool = True):
    """prints letter by letter rather than all at once
    first parameter is the text to print, second is how fast
    speeds: 'slow', 'medium', 'fast', 'fastest' """
    
    # Super sloppy code but functional
    if speed == "medium": speed = 0.05
    elif speed == "fast": speed = 0.03
    elif speed == "slow": speed = 1
    stprs = ".,!?-:"
    skprs = ":"
    hit_skpr = False
    fastest = False
    stpr_speed = 0.6
    end_speed = 0.6
    c_since_endline = 0
    if speed == "fastest": 
        fastest = True
        hit_skpr = True
    speed = 0.03

    for c in str(text_to_print):
        end_speed = 0.6
        c_since_endline +=1
        if fastest and hit_skpr: 
            if c_since_endline > 350 and c in stprs:
                c_since_endline = 0
                print(f"{unstyl()}{c} ")
                sleep(0.1)
                continue
            if c in stprs:
                print(c, end="", flush=True)
                sleep(0.01)
                continue
            print(c, end="", flush=True)
            continue
        
        if c in skprs:
            hit_skpr = True
            speed = 0
            stpr_speed = 0.05
        if c_since_endline > 350 and c in stprs:
            c_since_endline = 0
            print(f"{unstyl()}{c} ")
            sleep(end_speed)
            sleep(speed)
            continue
        if c in stprs:
            print(c, end="", flush=True)
            sleep(stpr_speed)
            sleep(speed)
            end_speed = 0
            continue
        sleep(speed)
        print(c, end="", flush=True)
        end_speed = 0.6
    sleep(end_speed)
    if endline: print()
    return ""
