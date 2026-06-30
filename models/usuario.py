from database.fake_db import Database


class Usuario:
    def __init__(self, nome, email, cargo, crm_coren, senha, admin="nao"):
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.crm_coren = crm_coren
        self.senha = senha
        self.admin = admin

    def salvar(self):
        db = Database()
        with db.conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO usuarios (nome, email, cargo, crm_coren, senha, admin)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (self.nome, self.email, self.cargo, self.crm_coren, self.senha, self.admin),
            )

    @staticmethod
    def buscar_por_email(email):
        db = Database()
        with db.conectar() as conexao:
            cursor = conexao.execute(
                """
                SELECT * FROM usuarios WHERE email = ?
                """,
                (email,),
            )
            return cursor.fetchone()

    @staticmethod
    def buscar_por_crm_coren(crm_coren):
        db = Database()
        with db.conectar() as conexao:
            cursor = conexao.execute(
                """
                SELECT * FROM usuarios WHERE crm_coren = ?
                """,
                (crm_coren,),
            )
            return cursor.fetchone()

    @staticmethod
    def listar_todos():
        db = Database()
        with db.conectar() as conexao:
            cursor = conexao.execute(
                """
                SELECT * FROM usuarios ORDER BY id ASC
                """
            )
            return cursor.fetchall()

    @staticmethod
    def email_existe(email):
        return Usuario.buscar_por_email(email) is not None

    @staticmethod
    def autenticar(login_id, senha):
        db = Database()
        with db.conectar() as conexao:
            cursor = conexao.execute(
                """
                SELECT * FROM usuarios WHERE (email = ? OR crm_coren = ?) AND senha = ?
                """,
                (login_id, login_id, senha),
            )
            return cursor.fetchone()
        