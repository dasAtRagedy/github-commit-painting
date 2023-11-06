import sys

from src.tkinter_app.main_window import start_app

def main(year:int = 2015):
    """This is the entry point of the application"""
    start_app(year=year)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        year = 2015 # default value
        print(f"No year has been entered, defaulting to {year}")
    elif len(sys.argv) > 2:
        print(f"Expected parameter amount <= 1, provided {len(sys.argv)-1}; Terminating the application.")
        quit()
    year = int(sys.argv[1])
    print(f"Year is {year}")
    main(year=year)