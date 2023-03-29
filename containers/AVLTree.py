'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree():
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node is None:
            return ret
        if not AVLTree._is_bst_satisfied(node):
            return False
        if AVLTree._balance_factor(node) in [-1, 0, 1]:
            node_left = AVLTree._is_avl_satisfied(node.left)
            node_right = AVLTree._is_avl_satisfied(node.right)
            return ret and node_left and node_right
        else:
            return False

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        newnode = node
        if newnode.right:
            newroot = Node(newnode.right.value)
            newroot.left = Node(newnode.value)
            newroot.right = newnode.right.right
            newroot.left.left = newnode.left
            newroot.left.right = newnode.right.left
            return newroot
        else:
            return newnode

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        newnode = node
        if newnode.left:
            newroot = Node(newnode.left.value)
            newroot.right = Node(newnode.value)
            newroot.left = newnode.left.left
            newroot.right.right = newnode.right
            newroot.right.left = newnode.left.right
            return newroot
        else:
            return newnode

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)
        elif value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)
        else:
            print("Cannot insert value")

        if AVLTree._is_avl_satisfied(node) is False:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            return AVLTree._rebalance(node)
        else:
            return node

    def insert_list(self, xs):
        for i in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, i)
            else:
                self.root = Node(i)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        else:
            return node
