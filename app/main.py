from flask import Flask
from sqlmodel import SQLModel
from app.db.session import engine
from app.routes.user_routes import user_bp
from app.config import settings

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app

def init_db():
    SQLModel.metadata.create_all(engine)

app = create_app()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
