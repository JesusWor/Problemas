import java.util.List;
import java.util.ArrayList;

public class SameTree100 {
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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    // Helper de prueba: arma el arbol por niveles usando -9999 como marcador de null.
    private static TreeNode buildTree(List<Integer> values) {
        if (values.isEmpty() || values.get(0) == -9999) return null;

        TreeNode root = new TreeNode(values.get(0));
        List<TreeNode> nodes = new ArrayList<>();
        nodes.add(root);
        int i = 1;

        for (int idx = 0; idx < nodes.size() && i < values.size(); idx++) {
            TreeNode current = nodes.get(idx);

            if (i < values.size()) {
                if (values.get(i) != -9999) {
                    current.left = new TreeNode(values.get(i));
                    nodes.add(current.left);
                }
                i++;
            }

            if (i < values.size()) {
                if (values.get(i) != -9999) {
                    current.right = new TreeNode(values.get(i));
                    nodes.add(current.right);
                }
                i++;
            }
        }

        return root;
    }

    public static void main(String[] args) {
        SameTree100 sol = new SameTree100();

        TreeNode p1 = buildTree(List.of(1, 2, 3));
        TreeNode q1 = buildTree(List.of(1, 2, 3));
        System.out.println("Caso 1 (esperado true): " + sol.isSameTree(p1, q1));

        TreeNode p2 = buildTree(List.of(1, 2));
        TreeNode q2 = buildTree(List.of(1, -9999, 2));
        System.out.println("Caso 2 (esperado false): " + sol.isSameTree(p2, q2));

        TreeNode p3 = buildTree(List.of(1, 2, 1));
        TreeNode q3 = buildTree(List.of(1, 1, 2));
        System.out.println("Caso 3 (esperado false): " + sol.isSameTree(p3, q3));

        TreeNode p4 = buildTree(List.of());
        TreeNode q4 = buildTree(List.of());
        System.out.println("Caso 4 (esperado true): " + sol.isSameTree(p4, q4));
    }
}