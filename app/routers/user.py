from .. import models, schemas, utils
from ..database import get_db
from fastapi import Body, Depends, FastAPI, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user_exist = db.query(models.User) \
        .filter(models.User.email == user.email) \
        .first()

    if user_exist != None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'email: {user.email} has been used.')

    # hash the password
    user.password = utils.hash(user.password)

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'uid: {id} does not exist')

    return user
