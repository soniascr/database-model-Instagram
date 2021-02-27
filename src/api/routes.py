"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Post, Media, Comment #Follower
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['GET'])
def handle_users():

    users = User.get_all_users()
    all_users = list(map(lambda user: user.serialize(), users))

    return jsonify(all_users), 200

@api.route('/posts', methods=['GET'])
def handle_posts():

    posts = Post.get_all_posts()
    all_posts = list(map(lambda post: post.serialize(), posts))

    return jsonify(all_posts), 200

@api.route('/medias', methods=['GET'])
def handle_medias():

    medias = Media.get_all_medias()
    all_medias = list(map(lambda media: media.serialize(), medias))

    return jsonify(all_medias), 200

@api.route('/comments', methods=['GET'])
def handle_comments():

    comments = Comment.get_all_comments()
    all_comments = list(map(lambda comment: comment.serialize(), comments))

    return jsonify(all_comments), 200

# @api.route('/followers', methods=['GET'])
# def handle_followers():

#     followers = Follower.get_all_followers()
#     all_followers = list(map(lambda follower: follower.serialize(), followers))

#     return jsonify(all_followers), 200