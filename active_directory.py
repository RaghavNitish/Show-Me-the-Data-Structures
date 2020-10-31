class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if user == None or user == "" or type(group) != Group:
        return None
    
    if user in group.get_users():
        return True
    else:
        found = False
        def is_user_in_group_1(user, group):
            nonlocal found
            
            if user in group.get_users():
                found = True
                return 
            else:
                if group.get_groups():
                    for element in group.get_groups():
                        is_user_in_group_1(user, element)
            return found
        return is_user_in_group_1(user, group)

#-----------------TEST CASES---------------------
parent = Group("parent")
parent.add_user("Name100")

child = Group("child")
child.add_user("Name12")
child.add_user("Name13")

sub_child = Group("sub_child")
sub_child.add_user("sub_child_user")
sub_child.add_user("sub_child_user_1")

small_child = Group("small_child")
small_child.add_user("Name1")

small_child_1 = Group("small_child_1")
small_child_1.add_user("Name2")

sub_child.add_group(small_child)
sub_child.add_group(small_child_1)
child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("Name100", parent))
# prints True

print(is_user_in_group("harry", None))
# prints None

print(is_user_in_group("Name1", 123))
# prints None

