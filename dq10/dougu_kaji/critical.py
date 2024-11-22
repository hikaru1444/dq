# 会心が出た時にはピッタリ、出なかったときは基準値未満かどうか判定する
# 基準値、現在数値、打ち方
def critical(recipe: list, current_num: int, hit: list):
    # 最低値+会心で本会心になり、最大値で基準値未満になる
    if current_num + hit[0] * 2 >= recipe[-1] and current_num + hit[-1] < recipe[0]:
        # 偽会心の可能性があるものは表示
        print("偽会心:", [i * 2 for i in hit])
        return True
    else:
        return False
