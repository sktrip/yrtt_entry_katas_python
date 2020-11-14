# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h, m, s):
    hour_milliseconds = h * 60 * 60 * 1000
    minute_milliseconds = m * 60 * 1000
    seconds_milliseconds = s * 1000
    time_milliseconds = hour_milliseconds + minute_milliseconds + seconds_milliseconds
    return time_milliseconds

