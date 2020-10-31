class Node:
    def __init__(self, frequency, character=None):
        self.left = None
        self.right = None
        self.character = character
        self.frequency = frequency
        self.visited = False
        
class min_heap:
    def __init__(self, arr):
        self.arr = arr

    def min_heapify(self, j):
        left_index = 2*j + 1
        right_index = 2*j + 2
        smallest_index = j
        length = len(self.arr) - 1 
                
        if left_index <= length and self.arr[j].frequency > self.arr[left_index].frequency:
            smallest_index = left_index

        if right_index <= length and self.arr[smallest_index].frequency > self.arr[right_index].frequency:
            smallest_index = right_index
                    
        if smallest_index != j:
            self.arr[j], self.arr[smallest_index] = self.arr[smallest_index], self.arr[j]
            self.min_heapify(smallest_index)

    def build_min_heap(self):
        for j in reversed(range(len(self.arr) // 2)):
            self.min_heapify(j)
        
def huffman_encoding(data):
    #Corner Case 1
    if data == "" or data == None or len(data) == 1 or type(data) != str:
        return None, None
    
    #Variable declarations
    lst = list()
    frequency_dict = dict()

    #Step 1: generate the frequency table
    for character in data:
        if character not in frequency_dict:
            frequency_dict[character] = 1
        else:
            frequency_dict[character] += 1
    
    #Corner Case 2
    if len(frequency_dict) == 1:
        return None, None
    
    #Step 2: convert the frequency table into a list of nodes for min heap
    for key, value in frequency_dict.items():
        lst.append(Node(value, key))

    #Step 3: Perform steps 3 and 4 in the instruction set until 1 node is left
    min_heap_obj = min_heap(lst)

    while len(min_heap_obj.arr) != 1:
        min_heap_obj.build_min_heap()
        node1 = min_heap_obj.arr.pop(0)
        
        min_heap_obj.build_min_heap()
        node2 = min_heap_obj.arr.pop(0)
        
        new_node = Node(node1.frequency + node2.frequency)
        
        new_node.left = node1
        new_node.right = node2
        min_heap_obj.arr.append(new_node)

    #Step 4: At this point in time, our min heap array contains the tree required
    huffman_code_dict = code_generator(min_heap_obj.arr[0])
    
    #Step 5: We can now generate the huffman code for our string!
    final_str = ""
    for i in data:
        final_str += huffman_code_dict[i]
    
    return final_str, min_heap_obj.arr[0]
    
def code_generator(node):
    temp_str = ""
    code_dict = dict()
    root_frequency = node.frequency
    
    def code_generator_1(node):
        nonlocal temp_str
        nonlocal code_dict
        nonlocal root_frequency
        
        if node == None:
            return
        else:
            if node.left == None and node.right == None:
                code_dict[node.character] = temp_str
                temp_str = temp_str[0:-1]
                return
            
            if node.left:
                temp_str += "0"
                code_generator_1(node.left)
            
            if node.right:
                temp_str += "1"
                code_generator_1(node.right)
            
            temp_str = temp_str[0:-1]
                
    code_generator_1(node)
    
    return code_dict

def huffman_decoding(data, tree):
    #Addressing corner cases
    if data == None or data == "" or type(tree) != Node or type(data) != str or len(data) == 1:
        return None
    else:
        tree_root = tree
        traverse_node = tree
        decoded_str = ""
        
        for i in data:
            if i == "0":
                if traverse_node.left:
                    traverse_node = traverse_node.left
                    
                    if traverse_node.left == None and traverse_node.right == None:
                        decoded_str += traverse_node.character
                        traverse_node = tree_root
                    
            elif i == "1":
                if traverse_node.right:
                    traverse_node = traverse_node.right
                    
                    if traverse_node.left == None and traverse_node.right == None:
                        decoded_str += traverse_node.character
                        traverse_node = tree_root
        
        return decoded_str

#-----------------TEST CASES---------------------
if __name__ == "__main__":
    
    print("TEST CASE 1")
    a_great_sentence = "The bird is the word"
    print("The data being encoded is:", a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("This is the encoded data:", encoded_data)
    #encoded_data is equal to the string, 1000001010110101001111101111110011100111010110010101100001000011101111
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print("This is the decoded data:", decoded_data)
    #decoded_data is equal to the string, The bird is the word


    print("\nTEST CASE 2")
    a_great_sentence = ""
    print("The data being encoded is:", a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("This is the encoded data:", encoded_data)
    #encoded_data is equal to None
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print("This is the decoded data:", decoded_data)
    #decoded_data is equal to None
    
    
    print("\nTEST CASE 3")
    a_great_sentence = None
    print("The data being encoded is:", a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("This is the encoded data:", encoded_data)
    #encoded_data is equal to None
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print("This is the decoded data:", decoded_data)
    #decoded_data is equal to None
    
    
    print("\nTEST CASE 4")
    a_great_sentence = "d"
    print("The data being encoded is:", a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("This is the encoded data:", encoded_data)
    #encoded_data is equal to None
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print("This is the decoded data:", decoded_data)
    #decoded_data is equal to None