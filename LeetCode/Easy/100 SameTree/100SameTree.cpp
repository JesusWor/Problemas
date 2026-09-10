    #include <iostream>
    #include <vector>

    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };

    // Construye un árbol desde un vector estilo LeetCode, donde -9999 representa null de forma automatia
    TreeNode* buildTree(const std::vector<int>& values) {
        if (values.empty() || values[0] == -9999) return nullptr;

        TreeNode* root = new TreeNode(values[0]);
        std::vector<TreeNode*> nodes = {root};
        size_t i = 1;

        for (size_t idx = 0; idx < nodes.size() && i < values.size(); idx++) {
            TreeNode* current = nodes[idx];

            if (i < values.size()) {
                if (values[i] != -9999) {
                    current->left = new TreeNode(values[i]);
                    nodes.push_back(current->left);
                }
                i++;
            }

            if (i < values.size()) {
                if (values[i] != -9999) {
                    current->right = new TreeNode(values[i]);
                    nodes.push_back(current->right);
                }
                i++;
            }
        }

        return root;
    }

    void freeTree(TreeNode* root) {
        if (!root) return;
        freeTree(root->left);
        freeTree(root->right);
        delete root;
    }

    class Solution {
    public:
        bool isSameTree(TreeNode* p, TreeNode* q) {
            if(p == nullptr && q == nullptr) {return true;}
            if(p == nullptr || q == nullptr) {return false;}
            if(p->val != q->val) {return false;}
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right); 
        }
    };


    int main() {
        Solution sol;

        // Caso 1: iguales -> true
        TreeNode* p1 = buildTree({1, 2, 3});
        TreeNode* q1 = buildTree({1, 2, 3});
        std::cout << "Caso 1 (esperado 1): " << sol.isSameTree(p1, q1) << std::endl;

        // Caso 2: distinta estructura -> false
        TreeNode* p2 = buildTree({1, 2});
        TreeNode* q2 = buildTree({1, -9999, 2});
        std::cout << "Caso 2 (esperado 0): " << sol.isSameTree(p2, q2) << std::endl;

        // Caso 3: mismo valor distinto en un nodo -> false
        TreeNode* p3 = buildTree({1, 2, 1});
        TreeNode* q3 = buildTree({1, 1, 2});
        std::cout << "Caso 3 (esperado 0): " << sol.isSameTree(p3, q3) << std::endl;

        // Caso 4: ambos vacíos -> true
        TreeNode* p4 = buildTree({});
        TreeNode* q4 = buildTree({});
        std::cout << "Caso 4 (esperado 1): " << sol.isSameTree(p4, q4) << std::endl;

        freeTree(p1); freeTree(q1);
        freeTree(p2); freeTree(q2);
        freeTree(p3); freeTree(q3);

        return 0;
    }