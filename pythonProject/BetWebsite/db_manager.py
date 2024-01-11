from urllib.parse import quote_plus

from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy import create_engine
from contextlib import contextmanager
from BetWebsite.models import User


config = {
  'host': "34.165.35.208",
  'port': 5432,
  'dbuser': "pablo",
  'dbpassword': "Isr231203",
  'dbname': "postgres"}

DB_HOST = config.get('host')
DB_PORT = config.get('port')
DB_USER = config.get('dbuser')
DB_PASS = config.get('dbpassword')
DB_NAME = config.get('dbname')

#db_uri = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

engine_url = f'postgresql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine_url = engine_url % quote_plus(DB_PASS)

engine = create_engine(engine_url)
Session = sessionmaker(bind=engine)

@contextmanager
def db_manager():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_user_by_email(email):
    query = Query(User).with_entities(User).filter(User.email == email)
    with db_manager() as session:
        return session.execute(query).fetchone()



