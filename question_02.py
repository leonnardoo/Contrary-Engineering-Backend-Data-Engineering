from config import utils

import sqlite3
from sqlite3 import Error


def question_02(destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                       SELECT COUNT(DISTINCT c.NAME) FROM companies c
                       LEFT JOIN people p
                       ON UPPER(c.COMPANY_LINKEDIN_NAMES) = UPPER(p.COMPANY_LI_NAME)
                       WHERE p.COMPANY_LI_NAME IS NULL;
                       """)

        for line in cur.fetchall():
            print(line)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    question_02(utils.db_raw_dir)
