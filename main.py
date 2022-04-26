import sqlalchemy
from sqlalchemy import orm
import sqlalchemy as sa
from collections import abc

import fastapi as fa


engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost:5432/postgres", pool_pre_ping=True, future=True)  # type: ignore
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=True, bind=engine, future=True)

def get_db() -> abc.Generator[orm.Session, None, None]:
    try:
        db = SessionLocal()
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()


app = fa.FastAPI()

@app.get("/")
def read_root(
    db: orm.Session = fa.Depends(get_db),
):
    users = db.execute(sa.select(sa.text("user"))).scalars().all()
    print(users)
