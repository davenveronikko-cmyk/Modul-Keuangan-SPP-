from sqlalchemy.orm import Session
import models, schemas

def create_spp(db: Session, spp: schemas.SPPCreate):
    db_spp = models.SPP(**spp.dict())
    db.add(db_spp)
    db.commit()
    db.refresh(db_spp)
    return db_spp

def get_all_spp(db: Session):
    return db.query(models.SPP).all()
