from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, Column, Computed, Date, DateTime, Enum, Float, \
    ForeignKey, Index, Integer, JSON, Numeric, String, Table, Text, text, func
from sqlalchemy.dialects.postgresql import JSONB, OID, TIMESTAMP, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    fullName = Column(String(255))
    bettor = relationship('Bettor', uselist=False, back_populates='user')


class Bettor(Base):
    __tablename__ = 'bettors'

    name = Column(String(255))
    bets = relationship('Bet', back_populates='bettor')
    user = relationship('User', back_populates='bettor')
    bettor_id = Column(Integer, ForeignKey('user.id'), primary_key=True)


# Define the 'Bet' class
class Bet(Base):
    __tablename__ = 'bets'

    betid = Column(Integer, primary_key=True)
    round = Column(Integer)
    date = Column(DateTime(timezone=True), default=func.now())  # the date and time of the bet
    match_id = Column(Integer)
    hometeam = Column(String(255))
    awayteam = Column(String(255))
    result_bet = Column(String(255))
    goals_bet = Column(String(255))
    result_score = Column(Integer, default=0)
    goals_score = Column(Integer, default=0)
    round_score = Column(Integer, default=0)

    bettor_id = Column(Integer, ForeignKey('bettors.bettor_id'))
    bettor = relationship('Bettor', back_populates='bets')
