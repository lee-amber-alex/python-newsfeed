from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, column_property
from sqlalchemy import select, func


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # ForeignKey references the users table.
    user_id = Column(Integer, ForeignKey("users.id"))
    # Python built-in datetime module generates timestamps.
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )
   

    user = relationship("User")
    # will delete associated comments if post is deleted.
    comments = relationship("Comment", cascade="all, delete")
