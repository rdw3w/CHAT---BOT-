import hashlib
import bcrypt

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def hash_password_sha256(password):
    """Alternative SHA256 hashing"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password_sha256(password, hashed):
    """Verify SHA256 password"""
    return hashlib.sha256(password.encode()).hexdigest() == hashed