from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            suma = nums[i] + nums[j]
            if suma == target:
                return [i, j]
    return []

if __name__ == "__main__":
    lista = [2, 7, 11, 15]
    objetivo = 9
    
    resultado = two_sum(lista, objetivo)
    print("Índices:", resultado)