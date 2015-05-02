from ..core import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)

    def __repr__(self):
        return '<Post: {0}>'.format(self.title)
