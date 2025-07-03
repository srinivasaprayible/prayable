from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user_route():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify(user.dict()), 201

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_route(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.dict())
