from typing import List, Optional

from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/api/v1/vote", tags=["Votes"])


@router.post('/', status_code=status .HTTP_201_CREATED)
def vote_post(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # print(current_user)
    post = db.query(mode.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found.')
    query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    vote_found = query.first()
    if (vote.dir == 1):
        if vote_found:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f'user with id: {current_user.id} has already voted on post with id: {vote.post_id}')
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        # db.refresh(new_vote)
        return {"message": "successfully added a vote"}
    else:
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'vote does not exist')
        query.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
