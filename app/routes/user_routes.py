from flask import Blueprint, jsonify, request
from app.model import User,db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    print(request)

    if not data or not 'username' in data or not 'email' in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    
    if not data or not 'username' in data or not 'email' in data:
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    user.username = data['username']
    user.email = data['email']
    db.session.commit()

    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200
