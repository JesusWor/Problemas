import java.util.List;
import java.util.ArrayList;

class BinaryTreeInorderTraversal94 {
    // TreeNode ahora vive DENTRO de esta clase, no compite por nombre
    // con el TreeNode de otros archivos del mismo paquete/carpeta.
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private void helper(TreeNode node, List<Integer> result) {
        if (node == null) return;
        helper(node.left, result);
        result.add(node.val);
        helper(node.right, result);
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        helper(root, result);
        return result;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        BinaryTreeInorderTraversal94 sol = new BinaryTreeInorderTraversal94();
        List<Integer> result = sol.inorderTraversal(root);

        System.out.print("Resultado Inorder: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}