from utilities import database_utilities
import os

os.chdir(os.path.dirname(__file__))
path = os.path.join(os.getcwd(), "words.db")
all_rows = database_utilities.execute_query("select * from words order by usage_count desc", database_path=path)
for row in all_rows:
     # row[0] returns the first column in the query (name), row[1] returns email column.
     print('{0} : {1}'.format(row[0], row[1]))