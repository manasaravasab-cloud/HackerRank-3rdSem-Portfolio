import sys

def time_conversion(s: str) -> str:
    """
    Converts 12-hour AM/PM time format to 24-hour military time format.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    period = s[-2:]
    hours = int(s[:2])
    rest = s[2:-2]

    if period == "AM":
        hours = 0 if hours == 12 else hours
    else:  # PM
        hours = hours if hours == 12 else hours + 12

    return f"{hours:02d}{rest}"

if __name__ == "__main__":
    line = sys.stdin.read().strip()
    if line:
        print(time_conversion(line))
