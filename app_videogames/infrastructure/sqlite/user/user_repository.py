from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app_videogames.domain.user import User, UserRepository
from app_videogames.usecase.user import UserCommandUseCaseUnitOfWork

from .user_dto import UserDTO


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, idUser: int) -> Optional[User]:
        try:
            user_dto = self.session.query(UserDTO).filter_by(idUser=idUser).one()
        except NoResultFound:
            return None
        except:
            raise
        return user_dto.to_entity()

    def find_by_email(self, email: str) -> Optional[User]:
        try:
            user_dto = self.session.query(UserDTO).filter_by(email=email).one()
        except NoResultFound:
            return None
        except:
            raise
        return user_dto.to_entity()

    def create(self, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            self.session.add(user_dto)
        except:
            raise

    def update(self, user: User):
        user_dto = UserDTO.from_entity(user)
        try:
            _user = self.session.query(UserDTO).filter_by(idUser=user_dto.idUser).one()
            _user.username = user_dto.username
            _user.password = user_dto.password
        except:
            raise

    def delete_by_id(self, idUser: int):
        try:
            self.session.query(UserDTO).filter_by(idUser=idUser).delete()
        except:
            raise

class UserCommandUseCaseUnitOfWorkImpl(UserCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        user_repository: UserRepository,
    ):
        self.session: Session = session
        self.user_repository: UserRepository = user_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
