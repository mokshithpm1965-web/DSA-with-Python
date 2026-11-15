"""
TREE PROGRAMS — STUDY NOTES

Binary-tree programs covered:
- Count total nodes
- Count leaf nodes
- Find height (edge-count convention: empty=-1, leaf=0)
- Find depth of a value (root depth=0)
- Check identical trees
- Check symmetry
- Sum all node values
- Find maximum and minimum in a binary tree
- Check whether a tree is balanced
- Mirror / invert a binary tree
- Print a tree

BST programs covered:
- Search, insertion, deletion
- Find minimum and maximum
- Validate a BST

Concepts:
- None means a child/subtree is empty.
- Every recursive call has its own local variables.
- A return ends that particular call and sends a result to its caller.
- Normal binary trees have no value-ordering rule.
- BST rule: smaller values go left; larger values go right.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value       # Store this node's value.
        self.left = None         # Initially, there is no left child.
        self.right = None        # Initially, there is no right child.


# COUNT ALL NODES
def count_nodes(root):
    if root is None:             # An empty subtree contains zero nodes.
        return 0                 # Return zero to the calling function.
    left_count = count_nodes(root.left)    # Count nodes in the left subtree.
    right_count = count_nodes(root.right)  # Count nodes in the right subtree.
    return 1 + left_count + right_count    # Current node (1) plus both subtree counts.


# COUNT LEAF NODES
def count_leaf_nodes(root):
    if root is None:             # An empty subtree has no leaves.
        return 0                 # Return zero leaves.
    if root.left is None and root.right is None:  # A leaf has no children.
        return 1                 # Count the current leaf.
    left_count = count_leaf_nodes(root.left)      # Count leaves on the left.
    right_count = count_leaf_nodes(root.right)    # Count leaves on the right.
    return left_count + right_count               # Add both leaf counts.


# HEIGHT: measured in edges, so empty=-1 and a leaf=0.
def get_height(root):
    if root is None:             # Reached an empty child position.
        return -1                # This makes a leaf's height equal zero.
    left_height = get_height(root.left)    # Calculate left subtree height.
    right_height = get_height(root.right)  # Calculate right subtree height.
    return 1 + max(left_height, right_height)  # One edge plus the taller side.


# DEPTH: root starts at zero; return -1 when the value is not found.
def find_depth(root, target, depth=0):
    if root is None:             # Target was not found in this empty subtree.
        return -1                # -1 means "not found".
    if root.value == target:     # Check the current node.
        return depth             # Return this node's depth.
    left_result = find_depth(root.left, target, depth + 1)  # Search left one level deeper.
    if left_result != -1:        # Check whether the left search found the target.
        return left_result       # Pass the found depth back to the caller.
    return find_depth(root.right, target, depth + 1)  # Otherwise search the right subtree.


# CHECK WHETHER TWO TREES ARE IDENTICAL.
def is_identical(root1, root2):
    if root1 is None and root2 is None:  # Both corresponding positions are empty.
        return True                      # These positions match.
    if root1 is None or root2 is None:   # Only one corresponding position is empty.
        return False                     # Their shapes differ.
    if root1.value != root2.value:       # Compare the current node values.
        return False                     # Different values mean not identical.
    return (is_identical(root1.left, root2.left) and  # Compare left subtrees...
            is_identical(root1.right, root2.right))   # ...and right subtrees.


# HELPER FOR SYMMETRY: compare two subtrees as mirror images.
def is_mirror(left, right):
    if left is None and right is None:  # Both mirror positions are empty.
        return True                     # They match.
    if left is None or right is None:   # Only one mirror position is empty.
        return False                    # They do not match.
    if left.value != right.value:       # Mirror-position values must be equal.
        return False                    # Unequal values break symmetry.
    return (is_mirror(left.left, right.right) and  # Left side matches opposite right...
            is_mirror(left.right, right.left))     # ...and right matches opposite left.


# CHECK WHETHER THE WHOLE TREE IS SYMMETRICAL.
def is_symmetric(root):
    if root is None:             # An empty tree is symmetrical.
        return True              # Nothing can break its symmetry.
    return is_mirror(root.left, root.right)  # Compare the root's two sides as mirrors.


# SUM ALL NODE VALUES.
def sum_nodes(root):
    if root is None:             # An empty subtree contributes nothing.
        return 0                 # Sum of an empty subtree is zero.
    left_sum = sum_nodes(root.left)    # Sum values in the left subtree.
    right_sum = sum_nodes(root.right)  # Sum values in the right subtree.
    return root.value + left_sum + right_sum  # Add current value and both sums.


# MAXIMUM VALUE IN AN ORDINARY BINARY TREE.
def find_max(root):
    if root is None:             # Empty subtree has no actual maximum.
        return float("-inf")     # Negative infinity is below every real value.
    left_max = find_max(root.left)     # Find maximum on the left.
    right_max = find_max(root.right)   # Find maximum on the right.
    return max(root.value, left_max, right_max)  # Compare current, left, and right.


# MINIMUM VALUE IN AN ORDINARY BINARY TREE.
def find_min(root):
    if root is None:             # Empty subtree has no actual minimum.
        return float("inf")      # Positive infinity is above every real value.
    left_min = find_min(root.left)     # Find minimum on the left.
    right_min = find_min(root.right)   # Find minimum on the right.
    return min(root.value, left_min, right_min)  # Compare current, left, and right.


# CHECK WHETHER THE TREE IS HEIGHT-BALANCED.
def is_balanced(root):
    if root is None:             # An empty tree is balanced.
        return True              # No node violates the balance rule.
    left_height = get_height(root.left)    # Calculate left subtree height.
    right_height = get_height(root.right)  # Calculate right subtree height.
    if abs(left_height - right_height) > 1:  # abs() removes a negative sign.
        return False             # A height difference greater than one is unbalanced.
    return is_balanced(root.left) and is_balanced(root.right)  # Check all lower nodes too.


# MIRROR / INVERT THE TREE IN PLACE.
def invert_tree(root):
    if root is None:             # Stop at an empty child position.
        return None              # There is no node here to invert.
    root.left, root.right = root.right, root.left  # Swap the child references.
    invert_tree(root.left)       # Invert the subtree now attached on the left.
    invert_tree(root.right)      # Invert the subtree now attached on the right.
    return root                  # Return the same, now-modified root object.


# PRINT TREE IN PREORDER: current node, left subtree, right subtree.
def print_tree(root):
    if root is None:             # Empty positions have nothing to print.
        return                   # End this particular recursive call.
    print(root.value, end=" ")   # Print the current node first.
    print_tree(root.left)        # Then print the entire left subtree.
    print_tree(root.right)       # Finally print the entire right subtree.


# BST SEARCH.
def bst_search(root, target):
    if root is None:             # Reached an empty position; target is absent.
        return None              # None means not found.
    if root.value == target:     # Check the current node.
        return root              # Return the matching node.
    if target < root.value:      # Smaller values can only be on the left.
        return bst_search(root.left, target)  # Continue searching left.
    return bst_search(root.right, target)     # Otherwise continue searching right.


# BST INSERTION.
def bst_insert(root, value):
    if root is None:             # Found the empty position for the new value.
        return TreeNode(value)   # Create and return the new node.
    if value < root.value:       # Smaller values belong on the left.
        root.left = bst_insert(root.left, value)  # Insert and reconnect left subtree.
    elif value > root.value:     # Larger values belong on the right.
        root.right = bst_insert(root.right, value)  # Insert and reconnect right subtree.
    return root                  # Return this subtree's root; duplicates are ignored.


# BST MINIMUM NODE: the minimum is the leftmost node.
def bst_min_node(root):
    if root is None:             # Empty tree has no minimum node.
        return None              # Return None.
    while root.left is not None: # Keep moving left while possible.
        root = root.left         # Move the local reference one step left.
    return root                  # Return the leftmost node.


# BST MAXIMUM NODE: the maximum is the rightmost node.
def bst_max_node(root):
    if root is None:             # Empty tree has no maximum node.
        return None              # Return None.
    while root.right is not None:  # Keep moving right while possible.
        root = root.right        # Move the local reference one step right.
    return root                  # Return the rightmost node.


# BST DELETION: handles leaf, one-child, and two-child cases.
def bst_delete(root, value):
    if root is None:             # Value does not exist in this subtree.
        return None              # Leave this empty position unchanged.
    if value < root.value:       # Target is smaller, so search left.
        root.left = bst_delete(root.left, value)  # Reconnect updated left subtree.
    elif value > root.value:     # Target is larger, so search right.
        root.right = bst_delete(root.right, value)  # Reconnect updated right subtree.
    else:                        # Current node is the one to delete.
        if root.left is None:    # No left child: zero-child or right-child case.
            return root.right    # Replace current node with its right child.
        if root.right is None:   # No right child, but a left child exists.
            return root.left     # Replace current node with its left child.
        successor = bst_min_node(root.right)  # Smallest node in right subtree.
        root.value = successor.value          # Copy successor value into current node.
        root.right = bst_delete(root.right, successor.value)  # Delete copied successor.
    return root                  # Return the updated subtree root.


# VALIDATE BST USING LOWER AND UPPER BOUNDS.
def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:             # An empty subtree is valid.
        return True              # No value violates the rule.
    if not (low < root.value < high):  # Current value must fit inside its allowed range.
        return False             # Value outside the range makes this invalid.
    return (is_valid_bst(root.left, low, root.value) and  # Left values must be smaller.
            is_valid_bst(root.right, root.value, high))  # Right values must be larger.


# INORDER DISPLAY: for a BST, this prints values in ascending order.
def print_inorder(root):
    if root is None:             # Stop at an empty child position.
        return                   # Nothing to print here.
    print_inorder(root.left)     # Print smaller values first.
    print(root.value, end=" ")   # Print the current value.
    print_inorder(root.right)    # Then print larger values.


# DEMONSTRATION: these calls run from top to bottom when the file is executed.
if __name__ == "__main__":
    # Build the example binary tree used in our lessons.
    root = TreeNode(10)           # Create root node 10.
    root.left = TreeNode(5)       # Attach 5 as the left child of 10.
    root.right = TreeNode(15)     # Attach 15 as the right child of 10.
    root.left.left = TreeNode(2)  # Attach 2 as the left child of 5.
    root.left.right = TreeNode(7) # Attach 7 as the right child of 5.

    print("Original tree:", end=" ")  # Print a label without a line break.
    print_tree(root)                  # Expected preorder: 10 5 2 7 15.
    print()                           # Move to a new line.

    print("Total nodes:", count_nodes(root))       # Expected: 5.
    print("Leaf nodes:", count_leaf_nodes(root))   # Expected: 3 (2, 7, 15).
    print("Height:", get_height(root))             # Expected: 2 edges.
    print("Depth of 7:", find_depth(root, 7))      # Expected: 2.
    print("Sum:", sum_nodes(root))                 # Expected: 39.
    print("Maximum:", find_max(root))              # Expected: 15.
    print("Minimum:", find_min(root))              # Expected: 2.
    print("Balanced:", is_balanced(root))          # Expected: True.

    # Build a second tree with the same structure and values.
    same = TreeNode(10)           # Create the second root.
    same.left = TreeNode(5)       # Match the first tree's left child.
    same.right = TreeNode(15)     # Match the first tree's right child.
    same.left.left = TreeNode(2)  # Match the left-left node.
    same.left.right = TreeNode(7) # Match the left-right node.
    print("Identical:", is_identical(root, same))  # Expected: True.

    # Build a symmetric tree whose opposite sides are mirror images.
    symmetric = TreeNode(1)        # Create its root.
    symmetric.left = TreeNode(2)  # Add left child 2.
    symmetric.right = TreeNode(2) # Add right child 2.
    symmetric.left.left = TreeNode(3)    # Add 3 at outer-left.
    symmetric.right.right = TreeNode(3)  # Add 3 at outer-right.
    print("Symmetric:", is_symmetric(symmetric))  # Expected: True.

    # Invert the original tree; this modifies the existing nodes.
    invert_tree(root)              # Swap left/right links at every node.
    print("After inversion:", end=" ")
    print_tree(root)               # Expected preorder: 10 15 5 7 2.
    print()

    # Build a separate BST using insertion.
    bst_root = None                # Start with an empty BST.
    for value in [10, 5, 15, 2, 7, 12, 20]:  # Values to insert.
        bst_root = bst_insert(bst_root, value)  # Keep the returned root.

    found = bst_search(bst_root, 7)  # Search for value 7.
    print("BST search for 7:", found.value if found else None)  # Expected: 7.

    smallest = bst_min_node(bst_root)  # Find the leftmost BST node.
    largest = bst_max_node(bst_root)   # Find the rightmost BST node.
    print("BST minimum:", smallest.value if smallest else None)  # Expected: 2.
    print("BST maximum:", largest.value if largest else None)    # Expected: 20.
    print("Valid BST:", is_valid_bst(bst_root))  # Expected: True.

    print("BST sorted values:", end=" ")  # Label sorted output.
    print_inorder(bst_root)                # Expected: 2 5 7 10 12 15 20.
    print()

    bst_root = bst_delete(bst_root, 15)  # Delete 15 and save the returned root.
    print("BST after deleting 15:", end=" ")
    print_inorder(bst_root)                # Expected: 2 5 7 10 12 20.
    print()
