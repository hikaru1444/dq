import search, recipes, temperatures
import pprint
if __name__ == '__main__':
    """
    個人用
    超かがやき樹液
    手順
    温度上げx2
    1600cCDEF超4連打ち32~47
    温度上げx2
    2150cA熱風おろし
    2000cCDEF4連打ち18~27
    1950cB熱風おろし
    1800cEorF(66~76)熱風おろし42~63
    1650cどこでも叩き
    1600cABCD超4連打ち
    1550cどこでも熱風おろし
    1400cどこでも狙い打ち
    数値
    A155-161 B220-230
    C155-161 D220-230
    E140-150 F140-150
    """
    pprint.pprint(temperatures.temps, depth=3)
    search.search_critical(
        recipes.tyo_kagayakijueki,  # レシピ名
        "2000c",  # 温度
        {  # 数値
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0}
    )
