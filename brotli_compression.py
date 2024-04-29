import brotli
import os

def brotli_compress(data):
    """Compress data using Brotli algorithm."""
    compressed_data = brotli.compress(data)
    return compressed_data

def brotli_decompress(compressed_data):
    """Decompress Brotli compressed data."""
    decompressed_data = brotli.decompress(compressed_data)
    return decompressed_data

def load_data(filepath):
    """Load data from a file into a byte array."""
    with open(filepath, 'rb') as file:
        data = file.read()
    return data

def save_compressed_data(filepath, compressed_data):
    """Save compressed data to a file."""
    with open(filepath, 'wb') as file:
        file.write(compressed_data)

# Example usage:
filepath = 'C:/Users/vinay/OneDrive/Pictures/Screenshots/jpg-vs-jpeg.jpg'
data = load_data(filepath)
compressed_data = brotli_compress(data)
save_compressed_data('compressed_file.br', compressed_data)

compressed_size_kb = len(compressed_data) / 1024
original_file_size = os.path.getsize(filepath) / 1024
print(f"Original file size: {original_file_size:.2f} KB")
print(f"Compressed file size: {compressed_size_kb:.2f} KB")