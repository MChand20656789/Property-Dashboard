from app.database import engine, Base
from app.models import Property

def init_db():
    Base.metadata.create_all(bind=engine)
    print("DB initialized")

if __name__ == "__main__":
    init_db()