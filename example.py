from te15 import generate_keys, encrypt, decrypt
import os
from yollor import t, c

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
    original = input(f'{t.hashtag_yellow} {c.cyan("Texto a ser criptografado")}: ').encode('utf-8')
    os.system( 'cls' if os.system == 'nt' else 'clear')
    
    # Criptografar
    encrypted = encrypt(original, keys)
    
    # Descriptografar
    decrypted = decrypt(encrypted, keys)
    
    print(f"{t.hashtag_yellow} {c.cyan('Original:')}", original, '\n')
    print(f"{t.hashtag_yellow} {c.cyan('Criptografado:')}", encrypted.hex(), '\n')
    print(f"{t.hashtag_yellow} {c.cyan('Decriptografado:')}", decrypted, '\n')
    print(f"{t.quest_red} {c.yellow('Sucesso?')}", decrypted == original)

if __name__ == "__main__":
    main()