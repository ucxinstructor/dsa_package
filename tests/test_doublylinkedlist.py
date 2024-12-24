import unittest
from dsa.doublylinkedlist import DoublyLinkedList, Node

class TestDoublyLinkedList(unittest.TestCase):
    def test_create(self):
        ll = DoublyLinkedList()
        self.assertEqual(ll.count, 0)
        self.assertTrue(ll.is_empty())
        n1 = Node(10)
        ll = DoublyLinkedList(n1)
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)

        n2 = Node(20)
        n1.next = n2
        ll = DoublyLinkedList(n1, n2, 2)
        self.assertEqual(ll.count, 2)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 20)

        n3 = Node(30)
        n2.next = n3
        ll = DoublyLinkedList(n1, n3, 3)
        self.assertEqual(ll.count, 3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 30)
        self.assertFalse(ll.is_empty())

    def test_from_list(self):
        ll = DoublyLinkedList.from_list([])
        self.assertEqual(ll.count, 0)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

        ll = DoublyLinkedList.from_list([1])
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)

        ll = DoublyLinkedList.from_list([1, 2])
        self.assertEqual(ll.count, 2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

        ll = DoublyLinkedList.from_list([1, 2, 3])
        self.assertEqual(ll.count, 3)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)
        
    def test_to_list(self):
        ll = DoublyLinkedList()
        for _ in range(15):
            ll.append(_)

        self.assertEqual(ll.to_list(), list(range(15)))

    def test_search(self):
        ll = DoublyLinkedList.from_list(range(20))
        self.assertRaises(Exception, ll.search, -1)
        self.assertEqual(ll.search(1), 1)
        self.assertEqual(ll.search(10), 10)
        self.assertRaises(Exception, ll.search, 20)


    def test_insert(self):
        ll = DoublyLinkedList()

        for _ in range(15):
            ll.append(_)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.head.next.value, 1)
        self.assertEqual(ll.head.next.prev.value, 0)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.tail.prev.value, 13)
        self.assertEqual(ll.tail.prev.next.value, 14)
        self.assertEqual(ll.count, 15)

        for _ in range(10):
            ll.prepend(_)
        self.assertEqual(ll[0], 9)
        self.assertEqual(ll[2], 7)
        self.assertEqual(ll.count, 25)

    def test_delete(self):
        ll = DoublyLinkedList()

        for _ in range(15):
            ll.append(_)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)
        
        for _ in range(15):
            ll.delete(0)
            self.assertEqual(ll.count, 14 - _)
        self.assertRaises(Exception, ll.delete, 0)

    def test_traverse(self):
        ll = DoublyLinkedList()

        for _ in range(15):
            ll.append(_)

        node = ll.head
        for _ in range(15):
            self.assertEqual(node.value, _)
            node = node.next

        # traverse backwards
        node = ll.tail
        for _ in range(15):
            self.assertEqual(node.value, 14 - _)
            node = node.prev
        
    def test_index(self):
        ll = DoublyLinkedList.from_list(range(20))
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[19], 19)

    def test_init_empty(self):
        dll = DoublyLinkedList()
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)
        self.assertEqual(dll.count, 0)

    def test_init_with_head(self):
        node = Node(1)
        dll = DoublyLinkedList(head=node)
        self.assertEqual(dll.head, node)
        self.assertEqual(dll.tail, node)
        self.assertEqual(dll.count, 1)

    def test_init_with_head_and_tail(self):
        head = Node(1)
        tail = Node(2)
        dll = DoublyLinkedList(head=head, tail=tail, count=2)
        self.assertEqual(dll.head, head)
        self.assertEqual(dll.tail, tail)
        self.assertEqual(dll.count, 2)

    def test_from_list_short(self):
        values = [1, 2, 3, 4]
        dll = DoublyLinkedList.from_list(values)
        self.assertEqual(dll.to_list(), values)
        self.assertEqual(dll.count, len(values))

    def test_to_list_empty(self):
        values = [1, 2, 3, 4]
        dll = DoublyLinkedList.from_list(values)
        self.assertEqual(dll.to_list(), values)

    def test_repr(self):
        values = [1, 2, 3, 4]
        dll = DoublyLinkedList.from_list(values)
        expected_repr = "[ 1 2 3 4 ] Count: 4"
        self.assertEqual(repr(dll), expected_repr)

if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    unittest.main()
