class Solution {
    private TreeNode first = null; // First misplaced node
    private TreeNode second = null; // Second misplaced node
    private TreeNode prev = null; // Keeps track of the previous node during traversal

    public void recoverTree(TreeNode root) {
        inorder(root);

        // Swap the values of the two nodes
        if (first != null && second != null) {
            int temp = first.val;
            first.val = second.val;
            second.val = temp;
        }
    }

    private void inorder(TreeNode node) {
        if (node == null) return;

        inorder(node.left); // Visit left subtree

        if (prev != null && prev.val > node.val) {
            if (first == null) {
                first = prev; // Mark the first violation
            }
            second = node; // Mark the second violation
        }
        prev = node; // Update `prev` to current node

        inorder(node.right); // Visit right subtree
    }
}