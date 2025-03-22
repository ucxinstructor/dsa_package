import unittest

from dsa.huffman import build_frequency_table, build_huffman_tree, build_huffman_dictionary, huffman_encode, bitstring_to_bytes
from dsa.huffman import huffman_decode, bytes_to_bitstring

class TestHuffman(unittest.TestCase):
    def test_create(self):
        message = "a man plan a canal panama"

        pq = build_frequency_table(message)
        self.assertEqual(len(pq), 7)
        tree = build_huffman_tree(pq)

        hd = build_huffman_dictionary(tree.root)
        encoded_message = huffman_encode(message, hd)

        self.assertEqual(len(encoded_message), 64)
        self.assertEqual(encoded_message, "1101101011000110111001110001110110001100111001011011110011101011")
        encoded_message_length = len(encoded_message)
        
        bytes_message = bitstring_to_bytes(encoded_message)
        self.assertEqual(bytes_message, b'\xda\xc6\xe7\x1d\x8c\xe5\xbc\xeb')
        bitlength = 8 - (encoded_message_length % 8)
        bitlength = encoded_message_length % 8
        self.assertEqual(bitlength, 0)
        bits_message = bytes_to_bitstring(bytes_message, bitlength=bitlength)

        decoded_message = huffman_decode(bits_message, tree)
        self.assertEqual(decoded_message, message)

    def test_encode_decode2(self):
        message = "123456789123456789123456789"

        pq = build_frequency_table(message)
        tree = build_huffman_tree(pq)

        hd = build_huffman_dictionary(tree.root)
        encoded_message = huffman_encode(message, hd)

        encoded_message_length = len(encoded_message)
        self.assertEqual(encoded_message_length, 87)
        bytes_message = bitstring_to_bytes(encoded_message)
        self.assertEqual(bytes_message, b'\xef\x059wx)\xcb\xbb\xc1N.')

        bitlength = 8 - (encoded_message_length % 8)
        bitlength = encoded_message_length % 8
        self.assertEqual(bitlength, 7)
        bits_message = bytes_to_bitstring(bytes_message, bitlength=bitlength)

        decoded_message = huffman_decode(bits_message, tree)
        self.assertEqual(decoded_message, message)


    def test_encode_decode3(self):
        message = "The quick brown fox jumps over the lazy dog."

        pq = build_frequency_table(message)
        tree = build_huffman_tree(pq)

        hd = build_huffman_dictionary(tree.root)
        encoded_message = huffman_encode(message, hd)

        encoded_message_length = len(encoded_message)
        
        bytes_message = bitstring_to_bytes(encoded_message)

        bitlength = 8 - (encoded_message_length % 8)
        bitlength = encoded_message_length % 8
        bits_message = bytes_to_bitstring(bytes_message, bitlength=bitlength)

        decoded_message = huffman_decode(bits_message, tree)
        self.assertEqual(decoded_message, message)

if __name__ == '__main__':
    unittest.main()
