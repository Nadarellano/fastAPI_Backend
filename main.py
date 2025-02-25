from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
import datetime
import jwt

# Configuración de seguridad para generar tokens JWT
SECRET_KEY = "secret123"
ALGORITHM = "HS256"

app = FastAPI()

# Datos simulados para razas y perros
breeds_data = [
    {"id": 1, "name": "Labrador"},
    {"id": 2, "name": "Bulldog"},
    {"id": 3, "name": "Beagle"},
    {"id": 4, "name": "Golden Retriever"},
]

dogs_data = [
    {"id": 1, "name": "Max", "breed": "Labrador"},
    {"id": 2, "name": "Rocky", "breed": "Bulldog"},
    {"id": 3, "name": "Buddy", "breed": "Beagle"},
    {"id": 4, "name": "Charlie", "breed": "Golden Retriever"},
    {"id": 5, "name": "Max", "breed": "Labrador"},
]

# Modelo para autenticación 
class AuthRequest(BaseModel):
    email: str
    password: str

# Modelo de respuesta para /answer/
class AnswerRequest(BaseModel):
    totalBreeds: int
    totalDogs: int
    commonBreed: str
    commonDogName: str

# Definimos un esquema de autenticación OAuth2 con "Bearer Token" 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/") #endpoint donde los clientes obtienen un token JWT.

# Función para crear el token de autorización
# Función para generar un token JWT
def create_jwt_token(email: str):
    expiration = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    token = jwt.encode({"sub": email, "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para Autenticación y obtención de token
@app.post("/api/v1/auth/")
def authenticate(auth_data: AuthRequest):
    if auth_data.email == "admin@example.com" and auth_data.password == "1234":
        token = create_jwt_token(auth_data.email)
        return {"token": token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Función para obtener lista de razas
@app.get("/api/v1/breeds/")
def get_breeds(token: str = Depends(oauth2_scheme)):
    return {
        "count": len(breeds_data),
        "next": "http://example.com",
        "previous": "http://example.com",
        "results": breeds_data
    }

# Función para obtener lista de perros con formato correcto
@app.get("/api/v1/dogs/")
def get_dogs(token: str = Depends(oauth2_scheme)):
    return {
        "count": len(dogs_data),
        "next": "http://example.com",
        "previous": "http://example.com",
        "results": dogs_data
    }

# Función para procesar datos y enviar respuestas
@app.post("/api/v1/answer/")
def send_answer(answer: AnswerRequest, token: str = Depends(oauth2_scheme)):
    return {
        "totalBreeds": answer.totalBreeds,
        "totalDogs": answer.totalDogs,
        "commonBreed": answer.commonBreed,
        "commonDogName": answer.commonDogName
    }
