#include <iostream>

class Solution {
public:
    int divide(int dividend, int divisor) {
        // Evitar el caso de desbordamiento
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        bool negative = false;
        long long dvs = divisor,
                  dvd = dividend,
                  ans = 0;
        if (divisor < 0) {
            dvs = -dvs;
            negative = !negative;
        }
        if (dividend < 0) {
            dvd = -dvd;
            negative = !negative;
        }
        while (dvd >= dvs) {
            long long temp = dvs, multiple = 1;
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            ans += multiple;
        }
        return negative ? -ans : ans;
    }
};

int main() {
    Solution sol;

    // Salida 1 su output seria 3
    int dividend = 10, divisor = 3;
    std::cout<<"Prueba de salida 1: "<<sol.divide(dividend, divisor)<<std::endl;

    // Salida 2 su output seria -2
    dividend = 7, divisor = -3;
    std::cout<<"Prueba de salida 1: "<<sol.divide(dividend, divisor)<<std::endl;

    // Salida 3 caso de excepcion su output seria 2147483647
    dividend = -2147483648, divisor = -1;
    std::cout<<"Prueba de salida 1: "<<sol.divide(dividend, divisor)<<std::endl;

    return 0;
}