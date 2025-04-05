from te15 import generate_keys, encrypt, decrypt
import os

def main():
    # Gerar ou carregar chaves
    if not os.path.exists('keys'):
        os.makedirs('keys')
        keys = generate_keys()
        for i, key in enumerate(keys):
            with open(f'keys/key_{i+1}.bin', 'wb') as f:
                f.write(key)
    else:
        keys = []
        for i in range(15):
            with open(f'keys/key_{i+1}.bin', 'rb') as f:
                keys.append(f.read())
    
    # Exemplo de uso
    original = b"Super Criptografia"
    
    # Criptografar
    encrypted = encrypt(original, keys)
    
    # Descriptografar
    decrypted = decrypt(encrypted, keys)
    
    print("Original:", original, '\n')
    print("Criptografado:", encrypted.hex(), '\n')
    print("Descriptografado:", decrypted, '\n')
    print("Sucesso?", decrypted == original)

if __name__ == "__main__":
    main()
