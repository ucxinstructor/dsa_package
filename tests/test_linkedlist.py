import unittest
from dsa.singlylinkedlist import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    def test_create(self):
        ll = LinkedList()
        self.assertEqual(ll.count, 0)
        self.assertTrue(ll.is_empty())

        n1 = Node(10)
        ll = LinkedList(n1)
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)

        n2 = Node(20)
        n1.next = n2
        ll = LinkedList(n1, n2, 2)
        self.assertEqual(ll.count, 2)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 20)

        n3 = Node(30)
        n2.next = n3
        ll = LinkedList(n1, n3, 3)
        self.assertEqual(ll.count, 3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 30)
        self.assertFalse(ll.is_empty())

    def test_from_list(self):
        ll = LinkedList.from_list([])
        self.assertEqual(ll.count, 0)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

        ll = LinkedList.from_list([1])
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)

        ll = LinkedList.from_list([1, 2])
        self.assertEqual(ll.count, 2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

        ll = LinkedList.from_list([1, 2, 3])
        self.assertEqual(ll.count, 3)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)


    def test_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), list())

        for _ in range(15):
            ll.append(_)

        self.assertEqual(ll.to_list(), list(range(15)))

    def test_search(self):
        ll = LinkedList.from_list(range(20))
        self.assertRaises(Exception, ll.search, -1)
        self.assertEqual(ll.search(1), 1)
        self.assertEqual(ll.search(10), 10)
        self.assertRaises(Exception, ll.search, 20)

    def test_insert(self):
        ll = LinkedList()

        for _ in range(15):
            ll.append(_)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.head.next.value, 1)
        self.assertEqual(ll.tail.value, 14)
        self.assertEqual(ll.count, 15)

        for _ in range(10):
            ll.prepend(_)
        self.assertEqual(ll[0], 9)
        self.assertEqual(ll[2], 7)
        self.assertEqual(ll.count, 25)



    def test_delete(self):
        ll = LinkedList()

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
        ll = LinkedList()

        for _ in range(15):
            ll.append(_)

        node = ll.head
        for _ in range(15):
            self.assertEqual(node.value, _)
            node = node.next

    def test_index(self):
        ll = LinkedList.from_list(range(20))
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[19], 19)

if __name__ == '__main__':
    unittest.main()
