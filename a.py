from pprint import pprint


def fuck_printer():
    fuck = "fuck /fuck /fuck /fuck /fuck /fuck /fuck /fuck /fuck /"
    pprint([fuck, fuck, fuck])


if __name__ == "__main__":
    (fuck_printer() for _ in range(100))
