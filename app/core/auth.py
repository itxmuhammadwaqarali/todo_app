from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from uuid import UUID

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    # bcrypt only supports up to 72 bytes
    return pwd_context.hash(password[:72])

def verify_password(plain, hashed):
    # bcrypt only supports up to 72 bytes
    return pwd_context.verify(plain[:72], hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    # Convert any UUID objects to strings for JSON serialization
    for key, value in to_encode.items():
        if isinstance(value, UUID):
            to_encode[key] = str(value)
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None