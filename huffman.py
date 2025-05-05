import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    
    priority_queue = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        heapq.heappush(priority_queue, internal)
    
    return priority_queue[0]

def generate_codes(root):
    codes = {}
    
    def traverse(node, code):
        if node:
            if node.char:
                codes[node.char] = code
                return
            
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    
    traverse(root, "")
    return codes

def huffman_encoding(text):
    if not text:
        return "", None
    
    root = build_huffman_tree(text)
    
    codes = generate_codes(root)
    
    encoded_text = ''.join(codes[char] for char in text)
    
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    if not encoded_text or not root:
        return ""
    
    decoded_text = []
    current = root
    
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
            
        if current.char:
            decoded_text.append(current.char)
            current = root
    
    return ''.join(decoded_text)

if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    print("Original text:", text)
    
    encoded_text, tree = huffman_encoding(text)
    print("\nEncoded text:", encoded_text)
    
    original_size = len(text) * 8
    compressed_size = len(encoded_text)
    print(f"Compression ratio: {compressed_size}/{original_size} = {compressed_size/original_size:.2f}")
    
    codes = generate_codes(tree)
    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    
    decoded_text = huffman_decoding(encoded_text, tree)
    print("\nDecoded text:", decoded_text)
    
    print("\nOriginal and decoded texts match:", text == decoded_text)