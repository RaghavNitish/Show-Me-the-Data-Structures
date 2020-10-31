import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, prev_hash):
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.data_hash = self.calc_hash()
        self.next = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    
    def __repr__(self):
        return "Timestamp: {}, Data: {}, Previous Hash: {}, Current Hash: {}".format(str(self.timestamp), str(self.data), str(self.prev_hash), str(self.data_hash))
    
class BlockChain(object):
    def __init__(self):
        self.head, self.tail = None, None
    
    def append(self, data):
        if data == "" or data == None:
            return
        else:
            if self.head == None:
                self.head = Block(datetime.datetime.utcnow(), data, 0)
                self.tail = self.head
            else:
                self.tail.next = Block(datetime.datetime.utcnow(), data, self.tail.data_hash)
                self.tail = self.tail.next
                
    def chain_list(self):
        current_node = self.head
        lst = list()
        
        while current_node:
            lst.append([current_node])
            current_node = current_node.next
        
        return lst

#-----------------TEST CASES---------------------
def main():
    # Test Case 1
    bl = BlockChain()
    data1 = "First Blockchain block"
    data2 = "Second Blockchain block"
    data3 = "Third Blockchain block"
    bl.append(data1)
    bl.append(data2)
    bl.append(data3)
    print(bl.chain_list()) 
    # prints block chain with the appropriate contents
    
    # Test Case 2
    bl1 = BlockChain()
    bl1.append("")
    bl1.append("")
    print(bl1.chain_list())  
    # prints empty block chain as there was no data passed
    
    #Test Case 3
    bl2 = BlockChain()
    bl2.append(None)
    bl2.append(None)
    print(bl2.chain_list())  
    # prints empty block chain as there was no data passed
    
if __name__ == "__main__":
    main()