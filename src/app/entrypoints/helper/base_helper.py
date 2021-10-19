def calc_available_page(num: int, hit_num: int) -> int:
    if num <= 0:
        return 0
    if hit_num % num == 0:
        return hit_num // num
    return hit_num // num + 1
