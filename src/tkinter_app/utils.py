from enum import Enum

class ColorPalette(Enum):
    EMPTY = "#161b22"
    LOW = "#0e4429"
    MEDIUM = "#006d32"
    HIGH = "#26a641"
    FULL = "#39d353"

    
def get_initial_offset(year:int) -> int:
    from datetime import datetime
    return datetime(year, 1, 1).weekday()

def is_leap_year(year:int) -> bool:
    return year%4 == 0 and (year % 400 == 0 or year % 100 != 0)

