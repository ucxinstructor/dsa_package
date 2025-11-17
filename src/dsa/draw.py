""" Module to access graphic drawing functions for Trees, Heaps, Tries and Graphs. """

from dsa.tree import Tree, TreeNode
from dsa.heap import Heap
from dsa.trie import Trie

import networkx as nx
import matplotlib.pyplot as plt

class Draw:
    """
    A base class for drawing various data structures.
    
    This class provides basic functionalities for rendering, saving, and displaying
    visual representations of data structures.
    """
    def __init__(self):
        """
        Initialize the Draw class with default figure size.
        """
        self.figsize = (5, 3)
        
    def render(self, **kwargs):
        """
        Render the visual representation of the data structure.
        
        This method should be overridden by subclasses to provide specific rendering logic.
        Args:
            **kwargs: Additional keyword arguments.
        """
        pass

    def set_figsize(self, figsize):
        """
        Set the figure size for the plot.
        
        Args:
            figsize (tuple): A tuple representing the figure size (width, height).
        """
        self.figsize = figsize

    def save(self, filename, **kwargs):
        """
        Save the rendered plot to a file.
        
        Args:
            filename (str): The name of the file to save the plot to.
            **kwargs: Additional keyword arguments.
        """
        plt = self.render(**kwargs)
        plt.axis('off')
        plt.savefig(filename)

    def draw(self, **kwargs):
        """
        Display the rendered plot.

        Args:
            **kwargs: Additional keyword arguments.
        """
        plt = self.render(**kwargs)
        plt.axis('off')
        plt.show()

class TreeDraw(Draw):
    """
    A class for drawing a tree structure using the NetworkX library.

    This class extends the `Draw` class to visualize tree structures. It organizes the nodes
    in a hierarchical tree layout and provides options for customization through the `render` method.

    Attributes:
        tree (Tree): The tree structure to be drawn.

    Usage Example:
        t = Tree(root_node)  # Define your tree structure with a root node
        td = TreeDraw(t)
        td.draw()
    """

    def __init__(self, tree: Tree):
        """ 
        Initializes the TreeDraw object.

        Args:
            tree (Tree): The tree structure to be drawn.
        """
        super().__init__()
        self.tree = tree
        
    def add_edges(self, graph, node, pos=None, x: float=0, y: float=0, layer=1):
        """
        Recursively adds edges to the graph and positions the nodes in a tree layout.
    
        Args:
            graph (networkx.DiGraph): The graph object where edges are added.
            node (TreeNode): The current node in the tree.
            pos (dict, optional): A dictionary to store the positions of the nodes. Defaults to None.
            x (float): The x-coordinate for the current node. Defaults to 0.
            y (float): The y-coordinate for the current node. Defaults to 0.
            layer (int): The current layer/level of the node in the tree. Defaults to 1.

        Returns:
            dict: A dictionary containing the positions of all nodes in the tree.
        """
        if pos is None:
            pos = {}
        if node is not None:
            pos[node.value] = (x, y)
            if node.left:
                graph.add_edge(node.value, node.left.value)
                pos = self.add_edges(graph, node.left, pos=pos, x=x-1/layer, y=y-1, layer=layer+1)
            if node.right:
                graph.add_edge(node.value, node.right.value)
                pos = self.add_edges(graph, node.right, pos=pos, x=x+1/layer, y=y-1, layer=layer+1)
        return pos
    
    def render(self, **kwargs):
        """ 
        Renders the tree using Matplotlib. Not to be called directly. Call draw() instead.

        This method generates a graphical representation of the tree with nodes positioned
        in a hierarchical layout. Customization options can be provided via keyword arguments.

        Args:
            **kwargs: Additional keyword arguments for customization.

        Returns:
            matplotlib.pyplot: The Matplotlib plot object for further customization or display.
        """
        super().render(**kwargs)
        graph = nx.DiGraph()
        pos = self.add_edges(graph, self.tree.root)
        plt.figure(figsize=self.figsize)
        nx.draw(graph, pos, with_labels=True, arrows=False, node_color="tab:blue", node_size=800, font_size=12, font_color="white") 
        return plt

class HeapDraw(Draw):
    """
    A class for drawing a heap structure using the NetworkX library.

    This class extends the `Draw` class to visualize heap structures, such as binary heaps or min-heaps.

    Attributes:
        heap (Heap): The heap structure to be drawn.

    Usage Example:
        h = MinHeap()  # Define your heap, e.g., MinHeap or Heap
        hd = HeapDraw(h)
        hd.draw()
    """

    def __init__(self, heap: Heap, **kwargs):
        """
        Initializes the HeapDraw object.

        Args:
            heap (Heap): The heap structure to be drawn.
            **kwargs: Additional keyword arguments passed to the parent `Draw` class.
        """
        super().__init__(**kwargs)
        self.heap = heap

    def array_to_node(self, index: int, array):
        """
        Converts an array-based heap into a tree node structure.

        This helper function recursively constructs a tree from the array representation
        of the heap, reflecting the binary tree structure of the heap.

        Args:
            index (int): The current index in the array representing the node.
            array (list): The array containing heap values, organized as a complete binary tree.

        Returns:
            TreeNode: The root node of the constructed subtree.
        """
        if index >= len(array):
            return None
        else:
            value = array[index]
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            node = TreeNode(value)
            node.left = self.array_to_node(left_index, array)
            node.right = self.array_to_node(right_index, array)
            return node

    def render(self, **kwargs):
        """
        Renders the heap as a tree using Matplotlib. Not to be called directly. Call draw() instead.

        This method converts the heap into a tree structure and then uses the `TreeDraw` class
        to render it visually. Customization options can be provided via keyword arguments.

        Returns:
            matplotlib.pyplot: The Matplotlib plot object for further customization or display.
        """
        node = self.array_to_node(0, [node[1] for node in self.heap.enumerate()])
        tree = Tree(node)

        tree_draw = TreeDraw(tree)
        tree_draw.set_figsize(self.figsize)
        return tree_draw.render(**kwargs)
    
class TrieDraw(Draw):
    """
    A class for drawing a Trie structure using the NetworkX library.

    This class extends the `Draw` class to visualize Trie structures, commonly used for storing strings
    or prefix trees. It provides methods to convert the Trie into a networkx graph, arrange nodes
    hierarchically, and render the visualization using Matplotlib.

    Attributes:
        trie (Trie): The Trie structure to be drawn.

    Usage Example:
        trie = Trie()  # Initialize your Trie and populate it with words
        trd = TrieDraw(trie)
        trd.draw()
    """

    def __init__(self, trie: Trie, **kwargs):
        """
        Initializes the TrieDraw object.

        Args:
            trie (Trie): The Trie structure to be drawn.
            **kwargs: Additional keyword arguments passed to the parent `Draw` class.
        """
        super().__init__(**kwargs)
        self.figsize = (10, 6)
        self.trie = trie
        
    def _add_edges(self, graph, node, current_path):
        """
        Recursively adds edges to the networkx graph based on the Trie structure.

        This helper function traverses the Trie, adding edges between nodes in the
        networkx graph and associating them with characters from the Trie.

        Args:
            graph (networkx.DiGraph): The directed graph to which edges are added.
            node (TrieNode): The current node in the Trie.
            current_path (str): The path representing the current prefix in the Trie.
        """
        if node is None:
            return
        for char, child in node.children.items():
            new_path = current_path + char
            graph.add_edge(current_path, new_path, label=char)
            self._add_edges(graph, child, new_path)
    
    def to_networkx(self) -> nx.DiGraph:
        """
        Converts the Trie into a NetworkX directed graph (DiGraph).

        This method creates a networkx graph representation of the Trie, where each node
        represents a prefix and each edge represents a character transition.

        Returns:
            networkx.DiGraph: The networkx graph representation of the Trie.
        """
        graph = nx.DiGraph()
        self._add_edges(graph, self.trie.root, "")
        return graph
    
    def hierarchical_pos(self, G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        Computes the hierarchical position of nodes in the graph for visualization.

        This method arranges the nodes of the Trie in a hierarchical layout, which is
        particularly useful for visualizing tree-like structures such as Tries.

        Args:
            G (networkx.Graph): The graph for which to compute positions.
            root (str, optional): The root node of the graph. Defaults to None, which means
                                  the root will be determined automatically.
            width (float): The width of the entire drawing. Defaults to 1.
            vert_gap (float): The gap between levels in the hierarchy. Defaults to 0.2.
            vert_loc (float): The vertical location of the root node. Defaults to 0.
            xcenter (float): The horizontal center of the root node. Defaults to 0.5.

        Returns:
            dict: A dictionary mapping each node to its (x, y) position in the layout.
        """
        if root is None:
            root = next(iter(nx.topological_sort(G)))
    
        def _hierarchical_pos(G, node, width: float=1., vert_gap: float=0.2, vert_loc:float=0, xcenter:float=0.5, pos=None, parent=None, parsed=[]):
            if pos is None:
                pos = {node: (xcenter, vert_loc)}
            else:
                pos[node] = (xcenter, vert_loc)
    
            children = list(G.neighbors(node))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)
    
            if len(children) != 0:
                dx = width / len(children)
                nextx = xcenter - width / 2 - dx / 2
                for child in children:
                    nextx += dx
                    pos = _hierarchical_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos, parent=node, parsed=parsed)
            return pos
    
        return _hierarchical_pos(G, root, width, vert_gap, vert_loc, xcenter)
    
    def render_rectangle(self, **kwargs):
        """
        Renders the Trie as a hierarchical graph using Matplotlib. Not to be called directly. Call draw() instead.

        This method uses the hierarchical positions of the nodes to render the Trie
        as a directed graph. Nodes are drawn as rectangles, and edges represent the transitions
        between prefixes.

        Returns:
            matplotlib.pyplot: The Matplotlib plot object for further customization or display.
        """
        super().render(**kwargs)
        trie_graph = self.to_networkx()
        
        pos = self.hierarchical_pos(trie_graph)
        
        plt.figure(figsize=self.figsize)
        nx.draw_networkx_edges(trie_graph, pos, arrows=True)
        
        ax = plt.gca()
        rect_width = 0.05
        rect_height = 0.15
        for node in pos:
            x, y = pos[node]
            rectangle = plt.Rectangle((x - (rect_width / 2), y - (rect_height / 2)), rect_width, rect_height, color="tab:blue")
            ax.add_patch(rectangle)
            plt.text(x, y, node[-1] if node else "", verticalalignment='center', horizontalalignment='center', fontsize=12, color="white")
        return plt

    def render(self, **kwargs):
        """
        Renders the Trie as a hierarchical graph using Matplotlib. Not to be called directly. Call draw() instead.

        This version uses NetworkX's default drawing tools with circular nodes for simplicity and clarity.
        """
        super().render(**kwargs)
        trie_graph = self.to_networkx()
        pos = self.hierarchical_pos(trie_graph)

        plt.figure(figsize=self.figsize)

        # Draw the graph using built-in node and edge drawing
        nx.draw(
            trie_graph,
            pos,
            with_labels=True,
            labels={node: node[-1] if node else "" for node in trie_graph.nodes},
            node_shape='o',
            node_color='tab:blue',
            font_color='white',
            font_size=10,
            edgecolors='none',
            arrows=False,
            **kwargs
        )

        return plt

class GraphDraw(Draw):
    """
    A class for drawing graphs using the NetworkX library.

    This class extends the `Draw` class to visualize graphs. It supports both directed 
    and undirected graphs, as well as weighted and unweighted graphs. Additionally, 
    it provides an option to display the Minimum Spanning Tree (MST) of the graph.

    Attributes:
        graph: The graph to be drawn
        directed (bool): Specifies if the graph is directed. Defaults to False
        weighted (bool): Specifies if the graph has weighted edges. Defaults to False

    Usage Example:
        gd = GraphDraw(g) # g is a Graph type (AdjacencyMatrixGraph, AdjacencyMatrixWeightedGraph, AdjacencyListWeightedGraph, AdjacencyListGraph)
        gd.draw()
    """
    def __init__(self, graph, directed=False, weighted=False):
        """
        Initializes the GraphDraw object.
        """
        super().__init__()
        self.graph = graph
        self.directed = directed
        self.weighted = weighted
            
    def render(self, pos=None, show_mst=False, mst_only=False, **kwargs):
        """
        Renders the graph using Matplotlib. Not to be called directly. Call draw() instead.
        """
        super().render(**kwargs)
        edges = self.graph.edges()

        if self.directed:
            g = nx.DiGraph()
        else:
            g = nx.Graph()

        if self.weighted:
            g.add_weighted_edges_from(edges)
        else:
            g.add_edges_from(edges)
    
        if pos is None:
            pos = nx.shell_layout(g) 

        plt.figure(figsize=self.figsize)

        if mst_only:
            show_mst = True
            nx.draw_networkx_nodes(g, pos, node_color="tab:blue", node_size=800)
            nx.draw_networkx_labels(g, pos, font_size=10, font_color="white")
        else:
            nx.draw(g, pos, with_labels=True, node_color="tab:blue", node_size=800, font_size=10, font_color="white")

        if self.weighted:
            edge_labels = {(u, v): d["weight"] for u, v, d in g.edges(data=True)}
            nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_size=14, label_pos=0.5)

        if show_mst:
            T = nx.minimum_spanning_tree(g)
            nx.draw_networkx_edges(T, pos, edge_color="tab:red", width=2)
        return plt

