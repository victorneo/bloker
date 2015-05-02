from bloker import create_app as createapp
from bloker.posts.models import Post
from bloker.core import db
from flask.ext.testing import TestCase


class PostTest(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_repr(self):
        title = 'Post Title'
        p = Post(title=title, content='123')
        db.session.add(p)
        db.session.commit()

        p = Post.query.first()
        self.assertEquals('<Post: {0}>'.format(title), str(p))

    def create_app(self):
        app = createapp('settings_test')
        app.config['TESTING'] = True
        return app