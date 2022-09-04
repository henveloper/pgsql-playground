from socketserver import DatagramRequestHandler
from typing import List
from getCovidData import CovidData
from psycopg2 import connect


def writeToDB(data: List[CovidData]):
    print(f"data has length {len(data)}")
    connection = connect(dbname="postgres", user="postgres",
                         password="123456", host="localhost", port="5432")

    i = 0
    for datum in data:
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO covid_data "
                "(case_no, reportDate, dateOfOnset, gender, age, nameOfHospitalAdmitted, status, hkResidence, classification, caseStatus) "
                "VALUES "
                f"(\'{datum.case_no}\', \'{datum.report_date}\', \'{datum.date_of_onset}\', \'{datum.gender}\', \'{datum.age}\', \'{datum.name_of_hospital_admitted}\', \'{datum.status}\', \'{datum.hk_residence}\', \'{datum.classification}\', \'{datum.case_status}\')"
            )
        connection.commit()
        print(i)
        i += 1
