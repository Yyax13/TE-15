import os
import random

def generate_key(key_size=15360):
    return bytes([random.getrandbits(8) for _ in range(key_size)])

def generate_keys(num_keys=15):
    return [generate_key() for _ in range(num_keys)]

def pad_data(data, block_size):
    padding_length = block_size - (len(data) % block_size) or block_size
    return data + bytes([padding_length] * padding_length)

def unpad_data(data):
    return data[:-data[-1]]

def xor_with_key(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def rotate_bits(block, key):
    rotated = []
    for i, b in enumerate(block):
        shift = key[i % len(key)] % 7 + 1
        rotated.append(((b << shift) | (b >> (8 - shift))) & 0xFF)
    return bytes(rotated)

def unrotate_bits(block, key):
    unrotated = []
    for i, b in enumerate(block):
        shift = key[i % len(key)] % 7 + 1
        unrotated.append(((b >> shift) | (b << (8 - shift))) & 0xFF)
    return bytes(unrotated)

def generate_sbox(key):
    sbox = list(range(256))
    for i in range(256):
        key_index = i % len(key)
        swap_with = (i + key[key_index]) % 256
        sbox[i], sbox[swap_with] = sbox[swap_with], sbox[i]
    return sbox

def generate_inv_sbox(key):
    sbox = generate_sbox(key)
    return [sbox.index(i) for i in range(256)]

def substitute(block, key):
    return bytes([generate_sbox(key)[b] for b in block])

def inverse_substitute(block, key):
    return bytes([generate_inv_sbox(key)[b] for b in block])

def generate_permutation_order(key, block_size):
    order = list(range(block_size))
    for i in range(block_size):
        key_index = i % len(key)
        j = (i + key[key_index]) % block_size
        order[i], order[j] = order[j], order[i]
    return order

def permute(block, key):
    order = generate_permutation_order(key, len(block))
    return bytes([block[i] for i in order])

def inverse_permute(block, key):
    order = generate_permutation_order(key, len(block))
    return bytes([block[order.index(i)] for i in range(len(block))])

def encrypt_layer(data, key):
    block_size = 16
    padded = pad_data(data, block_size)
    encrypted = b''
    for i in range(0, len(padded), block_size):
        block = padded[i:i+block_size]
        block = xor_with_key(block, key)
        block = rotate_bits(block, key)
        block = substitute(block, key)
        block = permute(block, key)
        encrypted += block
    return encrypted

def decrypt_layer(data, key):
    block_size = 16
    decrypted = b''
    for i in range(0, len(data), block_size):
        block = data[i:i+block_size]
        block = inverse_permute(block, key)
        block = inverse_substitute(block, key)
        block = unrotate_bits(block, key)
        block = xor_with_key(block, key)
        decrypted += block
    return decrypted

def encrypt(data, keys):
    for key in keys:
        data = encrypt_layer(data, key)
    return data

def decrypt(data, keys):
    for key in reversed(keys):
        data = decrypt_layer(data, key)
    return unpad_data(data)
