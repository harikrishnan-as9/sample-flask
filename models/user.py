from db import db

class UserModel(db.Model):

    __tablename__ = 'user_tbl'
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='default')

    def json(self):
        return {
            '_id': self._id,
            'username': self.username,
            'role': self.role,
            'isAdmin': self.role.lower() == 'admin',
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
