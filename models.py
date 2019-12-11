from db_config import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String(100), unique=True)
    translate = Column(String(200))
    transcription = Column(String(100))
    other_translations = Column(String(300))
    example = Column(Text)
    is_done = Column(Boolean, default=False)
    next_show = Column(DateTime)

    def __repr__(self):
        return f'<Word: {self.word} -> {self.translate}>'
