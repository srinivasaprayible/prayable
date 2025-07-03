from sqlmodel import select
from app.db.session import get_session
from app.models.user import User

class UserService:
    @staticmethod
    def create_user(data):
        session = next(get_session())
        user = User(name=data["name"], email=data["email"])
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get_user_by_id(user_id: int):
        session = next(get_session())
        return session.exec(select(User).where(User.id == user_id)).first()
