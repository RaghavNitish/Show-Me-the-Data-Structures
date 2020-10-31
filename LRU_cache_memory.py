class LRU_Cache(object):
    def __init__(self, capacity=5):
        self.key_value = {}
        self.capacity = capacity

    def get(self, key):
        #Addressing corner case
        if type(self.capacity) != int or self.capacity == 0:
            print("Cannot search for the given key due to invalid cache capacity.")
            return
        
        #Addressing corner cases
        if key == None or key == "":
            return None
        else:
            value = self.key_value.get(key)
            
            if value == None:
                return -1
            else:
                temp = self.key_value.pop(key)
                self.key_value[key] = temp
                return value

    def set(self, key, value):
        #Addressing corner case
        if type(self.capacity) != int or self.capacity == 0:
            print("Cannot insert key value pair due to invalid cache capacity.")
            return
        
        #Addressing corner cases
        if key != None and value != None and key != "" and value != "":
            if len(self.key_value) != self.capacity:
                self.key_value[key] = value
            else:
                self.key_value.pop(list(self.key_value.keys())[0])
                self.key_value[key] = value

#-----------------TEST CASES---------------------
print("TEST CASE 1")
our_cache = LRU_Cache(4)

our_cache.set(1, 500);
our_cache.set(2, 1000);
our_cache.set("", "");
our_cache.set(4, None);
our_cache.set(None, None)
our_cache.set(456, 789)
print(our_cache.get(1))       
# prints 500

print(our_cache.get(2))      
# prints 1000

print(our_cache.get(""))      
# prints None

print(our_cache.get(None))    
# prints None

print(our_cache.get(4))       
# prints -1

our_cache.set(12, 13) 
our_cache.set(14, 15)
our_cache.set(123, 456)
print(our_cache.get(456))    
# prints -1

print(our_cache.get(1))      
# prints -1

print("\nTEST CASE 2")
our_cache = LRU_Cache(None)

our_cache.set(4, 400)
# prints 'Cannot insert key value pair due to invalid cache capacity.'

our_cache.get(4)
# prints 'Cannot search for the given key due to invalid cache capacity.'

print("\nTEST CASE 3")
our_cache = LRU_Cache(0)

our_cache.set(3, 33)
# prints 'Cannot insert key value pair due to invalid cache capacity.'

our_cache.get(3)
# prints 'Cannot search for the given key due to invalid cache capacity.'

