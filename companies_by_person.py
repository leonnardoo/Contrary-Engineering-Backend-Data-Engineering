from config import utils

import sqlite3
from sqlite3 import Error

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--id", "-i", help="Person ID to search")
args = parser.parse_args()


def companies_by_person(id, destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT DISTINCT COMPANY_NAME FROM people
                       WHERE PERSON_ID = "{id}";
                       """)

        companies = ()

        for line in cur.fetchall():
            companies += line

        return companies

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    def main():
        companies_by_person(args.id, utils.db_raw_dir)

    main()

# Example of run script:
# python.exe companies_by_person.py -i 92a52877-8d5d-41a6-950f-1b9c6574be7a
