from my_interval import setInterval
from api import ClickBank


def main():

    for _ in range(20):
        bot = ClickBank()
        bot()


if __name__ == '__main__':
    setInterval(main,5)