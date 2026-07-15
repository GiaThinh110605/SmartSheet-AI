import bcrypt
import bcrypt
def get_password_hash(password: str) -> str:
    password_bytes = password.encode("utf-8")
    
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_bytes, salt)
    return hashed_pwd
    