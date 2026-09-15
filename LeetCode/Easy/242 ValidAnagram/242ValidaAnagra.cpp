#include <iostream>
#include <unordered_map>
#include <string>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if(s.length() != t.length()) return false;

        std::unordered_map<char, int> mapa;
        // meter s en el mapa caracter por caracter
        for(char c:s) {
            mapa[c]++;
        }
        // comparar que la letra de t este en el mapa
        for(char c:t) {
            // si la letra que se esta comparando no existe o ya se usaron todas las letras regresa false
            if(mapa.find(c) == mapa.end() || mapa[c] == 0) {
                return false;
            }
            mapa[c]--;
        }
        return true;
    }
};

int main() {
    Solution sol;
    std::string s = "anagram", 
                t = "nagaram";
    // Salida esperada: true;
    std::cout<<"Salida ejemplo 1: "<<sol.isAnagram(s,t)<<std::endl;

    std::string s = "rat", 
                t = "car";
    // Salida esperada: false;
    std::cout<<"Salida ejemplo 2: "<<sol.isAnagram(s,t)<<std::endl;


    return 0;
}
