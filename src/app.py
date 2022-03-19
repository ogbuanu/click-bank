from my_interval import setInterval
from api import ClickBank


def main():

    bot = ClickBank()
    bot()
    print("visiting the site now.... Done!")


if __name__ == '__main__':
    setInterval(main,5)