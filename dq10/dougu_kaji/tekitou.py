"""
超かがやきの樹液の序盤の打ち方
4連打ちなどの会心で余分に数値が伸びることは考慮しない
他に、温度や残り数値ごとの狙い打ち箇所判定作りたい
"""
import random
import temperatures
count = {'ok': 0, 'out': 0}
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

# 1000万回繰り返す
for i in range(0, 10000000):
    e, f = 0,0
    # 1600cCDEF超4連打ち
    e += random.choice(temperatures.temps["1600c"]["2.0"])  # [32, 34, 37, 39, 42, 45, 47]
    f += random.choice(temperatures.temps["1600c"]["2.0"])
    # 2000cCDEF4連打ち
    e += random.choice(temperatures.temps["2000c"]["1.2"])  # [23, 24, 26, 29, 30, 32, 33]
    f += random.choice(temperatures.temps["2000c"]["1.2"])
    # 1800cEFの高いほうに熱風おろし
    ef = max(e, f)
    # 最低値+会心で本会心になるまたは、最大値で基準値未満になる
    # ダメなパターンを引いたらカウントし、その数値を表示する
    if ef + 42 * 2 >= 150 and ef + 63 < 151:  # 66~76
        count['ok'] += 1
    else:
        # print("out!ef=", ef)
        count['out'] += 1

print(count)
