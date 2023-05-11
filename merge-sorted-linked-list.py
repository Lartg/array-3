#!python


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self, items=None):
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)                

    def __repr__(self):
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        items = []
        node = self.head
        while node is not None:  
            items.append(node.data)  
            node = node.next 
   
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty() == False:
            node = self.head
            count = 1
            while node.next is not None:
                node = node.next
                count += 1
          
            return count
        else:
            return 0



    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def prepend(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def find(self, item):
        if self.is_empty():
            return False
        else:
            if self.tail.data == item:
                return True
            node = self.head
            while node.next != None:
                if node.data != item:
                    node = node.next
                else:
                    return True
            return False
            

    def delete(self, item):
        if self.is_empty() == False:
            if self.head.data == item:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return
                self.head = self.head.next
                return
            node = self.head
            while node != self.tail:
                if node.next.data == item:
                    if node.next != self.tail:
                        node.next = node.next.next
                        return
                    else:
                        node.next = None
                        self.tail = node
                        return
                node = node.next
        raise ValueError(f'Item not found: {format(item)}')


    




#-------------------------------------------------------------------------------------

def merge_sorted_ll(list1, list2):
  merged_list = LinkedList()
  current_node1 = list1.head
  current_node2 = list2.head

  while current_node1 != list1.tail and current_node2 != list2.tail:
    if current_node1.data > current_node2.data:
      merged_list.append(current_node2.data)
      current_node2 = current_node2.next
    elif current_node1.data < current_node2.data:
      merged_list.append(current_node1.data)
      current_node1 = current_node1.next
  while current_node1 != list1.tail:
    merged_list.append(current_node1)
    current_node1 = current_node1.next
  while current_node2 != list2.tail:
    merged_list.append(current_node2)
    current_node2 = current_node2.next
  
  return merged_list


if __name__ == "__main__":
    list1 = LinkedList([1,3,5])
    print('input1', list1)
    list2 = LinkedList([2,4,6])
    print('input2', list2)
    print('test:',merge_sorted_ll(list1,list2))