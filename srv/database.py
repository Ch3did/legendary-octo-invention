import sqlite3


class LambeijosDB:
    def __init__(self):
        self.db_name = "./tmp/lambeijos.db"
        self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Usuarios (
                    id INTEGER PRIMARY KEY,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT,
                    numero_contato TEXT	
                     );"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Cliente (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    raca TEXT,
                    idade INTEGER,
                    comportamento TEXT,
                    sobre TEXT,
                    usuario_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
                     );"""
        )
        
    def select_client_from_id(self, id):
        # Executar uma instrução SQL para inserir dados na tabela
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """select * from cliente where usuario_id == (?) """,
            (id),
        )
        data = self.cursor.fetchall()
        return data

    def escrever_dados_usuario(self, email, usuario, senha, numero_contato):
        # Executar uma instrução SQL para inserir dados na tabela
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """INSERT INTO Usuarios (email, usuario, senha, numero_contato) VALUES (?, ?, ?, ?)""",
            (email, usuario, senha, numero_contato),
        )
        self.connection.commit()

    def escrever_dados_cliente(
        self, nome, raca, idade, comportamento, sobre, usuario_id
    ):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """INSERT INTO Cliente (nome, raca, idade, comportamento, sobre, usuario_id) VALUES (?, ?, ?, ?, ?, ?)""",
            (nome, raca, idade, comportamento, sobre, usuario_id),
        )
        self.connection.commit()

    def user_exists(self, user):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            SELECT id FROM Usuarios WHERE usuario = (?)
            """,
            (user,)
        )
        user = self.cursor.fetchone()
        print(f"user: {user}")

        return user[0] if user else False

    def validate_password(self, id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            SELECT senha FROM Usuarios WHERE id = (?)
            """,
            (id,)
        )
        senha = self.cursor.fetchone()

        return senha[0] if senha else False




x = LambeijosDB()
# x.create_table()
# x.escrever_dados_usuario('teste2@teste.com', 'teste2', 1234, 19999999998)
# x.escrever_dados_cliente('Macondo', 'Shiba inu', 4, 'Manso', 'Tem muita energia', 1)
# x.connection.commit()
from pprint import pprint
pprint(x.select_client_from_id("1"))