from my_interval import setInterval
from api import ClickBank


def main():

    for i in range(20):
        bot = ClickBank()
        bot()
        print(i)
        i+= 1
        print("visiting the site now.... Done!")


if __name__ == '__main__':
    setInterval(main,5)