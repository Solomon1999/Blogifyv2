from flask import Blueprint, request, url_for, render_template, flash, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user
# from app.blogger.forms import CreateBlog
# from models import Users, Blogs
from app import db


blogger = Blueprint('blogger', __name__, url_prefix='/blogger')


@blogger.route('/account')
@login_required
def account():
    print(current_user.username)
    if current_user.is_authenticated:
        print('you are logged in')

    return f'{current_user.username}'

# @blogger.route('/create_blog', methods=['GET', 'POST'])
# @login_required
# def create_blog():
#     forms = CreateBlog(request.form)
#     if request.method == 'POST' and forms.validate():
#         title = forms.Title.data
#         excerpt = forms.Excerpt.data
#         category = forms.Category.data
#         print(category)
#         body = forms.Body.data

#         post_blog = Blogs(author=current_user.full_name, title=title, excerpt=excerpt, body=body, category=category)
#         db.session.add(post_blog)
#         db.session.commit()
#         return redirect(url_for('main.blogs'))

#     return render_template("index.html")