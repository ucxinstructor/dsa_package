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

        ll = DoublyLinkedList.from_list([])
        self.assertEqual(ll.to_list(), list())

        ll = DoublyLinkedList.from_list([1])
        self.assertEqual(ll.to_list(), [1])

        ll = DoublyLinkedList.from_list([1, 2])
        self.assertEqual(ll.to_list(), [1, 2])

        ll = DoublyLinkedList.from_list([1, 2, 3])
        self.assertEqual(ll.to_list(), [1, 2, 3])

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
        self.verify_previous_link(ll)

        for _ in range(10):
            ll.prepend(_)
        self.assertEqual(ll[0], 9)
        self.assertEqual(ll[2], 7)
        self.assertEqual(ll.count, 25)
        self.verify_previous_link(ll)

    def test_insert_at_index(self):
        ll = DoublyLinkedList()

        for _ in range(15):
            ll.append(_)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.head.next.value, 1)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)

        ll.insert(0, 100)
        self.assertEqual(ll.head.value, 100)
        self.assertEqual(ll.head.next.value, 0)
        self.assertEqual(ll.head.next.prev.value, 100)
        self.assertEqual(ll.count, 16)
        self.verify_previous_link(ll)

        ll.insert(1, 200)
        self.assertEqual(ll.head.next.value, 200)
        self.assertEqual(ll.head.next.next.value, 0)
        self.assertEqual(ll.head.next.next.prev.value, 200)
        self.assertEqual(ll.count, 17)
        self.verify_previous_link(ll)

        ll.insert(10, 300)
        self.assertEqual(ll[10], 300)
        self.assertEqual(ll[11], 8)
        self.assertEqual(ll[9], 7)
        self.assertEqual(ll.count, 18)
        self.verify_previous_link(ll)

        ll.insert(17, 400)
        self.assertEqual(ll[17], 400)
        self.assertEqual(ll[18], 14)
        self.assertEqual(ll[16], 13)
        self.assertEqual(ll.count, 19)
        self.verify_previous_link(ll)

        ll.insert(19, 500)
        self.assertEqual(ll[19], 500)
        self.assertEqual(ll.tail.value, 500)
        self.assertEqual(ll.tail.prev.value, 14)
        self.assertEqual(ll.count, 20)
        self.verify_previous_link(ll)

        self.assertRaises(IndexError, ll.insert, 21, 600)

    def test_delete(self):
        ll = DoublyLinkedList()

        for _ in range(15):
            ll.append(_)
        self.assertRaises(IndexError, ll.delete, 15)

        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)
        
        for _ in range(15):
            ll.delete(0)
            self.assertEqual(ll.count, 14 - _)
        self.assertRaises(IndexError, ll.delete, 0)

        for _ in range(15):
            ll.append(_)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)

        for _ in range(15):
            ll.delete(len(ll) - 1)
            self.assertEqual(ll.count, 14 - _)
        self.assertRaises(IndexError, ll.delete, 0)

        self.verify_previous_link(ll)

        # delete middle
        for _ in range(15):
            ll.append(_)

        for _ in range(5):
            ll.delete(len(ll) // 2)
            self.assertEqual(ll.count, 14 - _)
        self.verify_previous_link(ll)

        # test delete tail and check tail value
        ll.delete(len(ll) - 1)
        self.assertEqual(ll.tail.value, 13)
        self.assertEqual(ll.count, 9)

        ll = DoublyLinkedList.from_list(range(20))
        ll.delete(19)
        self.assertEqual(ll.tail.value, 18)
        self.assertEqual(ll.count, 19)
        ll.delete(0)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.count, 18)
        ll.delete(3)
        self.assertEqual(ll[3], 5)
        self.assertEqual(ll.count, 17)  

        self.verify_previous_link(ll)

    def verify_previous_link(self, ll):
        current = ll.head
        while current and current.next:
            self.assertEqual(current.next.prev, current)
            current = current.next
            self.assertIsNotNone(current.prev, "Previous node is None, the list might be malformed.")

    def test_traverse(self):
        ll = DoublyLinkedList.from_list(range(15))
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

    def test_delete_head(self):
        dll = DoublyLinkedList()
        self.assertRaises(IndexError, dll.delete_head)

        dll = DoublyLinkedList.from_list([1, 2, 3])
        dll.delete_head()
        self.assertEqual(dll.to_list(), [2, 3])
        self.assertEqual(dll.count, 2)

    def test_delete_tail(self):
        dll = DoublyLinkedList()
        self.assertRaises(IndexError, dll.delete_tail)

        dll = DoublyLinkedList.from_list([1, 2, 3])
        dll.delete_tail()
        self.assertEqual(dll.to_list(), [1, 2])
        self.assertEqual(dll.count, 2)
    
if __name__ == '__main__':
    unittest.main()
