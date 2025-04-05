import os
import argparse
import json
from te15 import generate_keys, encrypt, decrypt

def generate_keys_directory(keys_dir):
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
        keys = generate_keys()
        for i, key in enumerate(keys):
            with open(os.path.join(keys_dir, f'key_{i+1}.bin'), 'wb') as f:
                f.write(key)
        print(f"Generated {len(keys)} keys in '{keys_dir}' directory.")
    else:
        print(f"Keys directory '{keys_dir}' already exists.")

def check_keys(keys_dir):
    keys = []
    for i in range(1, 16):
        key_path = os.path.join(keys_dir, f'key_{i}.bin')
        if os.path.exists(key_path):
            with open(key_path, 'rb') as f:
                keys.append(f.read())
        else:
            print(f"Key file '{key_path}' does not exist.")
            return False
    print("All keys are present.")
    return True

def encrypt_data(keys_dir, to_use, mode):
    keys = []
    for i in range(1, 16):
        with open(os.path.join(keys_dir, f'key_{i}.bin'), 'rb') as f:
            keys.append(f.read())
    
    if mode == 'string':
        original = to_use.encode('utf-8')
        encrypted = encrypt(original, keys)
        print(f"Encrypted data: {encrypted.hex()}")
    elif mode == 'files':
        with open(to_use, 'rb') as f:
            original = f.read()
        encrypted = encrypt(original, keys)
        with open(to_use + '.enc', 'wb') as f:
            f.write(encrypted)
        print(f"Encrypted file saved as '{to_use}.enc'.")

def decrypt_data(keys_dir, to_use, mode):
    keys = []
    for i in range(1, 16):
        with open(os.path.join(keys_dir, f'key_{i}.bin'), 'rb') as f:
            keys.append(f.read())
    
    if mode == 'string':
        encrypted = bytes.fromhex(to_use)
        decrypted = decrypt(encrypted, keys)
        print(f"Decrypted data: {decrypted.decode('utf-8')}")
    elif mode == 'files':
        with open(to_use, 'rb') as f:
            encrypted = f.read()
        decrypted = decrypt(encrypted, keys)
        with open(to_use[:-4], 'wb') as f:
            f.write(decrypted)
        print(f"Decrypted file saved as '{to_use[:-4]}'.")

def main():
    parser = argparse.ArgumentParser(description='TE-15 Cryptography Module')
    parser.add_argument('--keys', type=str, help='Directory containing the keys')
    parser.add_argument('--op', type=str, choices=['encrypt', 'decrypt'], help='Operation type')
    parser.add_argument('--mode', type=str, choices=['files', 'string'], help='Mode of operation')
    parser.add_argument('--toUse', type=str, help='String to encrypt or path to the file to be encrypted')
    parser.add_argument('--generate-keys', type=str, help='Generate keys in the specified directory')
    parser.add_argument('--check-keys', action='store_true', help='Check the validity of the keys in the specified directory')

    args = parser.parse_args()

    if args.generate_keys:
        generate_keys_directory(args.generate_keys)
    elif args.check_keys and args.keys:
        check_keys(args.keys)
    elif args.op and args.keys and args.mode and args.toUse:
        if args.op == 'encrypt':
            encrypt_data(args.keys, args.toUse, args.mode)
        elif args.op == 'decrypt':
            decrypt_data(args.keys, args.toUse, args.mode)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()