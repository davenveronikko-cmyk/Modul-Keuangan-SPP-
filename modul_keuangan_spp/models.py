from sqlalchemy import Column, Integer, String
from database import Base

class SPP(Base):
    __tablename__ = "spp"

    id = Column(Integer, primary_key=True, index=True)
    nama_siswa = Column(String, index=True)
    kelas = Column(String)
    bulan = Column(String)
    jumlah = Column(Integer)
    status = Column(String)
