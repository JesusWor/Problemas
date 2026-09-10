def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


def main():
    nums = [3, 2, 2, 3]
    val = 3

    k = remove_element(nums, val)

    print(f"Nueva longitud k: {k}")
    print("Arreglo modificado:", " ".join(str(nums[i]) for i in range(k)))


if __name__ == "__main__":
    main()