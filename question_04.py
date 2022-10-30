from config import utils

import sqlite3
from sqlite3 import Error


def question_04(destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT p.PERSON_ID, p.COMPANY_NAME, CAST(c.HEADCOUNT AS INTEGER) AS HEADCOUNT  FROM people p
                       LEFT JOIN companies c
                       ON UPPER(c.COMPANY_LINKEDIN_NAMES) = UPPER(p.COMPANY_LI_NAME)
                       WHERE LOWER(p.LAST_TITLE) LIKE "%founder%"
                       ORDER BY HEADCOUNT DESC
                       LIMIT 3;
                       """)

        for line in cur.fetchall():
            print(line)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    question_04(utils.db_raw_dir)
