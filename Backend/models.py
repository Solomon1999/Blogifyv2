from app import db
from sqlalchemy import Column, Integer, String, Text, Table
from flask_login import UserMixin
from app import login_managers

@login_managers.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True )


class Users(UserMixin, Base):
    __tablename__ = 'users'
    full_name = Column(String(100))
    username = Column(String(100), unique=True)
    email = Column(Text(), unique=True)
    password = Column(String(100))
    role = Column(String(50))


# categories = Table('categories',
#     Column('category_id', Integer, db.ForeignKey('category.id'), primary_key=True),
#     Column('blog_id', Integer, db.ForeignKey('blogs.id'), primary_key=True)
# )

class Blogs(Base):
    __tablename__ = 'blogs'
    author = Column(String(100))
    excerpt = Column(Text())
    title = Column(Text())
    category = Column(Text())
    # tags = Column(Text())
    body = Column(Text())
    comments = db.relationship('Comments', backref='blogs', lazy=True)
    # categories = db.relationship('Category', secondary=categories, lazy='subquery', backref=db.backref('blogs', lazy=True))

class Comments(Base):
    __tablename__ = 'comments'
    username = Column(String(100))
    email = Column(Text())
    body = Column(Text())
    blog_id = Column(Integer, db.ForeignKey('blogs.id'), nullable=False)
    likes = db.relationship('Likes', backref='comments', lazy=True)

class Likes(Base):
    __tablename__ = 'likes'
    username = Column(String(100))
    likes_id = Column(Integer, db.ForeignKey('comments.id'), nullable=False)

# class Category(Base):
#     __tablename__ = 'category'
#     name = Column(Text())
