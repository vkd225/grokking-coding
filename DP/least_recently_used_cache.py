class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dq = collections.deque()
        self.valueMap = {}

    def get(self, key: int) -> int:
        if key not in self.valueMap:
            return -1
        self.dq.remove(key)
        self.dq.append(key)

        return self.valueMap[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.valueMap:
            if len(self.dq) == self.cap:
                del self.valueMap[self.dq.popleft()]
        else:
            self.dq.remove(key)

        self.dq.append(key)
        self.valueMap[key] = value



#  using doubly linkedlist

class LinkedNode(object):

    def __init__(self, val, key):
        self.val = val     # 用来存放真正的缓存值
        self.key = key     # 反向指向字典中的一个key，用来进行反向删除操作
        self.next = None
        self.prev = None


class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.dummy = LinkedNode(0,0)
        self.head = self.dummy.next
        self.tail = self.dummy.next

    def remove_head_node(self):
        if not self.head:
            return
        prev = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del prev

    def append_new_node(self, new_node):
        """  add the new node to the tail end
        """
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next


    def unlink_cur_node(self, node):
        """ unlink current linked node
        """
        if self.head is node:
            self.head = node.next
            if node.next:
                node.next.prev = None
            return

        # removing the node from somewhere in the middle; update pointers
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev



    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        if node is not self.tail:
            self.unlink_cur_node(node)
            self.append_new_node(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.get(key)
            return


        if len(self.lookup) == self.capacity:
            # remove head node and correspond key
            self.lookup.pop(self.head.key)
            self.remove_head_node()

        # add new node and hash key
        new_node = LinkedNode(val=value, key=key)
        self.lookup[key] = new_node
        self.append_new_node(new_node)