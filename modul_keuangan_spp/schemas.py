from pydantic import BaseModel

class SPPBase(BaseModel):
    nama_siswa: str
    kelas: str
    bulan: str
    jumlah: int
    status: str

class SPPCreate(SPPBase):
    pass

class SPPResponse(SPPBase):
    id: int

    class Config:
        orm_mode = True
