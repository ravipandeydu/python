from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL for SQLite
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./zomato.db"

# Create an async engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Create a Base class for declarative class definitions
Base = declarative_base()


# Dependency to get a database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
