import time
from optparse import OptionParser


def build_option_parser():
    parser = OptionParser()
    parser.add_option("-t", "--time", dest="given_time", type="int")
    return parser.parse_args()


def countdown_timer(given_time_seconds):
    while given_time_seconds:
        minutes, seconds = divmod(given_time_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        print(time_format, end='\r')
        time.sleep(1)
        given_time_seconds -= 1


def main():
    (options, args) = build_option_parser()
    given_time = options.given_time
    countdown_timer(given_time)
