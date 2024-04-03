import sqlite3

class LambeijosDB:
    def __init__(self):
        self.db_name = "lambeijos.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def create_table(self):
        self.connect()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS lambeijos (
                                id INTEGER PRIMARY KEY,
                                mensagem TEXT)''')
        self.close()

    def escrever_mensagem(self, mensagem):
        self.connect()
        self.cursor.execute("INSERT INTO lambeijos (mensagem) VALUES (?)", (mensagem,))
        self.close()

    def ler_mensagens(self):
        self.connect()
        self.cursor.execute("SELECT * FROM lambeijos")
        mensagens = self.cursor.fetchall()
        self.close()
        return mensagens
