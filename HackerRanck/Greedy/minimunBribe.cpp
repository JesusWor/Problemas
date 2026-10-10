#include <iostream>
#include <vector>

void minimumBribes(std::vector<int> q)
{
    int bribes = 0;

    for (int i = 0; i < q.size(); i++)
    {
        if (q[i] - (i + 1) > 2)
        {
            std::cout << "Too chaotic" << std::endl;
            return;
        }

        // Contar los sobornos que recibió cada persona
        for (int j = std::max(0, q[i] - 2); j < i; j++)
        {
            if (q[j] > q[i])
                bribes++;
        }
    }

    std::cout << bribes << std::endl;
}

int main()
{
    std::vector<int> q = {2, 1, 5, 3, 4}; // Ejemplo
    minimumBribes(q);                     // Output esperado: 3
    return 0;
}