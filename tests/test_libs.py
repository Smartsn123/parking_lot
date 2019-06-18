import sys, os
import unittest
sys.path.append("{}/src/lib".format(os.getcwd()))
from utils import CustomHeap


class TestObj:
    def __init__(self, id, val):
        self.id = id
        self.val = val


class TestHeap(unittest.TestCase):

    def test_init(self):
        function_name = "CustomeHeap.init"
        print("Running unittest cases for {}\n".format(function_name))
        items = [TestObj(i, 10-i) for i in range(10) if i!=4]
        heap = CustomHeap(items, 'id', 'val')
        correct_answer = [(1, 9), (2, 8), (3, 7), (7, 3), (5, 5), (4, 6), (8, 2), (9, 1), (10, 0)]
        self.assertListEqual(heap.heap_list, correct_answer, "unittest for {} failed ".format(function_name))

    def test_insert(self):
        function_name = "CustomeHeap.insert"
        print("Running unittest cases for {}\n".format(function_name))
        items = [TestObj(i, 10 - i) for i in range(10) if i != 8]
        heap = CustomHeap(items, 'id', 'val')
        heap.insert(TestObj(8, 2))
        correct_answer = [(1, 9), (2, 8), (4, 6), (7, 3), (3, 7), (5, 5), (8, 2), (9, 1), (10, 0), (6, 4)]
        self.assertListEqual(heap.heap_list, correct_answer, "unittest for {} failed ".format(function_name))

    def test_extract_min(self):
        function_name = "CustomeHeap.extract_min"
        print("Running unittest cases for {}\n".format(function_name))
        items = [TestObj(i, 10 - i) for i in range(10) if i != 8]
        heap = CustomHeap(items, 'id', 'val')
        initial_len = len(heap.heap_list)
        mini_val, mini_id = heap.extract_min()
        match1 = (mini_id == 9 and mini_val == 1) and len(heap.heap_list) == initial_len-1
        mini_val, mini_id = heap.extract_min()
        match2 = (mini_id == 7 and mini_val == 3) and len(heap.heap_list) == initial_len-2
        mini_val, mini_id = heap.extract_min()
        match3 = (mini_id == 6 and mini_val == 4) and len(heap.heap_list) == initial_len-3

        heap.insert(TestObj(8, 2))
        mini_val, mini_id = heap.extract_min()
        match4 = (mini_id == 8 and mini_val == 2) and len(heap.heap_list) == initial_len-3

        self.assertEqual(match1, True, "unittest for {} failed ".format(function_name))
        self.assertEqual(match2, True, "unittest for {} failed ".format(function_name))
        self.assertEqual(match3, True, "unittest for {} failed ".format(function_name))
        self.assertEqual(match4, True, "unittest for {} failed ".format(function_name))

    def test_remove_node_id(self):
        function_name = "CustomeHeap.remove_node_id"
        print("Running unittest cases for {}\n".format(function_name))
        items = [TestObj(i, 10 - i) for i in range(10) ]
        heap = CustomHeap(items, 'id', 'val')
        heap.remove_node_id(8)
        correct_answer = [(1, 9), (3, 7), (4, 6), (7, 3), (6, 4), (5, 5), (8, 2), (10, 0), (9, 1)]
        self.assertListEqual(heap.heap_list, correct_answer, "unittest for {} failed ".format(function_name))


    def test_node_map(self):
        function_name = "CustomeHeap.node_map"
        print("Running unittest cases for {}\n".format(function_name))
        def check_correct_mapping(heap):
            for id, node_ix in heap.node_map.items():
                self.assertEqual(id, heap.heap_list[node_ix][1],"unittest for {} failed ".format(function_name))
        items = [TestObj(i, 10 - i) for i in range(10) if i != 8]
        heap = CustomHeap(items, 'id', 'val')
        check_correct_mapping(heap)
        heap.extract_min()
        check_correct_mapping(heap)
        heap.extract_min()
        check_correct_mapping(heap)
        heap.extract_min()
        check_correct_mapping(heap)
        heap.insert(TestObj(8, 2))
        check_correct_mapping(heap)
        heap.extract_min()
        check_correct_mapping(heap)




if __name__ == '__main__':
    unittest.main()