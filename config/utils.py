import os

config_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(config_dir)
db_dir = os.path.join(src_dir, "sqlite", "db")
db_raw_dir = os.path.join(db_dir, "raw.db")
