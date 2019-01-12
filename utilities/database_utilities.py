import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'words.db')

def create_database(database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "CREATE TABLE words (word TEXT PRIMARY KEY NOT NULL, usage_count INT DEFAULT 1 NOT NULL)"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cur.execute(ddl)
    conn.close()

def save_words_to_database(words_list: list, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check to see if the words is in there
            sql = "select count(word) from words where word='" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cur.execute(sql)
        print("Database save complete!")


def execute_query(sql: str, database_path=DEFAULT_PATH):
    conn = sqlite3.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
    conn.close()

# conn = db_connect()
# curs = conn.cursor()
