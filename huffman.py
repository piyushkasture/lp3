import heapq
from collections import defaultdict, Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def build_huffman_codes(root, current_code, huffman_codes):
    if root is not None:
        if root.char is not None:
            huffman_codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + '0', huffman_codes)
        build_huffman_codes(root.right, current_code + '1', huffman_codes)


def huffman_encoding(data):
    if not data:
        return None, None

    freq_dict = dict(Counter(data))
    root = build_huffman_tree(freq_dict)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, root


def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return None

    decoded_data = ""
    current_node = root
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data


# Example usage
if __name__ == "__main__":
    data = "this is an example for huffman encoding"

    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded data: {decoded_data}")