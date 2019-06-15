def comp(a, b, comp_type):
    if comp_type == 'min':
        return a < b
    else:
        return a > b


class CustomHeap:
    """
    A custom heap class with delete operation of id of the element given supported
    accepts generic objects and id_field and value_field functions
    """

    def __init__(self, items, id_field, value_field, heap_type='min'):
        """
        Constructor to construct a heap from the list of items
        :param items: list of objects
        :param id_field: field that will be used as identifier
        :param value_field: field that will be used for comparing
        :param heap_type: min or max heap
        :return: self object by default
        Complexity : O(n)
        """
        self.id_field = id_field
        self.value_field = value_field
        self.heap_list = [(getattr(item, value_field), getattr(item, id_field)) for item in items]
        self.heap_type = heap_type
        self.node_map = {item[1]: ix for ix, item in enumerate(self.heap_list)}
        for ix in range(int(len(self.heap_list)/2), -1, -1):
            self.heapify(ix)

    def __len__(self):
        """
        Interface len(Obj) function
        :return: length of the heap list
        """
        return len(self.heap_list)

    def swap(self, ix1, ix2):
        """
        function to swap heap nodes while maintaining the node_map correct
        :param ix1: index of first heap node
        :param ix2: index of second heap node
        :return: None
        """
        id1 = self.heap_list[ix1][1]
        id2 = self.heap_list[ix2][1]
        self.node_map[id1] = ix2
        self.node_map[id2] = ix1
        self.heap_list[ix1], self.heap_list[ix2] = self.heap_list[ix2], self.heap_list[ix1]

    def heapify(self, ix):
        """
        function to heapify from a given index
        :param ix: index to call heapify on
        :return: None
        """
        minim = ix
        left_node = 2*ix+1
        right_node = 2*ix+2
        if left_node < len(self.heap_list) and comp(self.heap_list[left_node],
                                                    self.heap_list[minim],
                                                    self.heap_type):
            minim = left_node

        if right_node < len(self.heap_list) and comp(self.heap_list[right_node],
                                                     self.heap_list[minim],
                                                     self.heap_type):
            minim = right_node

        if minim != ix:
            self.swap(ix, minim)
            self.heapify(minim)

    def insert(self, item):
        """
        function to insert new item into the  heap
        :param item: object to be inserted
        :return: None
        """
        new_item = (getattr(item, self.value_field), getattr(item, self.id_field))
        self.heap_list.append(new_item)
        self.node_map[new_item[1]] = len(self.heap_list)-1
        cur = len(self.heap_list)-1
        par = int((cur-1)/2)
        while cur != 0 and comp(self.heap_list[cur],
                                self.heap_list[par],
                                self.heap_type):
            self.swap(par, cur)
            cur = par
            par = int((cur-1)/2)

    def remove_last(self):
        """
        function to remove node from heap
        :param ix: index to
        :return:
        """
        self.node_map.pop(self.heap_list[-1][1])
        self.heap_list = self.heap_list[:-1]

    def extract_min(self):
        """
        :return: return minimum object
        """
        tmp = (self.heap_list[0][0], self.heap_list[0][1])
        self.swap(0, len(self.heap_list)-1)
        self.remove_last()
        self.heapify(0)
        return tmp

    def remove_node_id(self, id):
        """
        function to remove any item whose id is given
        :param id: id of the item to be removed
        :return: None
        """
        print(self.node_map)
        remove_ix = self.node_map[id]
        old_val = self.heap_list[remove_ix][0]
        new_val = self.heap_list[-1][0]

        if remove_ix != len(self.heap_list)-1:
            self.swap(remove_ix, len(self.heap_list)-1)
            if old_val > new_val:
                cur = remove_ix
                par = int((cur - 1) / 2)
                while cur != 0 and comp(self.heap_list[cur], self.heap_list[par], self.heap_type):
                    self.swap(par, cur)
                    cur = par
                    par = int((cur - 1) / 2)

            elif old_val < new_val:
                self.heapify(remove_ix)
        self.remove_last()





