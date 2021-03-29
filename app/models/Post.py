from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id")) #ForeignKey references the users table.
    created_at = Column(DateTime, default=datetime.now) #Python built-in datetime module generates timestamps.
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship("User")
    comments = relationship("Comment", cascade="all, delete") #will delete associated comments if post is deleted.
