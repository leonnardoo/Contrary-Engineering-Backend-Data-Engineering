from config import utils

import pandas as pd

import sqlite3
from sqlite3 import Error

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="Source url from file csv")
args = parser.parse_args()


def request_api_save_file(url, destination_database):
    data = pd.read_csv(url)
    split = url.split("/")
    name_table = split[-1:][0].replace(".csv", "")
    columns_create = ""
    columns_size = ""
    columns = ""

    for column in data.columns:
        columns_create += (column + " TEXT, ")
        columns += (column + ",")
        columns_size += ("?,")

    if name_table == "companies":
        data["HEADCOUNT"] = data["HEADCOUNT"].fillna(
            0.0).astype(int).astype(str)
        data["MOST_RECENT_RAISE"] = data["MOST_RECENT_RAISE"].fillna(
            0.0).astype(int).astype(str)
        data["MOST_RECENT_VALUATION"] = data["MOST_RECENT_VALUATION"].fillna(
            0.0).astype(int).astype(str)
        data["KNOWN_TOTAL_FUNDING"] = data["KNOWN_TOTAL_FUNDING"].fillna(
            0.0).astype(int).astype(str)
        data["COMPANY_LINKEDIN_NAMES"] = data["COMPANY_LINKEDIN_NAMES"].map(
            lambda x: x.strip().replace('[\n', "").replace('\n]', "").replace('"', '').strip())
        data["INVESTORS"] = data["INVESTORS"].astype(str).map(lambda x: x.strip().replace(
            '[\n', "").replace('\n]', "").replace('"', '').replace('\n', '').strip())

    list_data = data.values.tolist()

    conn = None
    try:
        conn = sqlite3.connect(destination_database)
        cur = conn.cursor()
        cur.executescript(f"""
                            BEGIN;
                            DROP TABLE IF EXISTS {name_table};
                            CREATE TABLE IF NOT EXISTS {name_table}({columns_create[:-2]});
                            COMMIT;
                        """)

        cur.executemany(f"""
                           INSERT INTO {name_table} ({columns[:-1]})
                           VALUES ({columns_size[:-1]})
                           """, list_data)

        conn.commit()
        print("Insert data sucessful.")

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    return


if __name__ == "__main__":
    url = args.url
    request_api_save_file(url, utils.db_raw_dir)

# Example of run script:
# python.exe ingest.py -u https://contrary-engineering-interview.s3.amazonaws.com/data/companies.csv
# python.exe ingest.py -u https://contrary-engineering-interview.s3.amazonaws.com/data/people.csv
