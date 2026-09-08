#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    std::string intToRoman(int num) {
        // Vector con las parejas de cada romano a entero
        const std::vector<std::pair<int, std::string>> val = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
            {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"},  {1, "I"}
        };

        std::string ans = ""; // Varaible para almacenar la salida
        for(const auto& pair : val) { // ciclo pra poder iterar y agregar la letra correpondiente y sacar el numero
            while (num >= pair.first) {
                ans += pair.second;
                num -= pair.first;
            }
        }
        return ans;
    }
};

int main() {
    Solution sol = Solution();
    int num = 3749; // salida esperada "MMMDCCXLIX"]
    std::string salida = sol.intToRoman(num);
    std::cout << "Salida: " << salida << std::endl;
    std::cout << (salida == "MMMDCCXLIX") ? true : false;
}