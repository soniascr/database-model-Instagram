from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120), unique=True, nullable=False)
    lastname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    posts = db.relationship('Post', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    #followers = db.relationship('Follower', backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    def get_all_users():
        return User.query.all()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    medias = db.relationship('Media', backref='post', lazy=True)
    comments = db.relationship('Comment', backref='post', lazy=True)
    
    def __repr__(self):
        return '<Post %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

    def get_all_posts():
         return Post.query.all()

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(80), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return '<Media %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url
            # do not serialize the password, its a security breach
        }

    def get_all_medias():
         return Media.query.all()

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(300), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text
            # do not serialize the password, its a security breach
        }

    def get_all_comments():
         return Comment.query.all()

    
# class Follower(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user_to_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return '<Follower %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             # do not serialize the password, its a security breach
#         }

#     def get_all_followers():
#          return Follower.query.all()