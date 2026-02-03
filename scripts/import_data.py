import pandas as pd
from app.database import SessionLocal
from app.models import Property
from sqlalchemy.exc import SQLAlchemyError

def import_sample(csv_path="data/real_estate_sample.csv"):
    df = pd.read_csv(csv_path)
    df = df.where(pd.notnull(df), None)  # convert NaN -> None for SQLAlchemy
    db = SessionLocal()
    try:
        for _, r in df.iterrows():
            p = Property(
                city=r.get("city"),
                state=r.get("state"),
                zip_code=str(r.get("zip_code")) if r.get("zip_code") is not None else None,
                status=r.get("status"),
                price=float(r.get("price")) if r.get("price") else None,
                bed=float(r.get("bed")) if r.get("bed") else None,
                bath=float(r.get("bath")) if r.get("bath") else None,
                acre_lot=float(r.get("acre_lot")) if r.get("acre_lot") else None,
                house_size=float(r.get("house_size")) if r.get("house_size") else None,
            )
            db.add(p)
        db.commit()
        print("Imported sample into DB")
    except SQLAlchemyError as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import_sample()