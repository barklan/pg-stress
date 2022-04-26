import sqlalchemy
from sqlalchemy import orm
import sqlalchemy as sa
from collections import abc
import faker

import fastapi as fa

fake = faker.Faker()

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

@app.get("/create")
def create(
    db: orm.Session = fa.Depends(get_db),
):
    db.execute(sa.text("""
    create table if not exists book (
        title varchar(100) not null
    );
    """))

@app.get("/select")
def select(
    db: orm.Session = fa.Depends(get_db),
):
    db.execute(sa.text("select * from book;"))
    return {"status": "ok"}

@app.get("/insert")
def insert(
    db: orm.Session = fa.Depends(get_db),
):
    db.execute(sa.text("insert into book (title) values ('{}')".format(fake.name())))
    return {"status": "ok"}
