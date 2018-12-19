from sqlalchemy import create_engine
from sqlalchemy import Column, String, MetaData, Integer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.db_config import DatabaseConfig

db_string = DatabaseConfig.db_string
db = create_engine(db_string)
meta = MetaData(db)
Base = declarative_base()
Session = sessionmaker(db)
session = Session()


def create_all_table():
    Base.metadata.create_all(db)
    return True


class File(Base):
    __tablename__ = 'file'
    file_id = Column(String, primary_key=True)
    peer_id = Column(Integer, nullable=False)
    access_hash = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)

    def __init__(self, peer_id, file_id, access_hash, file_size):
        self.file_id = file_id
        self.peer_id = peer_id
        self.access_hash = access_hash
        self.file_size = file_size

    def __repr__(self):
        return "<File(file_id='%s',peer_id='%i',access_hash='%s', file_size='%i')>" % (
            self.file_id, self.peer_id, self.access_hash, self.file_size)


def insert_to_files(file):
    try:
        session.add(file)
        session.commit()
        return file
    except SQLAlchemyError as e:
        print(e.args)
        return False


def get_file_row(file_id, peer_id):
    try:
        return session.query(File).filter(File.file_id == file_id, File.peer_id == peer_id).one_or_none()
    except SQLAlchemyError as e:
        print(e.args)
        return False
