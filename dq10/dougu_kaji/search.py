import critical
import range_hits
import recipes
import temperatures

"""
最大ダメージ<最低基準値　かつ　最低ダメージx2>最大基準値になる箇所を探しており、以下のような特徴があります
会心が出た時は必ず本会心になる
会心が出なかったときでも基準値未満になり再度狙い打ちを狙ったり、このプログラムで再度探すことができる

結果は複数表示しているため集中力や他の箇所の処理は個人で判断するとなお良い

入力
search関数: レシピ名　温度　現在の数値
search(
    recipes.tyo_kagayakijueki, 
    "2000c", 
    {'A': 100, 'B': 100, 'C': 100, 'D': 100, 'E': 100, 'F': 100}
)

未実装
基準値内での弱狙い打ち
1.0, 1.2, 0.5以外の打ち方
威力2倍、半減ターン
6か所以外のレシピはその箇所を0にすれば動くはずだが未確認
"""
# recipes.tyo_kagayakijueki, "2000c", {'A': 100, 'B': 100, 'C': 100, 'D': 100, 'E': 100, 'F': 100}
def search_critical(recipe: dict, temp: str, current_num: dict):
    # 上下狙い
    for i in range_hits.top_and_bottom:
        critical_check = True  # Trueのままだと狙う
        for j in range(0, 1):  # ACの判定
            #
            if not critical.critical(
                    recipe=recipes.tyo_kagayakijueki[i[j]],
                    current_num=current_num[i[j]],
                    hit=temperatures.temps[temp]["1.2"]
            ):
                critical_check = False
        if critical_check:
            print("上下狙い打ち:", i)
    # 狙い打ち
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:  # 全箇所
        critical_check = True
        if not critical.critical(
                recipe=recipes.tyo_kagayakijueki[i],
                current_num=current_num[i],
                hit=temperatures.temps[temp]["0.5"]
        ):
            critical_check = False
        if critical_check:
            print("狙い打ち:", i)
    # 弱狙い打ち
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:  # 全箇所
        critical_check = True
        if not critical.critical(
                recipe=recipes.tyo_kagayakijueki[i],
                current_num=current_num[i],
                hit=temperatures.temps[temp]["1.0"]
        ):
            critical_check = False
        if critical_check:
            print("弱狙い打ち:", i)


# こすぱがいい
def search_neppu(recipe: dict, temp: str, current_num: dict):
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:  # 全箇所
        critical_check = True
        if not critical.critical(
                recipe=recipes.tyo_kagayakijueki[i],
                current_num=current_num[i],
                hit=temperatures.temps[temp]["2.5"]
        ):
            critical_check = False
        if critical_check:
            print("熱風おろし:", i)