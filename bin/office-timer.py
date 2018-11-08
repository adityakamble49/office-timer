from optparse import OptionParser

from officetimer import timer_controller


def build_option_parser():
    parser = OptionParser()
    parser.add_option("-t", "--time", dest="given_time", type="int")
    return parser.parse_args()


if __name__ == '__main__':
    (options, args) = build_option_parser()
    given_time = options.given_time
    timer_controller.countdown_timer(given_time)
