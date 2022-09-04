from getCovidData import getCovidData
from writeToDB import writeToDB


def main():
    data = getCovidData()
    writeToDB(data)


if __name__ == "__main__":
    main()
