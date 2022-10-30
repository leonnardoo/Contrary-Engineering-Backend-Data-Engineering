from config import utils

import sqlite3
from sqlite3 import Error


def question_05(destination_database):
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()

        cur.execute(f"""
                    SELECT ROUND(AVG(difference_years),2) AS avg_difference_years, COUNT(DISTINCT PERSON_ID) FROM (
                       SELECT p.PERSON_ID, p.COMPANY_NAME, (JULIANDAY(CAST(p.GROUP_END_DATE AS DATE)) - JULIANDAY(CAST(p.GROUP_START_DATE AS DATE)))/365 AS difference_years,
                       RANK () OVER ( 
	                            	PARTITION BY p.PERSON_ID
	                            	ORDER BY CAST(p.GROUP_START_DATE AS DATE) DESC
	                            ) job_recent_rank 
                       FROM people p
                    )
                    WHERE job_recent_rank = 2;
                    """)

        for line in cur.fetchall():
            print(line)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    question_05(utils.db_raw_dir)
