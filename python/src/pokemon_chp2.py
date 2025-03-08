class Pokemon:
    def __init__(self):
        self.name = "リザードン"  # 名前
        self.type1 = "ほのお"     # タイプ1
        self.type2 = "ひこう"     # タイプ2
        self.hp = 100             # ヒットポイント
        self.mp = 10              # マジックポイント（追加）

    def attack(self):
        print(f"{self.name} のこうげき!")

if __name__ == "__main__":
    poke = Pokemon()

    print(poke.name)   # リザードン
    print(poke.type1)  # ほのお
    poke.attack()      # リザードン のこうげき！
    print(poke.mp)     # 10
