from flask import Blueprint, jsonify
from .models import Post


bp = Blueprint('posts', __name__)


@bp.route('/posts/')
def show_posts():
    posts = Post.query.all()
    return jsonify(
        [{'id': p.id, 'title': p.title, 'content': p.content} for p in posts]
    )
