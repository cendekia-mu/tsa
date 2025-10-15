import sqlalchemy as sa
from .meta import Base


class WikiModel(Base):
    __tablename__ = 'wiki'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    body = sa.Column(sa.Text, nullable=False)