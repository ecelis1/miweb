import hashlib

def hash_password(password):
    """Función para generar el hash de una contraseña."""
    hash_obj = hashlib.sha256(password.encode())  # Usando SHA-256 como ejemplo de algoritmo de hash
    return hash_obj.hexdigest()  # Devuelve el hash en formato hexadecimal
