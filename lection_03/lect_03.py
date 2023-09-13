import datetime

from flask import Flask, render_template, jsonify
from lection_03.models_03 import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
db.init_app(app)


# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#     print('ok')
#
#
# @app.cli.command('add-jhon')
# def add_user():
#     user = User(username='Вася', email='ываы@sdfsf')
#     db.session.add(user)
#     db.session.commit()
#     print('ok - added')
#
# @app.cli.command('edit-jhon')
# def edit_user():
#     user = User.query.filter_by (username='Вася').first()
#     user.username = 'Петя'
#     user.email = 'qqq@www'
#     db.session.commit()
#     print('ok - изменено')
#
#
# @app.cli.command('delete-jhon')
# def edit_user():
#     user = User.query.filter_by (username='Петя').first()
#     db.session.delete(user)
#     db.session.commit()
#     print('ok - удалено')
#
#
# @app.cli.command('fill-tab')
# def fill_tab():
#     # добавление юзеров
#     count = 5
#     for user_num in range(1, count + 1):
#         new_user = User(username=f'user_{user_num}', email=f'user_{user_num}@ddd.ru')
#         db.session.add(new_user)
#     db.session.commit()
#
#     # добавление статей
#     for post in range(1, count ** 2):
#         author = User.query.filter_by(username=f'user_{post %  count + 1}').first()
#         new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
#         db.session.add(new_post)
#     db.session.commit()

@app.route('/')
def start():
    return render_template('start.html')


@app.route('/data')
def data():
    return "Your data"

@app.route('/users')
def all_users():
    users = User.query.all()
    content = {'users': users}
    return render_template('users_data.html', **content)

@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users_data.html', **context)

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id,
              'title': post.title,
              'content': post.content,
              'created_at': post.created_id} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

@app.route('/posts/last-week')
def get_posts_last_week():
    date = datetime.utcnow() - datetime.timedelta(days=7)
    posts = Post.query.filter_by(Post.created_id <= date).all()
    if posts:
        return jsonify(
            [{'id': post.id,
              'title': post.title,
              'content': post.content,
              'created_at': post.created_id} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})


if __name__ == '__main__':
    app.run(debug=True)