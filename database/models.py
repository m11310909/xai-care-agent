from sqlalchemy import Column, Integer, String, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Interaction(Base):
    __tablename__ = 'interactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    context = Column(JSON)
    prediction = Column(String)
    trust_score = Column(Integer, default=0)
    state = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    interaction_id = Column(Integer)
    understood = Column(Boolean)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class TrustResponse(Base):
    __tablename__ = 'trust_responses'
    id = Column(Integer, primary_key=True)
    interaction_id = Column(Integer)
    score = Column(Integer)
    qtype = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
