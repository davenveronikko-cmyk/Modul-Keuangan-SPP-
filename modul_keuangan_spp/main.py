from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Modul Keuangan SPP")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/spp/", response_model=schemas.SPPResponse)
def tambah_spp(spp: schemas.SPPCreate, db: Session = Depends(get_db)):
    return crud.create_spp(db, spp)

@app.get("/spp/", response_model=list[schemas.SPPResponse])
def lihat_spp(db: Session = Depends(get_db)):
    return crud.get_all_spp(db)
