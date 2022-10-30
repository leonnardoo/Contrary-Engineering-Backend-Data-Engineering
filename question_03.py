from config import utils

import sqlite3
from sqlite3 import Error


def question_03(destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT DISTINCT c.NAME, CAST(c.HEADCOUNT AS INTEGER) AS HEADCOUNT FROM people p
                       LEFT JOIN companies c
                       ON UPPER(p.COMPANY_LI_NAME) = UPPER(c.COMPANY_LINKEDIN_NAMES)
                       ORDER BY HEADCOUNT DESC
                       LIMIT 10;
                       """)

        for line in cur.fetchall():
            print(line)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    question_03(utils.db_raw_dir)
