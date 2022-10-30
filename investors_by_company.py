from config import utils

import sqlite3
from sqlite3 import Error

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--linkedin_name", "-l", help="LinkedIn name of company")
args = parser.parse_args()


def investors_by_company(company, destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT INVESTORS FROM companies
                       WHERE COMPANY_LINKEDIN_NAMES = "{company}";
                       """)

        investors = ()

        for line in cur.fetchall():
            investors += line

        return investors

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    def main():
        print(investors_by_company(args.linkedin_name, utils.db_raw_dir))

    main()

# Example of run script:
# python.exe investors_by_company.py -l toast-inc
