""" Module containing tree class. """

class TreeNode:
    """ 
    A binary tree node implementation.
    """
    def __init__(self, value, left=None, right=None):
        """ 
        TreeNode constructor.
        
        Args:
            value: The value of the node.
            left: Reference to the left node.
            right: Reference to the right node.
        """
        self.value = value
        self.left = left
        self.right = right

    def copy(self):
        """
        Return a copy of the node.
        """
        new_node = TreeNode(self.value) 
        if self.left:
            new_node.left = self.left.copy()
        if self.right:
            new_node.right = self.right.copy()
        return new_node
    
    def print(self, level=0):
        """ 
        Print the contents of a node.

        Args:
            level: starting level of node
        """
        if self.right:
            self.right.print(level + 1)
        print("   " * level + str(self.value))
        if self.left:
            self.left.print(level + 1)

    def __lt__(self, other):
        """
        Compare the value of two nodes.
        """
        return self.value < other.value
    
    def __repr__(self):
        """
        Return the string representation of a node.
        """
        if self.value is None:
            return "none"
        else:
            return str(self.value)

class Tree:
    """ 
    A binary search tree (BST) implementation. Can be treated as a plain binary tree if operations (insert, search, delete) are not used and nodes are set manually.
    """
    def __init__(self, root=None):
        """ 
        Args:
            root: Root node of the Tree.
        """
        self.root = root
        
    def search(self, value):
        """ 
        Search for a value in the binary search tree.

        Args:
            value: Value to search for.
        
        Returns:
            node with matching value

        Raises:
            ValueError: if value is not found
        """
        current = self.root
        
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right

        raise ValueError(f"Value {value} not found in the tree")

    def insert(self, value):
        """ 
        Insert a value in the binary search tree.

        Args:
            value: The value to insert.
        
        Returns:
            The root of the tree after deletion.

        Raises:
            ValueError: if value is already in the tree
        """
        self.root = self.insert_rec(self.root, value)
        return self.root
    
    def insert_rec(self, root, value):
        if root is None:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert_rec(root.left, value)
        elif value > root.value:
            root.right = self.insert_rec(root.right, value)
        else:
            raise ValueError("Value already exists in the tree")
        return root

    def insert_iterative(self, value):
        """ 
        Insert a value in the binary search tree (iterative implementation).

        Args:
            value: The value to insert.
        
        Returns:
            None

        Raises:
            ValueError: if value is already in the tree
        """
        current = self.root
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                else:
                    current = current.right
            else:
                return 
   
    def delete(self, value):
        """ 
        Delete a value from the binary search tree.

        Args:
            value: The value to delete.
        
        Returns:
            The root of the tree after insertion.

        
        Raises:
            ValueError: if value is not found.
        """
        self.root = self.delete_node(self.root, value)
        return self.root
        
    def delete_node(self, node, value):
        """ 
        Helper function to delete a value from the binary search tree. (Use delete() instead)

        Args:
            value: The value to delete.
            node: The current node.

        Returns:
            The new subtree root after deletion.
        
        Raises:
            ValueError: if value is not found.
        """ 
        if node is None:
            raise ValueError("Value not found in the tree")
            return None
        
        if value < node.value:
            node.left = self.delete_node(node.left, value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            if node.left is None:
                subtree = node.right
                node = None
                return subtree
            elif node.right is None:
                subtree = node.left
                node = None
                return subtree
            
            successor = self.successor_node(node.right)
            node.value = successor.value
            node.right = self.delete_node(node.right, successor.value)
            
        return node
    
    def successor_node(self, node=None):
        """ 
        Return the successor node (the minimum value in a binary search tree's right subtree).

        Args:
            node: The starting node.
        
        Returns:
            node with the lowest value in the BST
            None if not found

        Raises:
            ValueError: if value is not found.
        """
        if node is None:
            node = self.root
        
        if node.left is None:
            return node
        else:
            return self.successor_node(node.left)
    
    def predecessor_node(self, node=None):
        """ 
        Return the predecessor node (the maximum value in a binary search tree's left subtree).

        Args:
            node: The starting node.
        
        Returns:
            node with the lowest value in the BST
            None if not found

        Raises:
            ValueError: if value is not found.
        """
        if node is None:
            node = self.root
        
        if node.right is None:
            return node
        else:
            return self.predecessor_node(node.right)
    
    def delete_iterative(self, root, value):
        """ 
        Delete a value from the binary search tree (iterative version).

        Args:
            value: The value to delete.
        
        Returns:
            The root of the tree after insertion.

        
        Raises:
            ValueError: if value is not found.
        """
        parent = None
        current = root

        # Find the node to delete and its parent
        while current and current.key != value:
            parent = current
            if value < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return root  # Key not found

        # Case 1 & 2: Node has at most one child
        def replace_node_in_parent(new_child):
            if parent is None:
                return new_child  # Deleting the root node
            if parent.left == current:
                parent.left = new_child
            else:
                parent.right = new_child
            return root

        if current.left is None:
            return replace_node_in_parent(current.right)
        elif current.right is None:
            return replace_node_in_parent(current.left)

        # Case 3: Node has two children
        # Find in-order successor and its parent
        successor_parent = current
        successor = current.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace current's key with successor's key
        current.key = successor.key

        # Delete successor node (which has at most one child)
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        return root

    def print(self):
        """ 
        Print the values in the BST.
        """
        self.root.print()
        
    def __len__(self):
        """ 
        Return the number of nodes in the BST.
        
        Returns:
            The number of nodes in the BST.
        """
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        return count_nodes(self.root)
        

    def __eq__(self, other):
        """
        Compare two Tree objects for value-based equality (structure and values).

        Returns:
            True if both are Tree instances and their structures and values are equal, False otherwise.
        """
        if not isinstance(other, Tree):
            return False
        def nodes_equal(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return (
                n1.value == n2.value and
                nodes_equal(n1.left, n2.left) and
                nodes_equal(n1.right, n2.right)
            )
        return nodes_equal(self.root, other.root)

