#include <iostream>
#include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    void helper(TreeNode* node, std::vector<int>& result) {
        if (!node) return;
        helper(node->left, result);
        result.push_back(node->val);
        helper(node->right, result);
    }

public:
    std::vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        helper(root, result);
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);

    Solution sol;
    std::vector<int> result = sol.inorderTraversal(root);

    std::cout << "Resultado Inorder: ";
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}