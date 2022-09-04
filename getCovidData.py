from io import StringIO
from random import vonmisesvariate
from typing import List
import requests
from io import StringIO
import csv


class CovidData:
    def __init__(self, case_no: int, report_date: str, date_of_onset: str, gender: str, age: str, name_of_hospital_admitted: str, status: str, hk_residence: str, classification: str, case_status: str) -> None:
        self.case_no = case_no
        self.report_date = report_date
        self.date_of_onset = date_of_onset
        self.gender = gender
        self.age = age  # can't be int because "<1"
        self.name_of_hospital_admitted = name_of_hospital_admitted
        self.status = status
        self.hk_residence = hk_residence
        self.classification = classification
        self.case_status = case_status


def getCovidData() -> List[CovidData]:
    DATA_URL = "http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv"
    resp_text = requests.get(DATA_URL).text
    reader = csv.reader(StringIO(resp_text), delimiter=",")
    next(reader)  # skip header

    data: List[CovidData] = []
    for row in reader:
        covid_data = CovidData(
            case_no=int(row[0]),
            report_date=row[1],
            date_of_onset=row[2],
            gender=row[3],
            age=row[4],
            name_of_hospital_admitted=row[5],
            status=row[6],
            hk_residence=row[7],
            classification=row[8],
            case_status=row[9],
        )
        data.append(covid_data)
    return data


if (__name__ == "__main__"):
    getCovidData()
