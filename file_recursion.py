import os

def find_files(suffix, path):
    paths = list()
    
    #Corner Case 1: If the suffix or path is None type, the program returns None
    if type(suffix) != str or type(path) != str:
        return None
    
    #Corner Case 2: If the path is neither a directory nor a file, the program returns None
    if os.path.isdir(path) == False and os.path.isfile(path) == False:
        return None
    
    #Corner Case 3: If the path is a path to a file, check the appropriate conditions
    if os.path.isfile(path) == True:
        if path.endswith(suffix) == True:
            paths.append(path)
            return paths
        else:
            return None
    
    #For all other cases, the following code gets executed
    def find_files_1(suffix, path):
        nonlocal paths
        
        for file in os.listdir(path):
            temp_str = path + "/" + file
            
            if os.path.isdir(temp_str):
                find_files_1(suffix, temp_str)
            
            if temp_str.endswith(suffix) == True:
                paths.append(temp_str)
        
    find_files_1(suffix, path)
    return paths

#-----------------TEST CASES---------------------
print(find_files("", ""))
# prints None

print(find_files(None, None))
# prints None

print(find_files(1, 2))
# prints None
