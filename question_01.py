from config import utils

import sqlite3
from sqlite3 import Error

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--id", "-i", help="Person ID to search")
args = parser.parse_args()


def question_01(id, destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT AVG(c.KNOWN_TOTAL_FUNDING) AS KNOWN_TOTAL_FUNDING FROM people p
                       LEFT JOIN companies c
                       ON UPPER(p.COMPANY_LI_NAME) = UPPER(c.COMPANY_LINKEDIN_NAMES)
                       WHERE p.PERSON_ID = "{id}";
                       """)

        person = ()
        
        for line in cur.fetchall():
            person += line

        return person

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    def main():
        print(question_01(args.id, utils.db_raw_dir))

    main()

# Example of run script:
# python.exe question_01.py -i 92a52877-8d5d-41a6-950f-1b9c6574be7a
