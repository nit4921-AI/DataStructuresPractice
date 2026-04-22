def timeConversion(s):
    period = s[-2:]      # AM or PM
    hour = int(s[:2])    # extract hour
    rest = s[2:-2]       # :MM:SS

    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{rest}"


if __name__ == "__main__":
    s = "07:05:45PM"   # ✅ predefined input
    print(timeConversion(s))