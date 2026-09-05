from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    resultados = []
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        j = i + 1
        k = n - 1
        
        while j < k:
            suma = nums[i] + nums[j] + nums[k]
            if suma == 0:
                resultados.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif suma < 0:
                j += 1
            else:
                k -= 1
                
    return resultados

if __name__ == "__main__":
    lista = [-1, 0, 1, 2, -1, -4]
    respuesta = three_sum(lista)
    print("Triplets que suman 0:", respuesta)