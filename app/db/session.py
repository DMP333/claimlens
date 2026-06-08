from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


# Connection pool to Postgres. Created at import; connects lazily on first query.
# sets up the connection to database, but doens't actaully enable connection, that's doen by asyncsessionlocal
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)

# Factory for short-lived per-request sessions.
#session: one short conversation with the database
#running this will hand me the fresh new session
#notice we are writing an "object" and we are writing that object to database when we commit
#when we commit all we are saying is that let's keep this object in our memory so we can utilize them
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Parent class for all table models; the registry create-all uses on startup.
#yes we have one database, but we will have multiple tables and this table will come from inheriting this
#inehriting classes creates new table, which will all bootup thorugh here in the startup
class Base(DeclarativeBase):
    pass


# Request-scoped session dependency (the background job opens its own, see service).
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


#my understanding of this file
#Postgres: database
#session.py is gonna talk to database using sql alchemy
#this file is not a database, it is a pipeline to communicate with the database