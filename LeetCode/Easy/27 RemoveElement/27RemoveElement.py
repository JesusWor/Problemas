from typing import List

def remove_element(nums: List[int], val: int) -> int:
    k = 0 
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
            
    return k

if __name__ == "__main__":
    lista = [0, 1, 2, 2, 3, 0, 4, 2]
    valor_a_eliminar = 2
    
    k = remove_element(lista, valor_a_eliminar)
    
    print(f"Nueva longitud k: {k}")
    print(f"Lista modificada: {lista[:k]}")