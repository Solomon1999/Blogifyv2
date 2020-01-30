from flask import Blueprint, request, url_for, render_template, flash, session, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user
# from models import Users, Blogs, Comments, Likes
# from app.main.forms import CommentForm
from models import Blogs
from app import app, db
import random


main = Blueprint('main', __name__, url_prefix='/main')


@app.route('/', methods=['GET', 'POST'])
def home():
    blogs = Blogs.query.all()
    return jsonify([{
        'Id' : blog.id,
        'Title' : blog.title,
        'Body' : blog.body,
        'Excerpt' : blog.excerpt,
        'Author' : blog.author,
        'Category' : blog.category

    } for blog in blogs])


@main.route('/category/<category>')
def Category(category):
    blogs = Blogs.query.filter_by(category=category).all()
    if blogs:
        return jsonify([{
            'Id' : blog.id,
            'Title' : blog.title,
            'Body' : blog.body,
            'Excerpt' : blog.excerpt,
            'Author' : blog.author,
            'Category' : blog.category

        } for blog in blogs])
    else:
        return 'None'


@main.route('fullblog/<blog_id>')
def FullBlog(blog_id):
    blog = Blogs.query.filter_by(id=blog_id).first()
    if blog:
        return jsonify({
            'Id' : blog.id,
            'Title' : blog.title,
            'Body' : blog.body,
            'Author' : blog.author,     
        })
    else:
        return 'None'



# @main.route(f'/full_blog/<blog>/author:<author>', methods=['GET', 'POST'])
# def full_blog(blog, author):
#     forms = CommentForm(request.form)
#     bl = Blogs.query.filter_by(id=blog).first()
    

#     def comment():
#         if request.method == 'POST' and forms.validate():
#             username = forms.Username.data
#             email = forms.Email.data
#             body = forms.Body.data
#             if current_user.is_authenticated:
#                 comment = Comments(username=current_user.username, email=current_user.email, body=body, blog_id=blog)
#             else:
#                 comment = Comments(username=username, email=email, body=body, blog_id=blog)

#             db.session.add(comment)
#             db.session.commit()
#     comment()

#     # def likes():
#     #     if request.method == 'POST' and forms.validate():
#     #         like = request.form['likes']
#     #         if current_user.is_authenticated:
#     #             user = Likes(username=current_user.username)
#     #         else:
#     #                 user = Likes(username='Anonymous')
#     #         db.session.add(user)
#     #         db.session.commit()
        
#     # likes()

#     return render_template("index.html")

