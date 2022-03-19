from my_interval import setInterval
from api import ClickBank


def main():

    for _ in range(25):
        bot = ClickBank()
        bot()
        print("visiting the site now.... Done!")


if __name__ == '__main__':
    setInterval(main,5)