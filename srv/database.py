import sqlite3


class LambeijosDB:
    def __init__(self):
        self.db_name = "tmp/lambeijos.db"
        self.connection = sqlite3.connect(self.db_name)
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

    def escrever_dados_usuario(self, email, usuario, senha, numero_contato):
        # Executar uma instrução SQL para inserir dados na tabela
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """INSERT INTO Usuarios (email, usuario, senha, numero_contato) VALUES (?, ?, ?, ?)""",
            (email, usuario, senha, numero_contato),
        )

    def escrever_dados_cliente(
        self, nome, raca, idade, comportamento, sobre, usuario_id
    ):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """INSERT INTO Cliente (nome, raca, idade, comportamento, sobre, usuario_id) VALUES (?, ?, ?, ?, ?, ?)""",
            (nome, raca, idade, comportamento, sobre, usuario_id),
        )

    def user_exists(self, user):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            SELECT id FROM Usuarios WHERE usuario = (?)
            """,
            (user),
        )
        user = self.cursor.fetchone()

        return user if user else False

    def validate_password(self, id):
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            SELECT senha FROM Usuarios WHERE id = (?)
            """,
            (id),
        )
        senha = self.cursor.fetchone()

        return senha if senha else False


if __name__ == "__main__":
    x = LambeijosDB()
    x.create_table()
    x.escrever_dados_usuario('teste2@teste.com', 'teste2', 1234, 19999999998)
    x.escrever_dados_cliente('Macondo', 'Shiba inu', 4, 'Manso', 'Tem muita energia', 1)
    
