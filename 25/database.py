import sqlite3
class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        que_create = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_point INTEGER)'''
        self.cur.execute(que_create)
        self.con.commit()

    def get(self, que='SELECT * FROM score ORDER BY score_point DESC'):
        return self.cur.execute(que).fetchall()

    def insert(self, name, score):
        que_insert = f'''
        INSERT INTO score (name, score_point)
        VALUES ('{name}', {score})'''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):
        self.con.close()

    def update(self, name, score):
        que = f"""UPDATE score SET score_point = {score} WHERE name = '{name}'"""
        self.cur.execute(que)
        self.con.commit()
data_base = DataBase('score.sql')
# data_base.insert('best_player555', 10)
# data_base.insert('qwerty', 4)
# data_base.insert('test12345', 15)

data = data_base.get()
for line in data:
    print(line)
data_base.update("qwerty", 7)
for i in data_base.get():
    print(i)