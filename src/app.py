from my_interval import setInterval
from api import ClickBank


def main():
    bot = ClickBank()
    bot()


if __name__ == '__main__':
    setInterval(main,5)