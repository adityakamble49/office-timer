import time
from optparse import OptionParser


def build_option_parser():
    parser = OptionParser()
    parser.add_option("-t", "--time", dest="given_time", type="string", help="Use HH:MM format for timer")
    return parser.parse_args()


def countdown_timer(given_time_seconds):
    while given_time_seconds:
        minutes, seconds = divmod(given_time_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(time_format, end='\r')
        time.sleep(1)
        given_time_seconds -= 1


def main():
    (options, args) = build_option_parser()
    given_time = options.given_time
    if given_time:
        hours = int(given_time.split(':')[0])
        minutes = int(given_time.split(':')[1])
        given_time_seconds = (hours * 3600) + (minutes * 60)
        countdown_timer(given_time_seconds)
    else:
        print("Use -h option to view help\n Developer: Aditya Kamble (adityakamble49.com)")


if __name__ == '__main__':
    main()
