from sqlalchemy import func
from app.database import SessionLocal
from app.models import Property

def count_properties():
    db = SessionLocal()
    total = db.query(func.count(Property.id)).scalar()
    db.close()
    return total

def avg_price_by_state(limit=10):
    db = SessionLocal()
    result = (
        db.query(Property.state, func.avg(Property.price).label("avg_price"))
        .group_by(Property.state)
        .order_by(func.avg(Property.price).desc())
        .limit(limit)
        .all()
    )
    db.close()
    return result