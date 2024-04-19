from srv.database import LambeijosDB


class View:
    def __init__(self):
        self.db = LambeijosDB()

    def auth_validation(self, user, password):
        if id := self.db.user_exists(user):
            senha = self.db.validate_password(id)

            if password == senha:
                return id

        return False
