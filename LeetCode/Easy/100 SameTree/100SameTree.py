class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Helper de prueba: arma el arbol por niveles usando -9999 como marcador de null.
def build_tree(values: list[int]) -> TreeNode | None:
    if not values or values[0] == -9999:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    i = 1
    idx = 0

    while idx < len(nodes) and i < len(values):
        current = nodes[idx]

        if i < len(values):
            if values[i] != -9999:
                current.left = TreeNode(values[i])
                nodes.append(current.left)
            i += 1

        if i < len(values):
            if values[i] != -9999:
                current.right = TreeNode(values[i])
                nodes.append(current.right)
            i += 1

        idx += 1

    return root

def main():
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print(f"Caso 1 (esperado True): {is_same_tree(p1, q1)}")

    p2 = build_tree([1, 2])
    q2 = build_tree([1, -9999, 2])
    print(f"Caso 2 (esperado False): {is_same_tree(p2, q2)}")

    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print(f"Caso 3 (esperado False): {is_same_tree(p3, q3)}")

    p4 = build_tree([])
    q4 = build_tree([])
    print(f"Caso 4 (esperado True): {is_same_tree(p4, q4)}")


if __name__ == "__main__":
    main()