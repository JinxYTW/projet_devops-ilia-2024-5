from config import db


class User(db.Model):
    __tablename__ = 'users'

    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(50), primary_key=True)
    pseudo = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "username": self.username,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "email": self.email,
            "pseudo": self.pseudo
        }
    
    def to_dict_min(self):
        return {
            "username": self.username,
            "pseudo": self.pseudo
        }
