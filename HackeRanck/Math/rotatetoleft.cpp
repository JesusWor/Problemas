#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> rotLeft(std::vector<int> a, int d)
{
    std::rotate(a.begin(), a.begin() + d, a.end());
    return a;
}

int main()
{
    std::vector<int> vec = {1, 2, 3, 4, 5};
    int d = 2;

    std::vector<int> rotated = rotLeft(vec, d);

    for (int num : rotated)
    {
        std::cout << num << " ";
    }

    return 0;
}