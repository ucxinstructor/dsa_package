import unittest

from dsa.huffman import build_frequency_table, build_huffman_tree, build_huffman_dictionary, huffman_encode, bitstring_to_bytes
from dsa.huffman import huffman_decode, bytes_to_bitstring

class TestHuffman(unittest.TestCase):
    def test_create(self):
        message = "a man plan a canal panama"
        print(message)
        freq_table = build_frequency_table(message)
        print(freq_table)
        tree = build_huffman_tree(freq_table)
        hd = build_huffman_dictionary(tree)

        encoded_message = huffman_encode(message, hd)
        print(encoded_message)
        encoded_message_length = len(encoded_message)
        print(f"Encoded Message length in bits: {encoded_message_length}")
        
        bytes_message = bitstring_to_bytes(encoded_message)
        print(bytes_message)

        bitlength = 8 - (encoded_message_length % 8)
        bitlength = encoded_message_length % 8
        bits_message = bytes_to_bitstring(bytes_message, bitlength=bitlength)

        decoded_message = huffman_decode(bits_message, tree)
        print(decoded_message)

if __name__ == '__main__':
    unittest.main()
