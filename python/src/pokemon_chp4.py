"""
Chapter2: クラスとは
"""

class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name  # 名前
        self.type1 = type1  # タイプ1
        self.type2 = type2  # タイプ2
        self.hp = hp  # ヒットポイント
        self.mp = 10  # マジックポイント（デフォルト値）

    def attack(self):
        print(f"{self.name} のこうげき!")

class Pikachu(Pokemon):
    def __init__(self, name="ピカチュウ", type1="でんき", type2="", hp=100):
        super().__init__(name, type1, type2, hp)  # 親クラスのコンストラクタを呼び出す

    def attack(self):
        super().attack()  # 親クラスのattackメソッドを呼び出す
        print(f"{self.name} の10万ボルト!")  # 親のメッセージに追加

if __name__ == "__main__":
    pika = Pikachu()  # Pikachuのインスタンスを作成

    print(pika.name)  # ピカチュウ
    pika.attack()  # ピカチュウ のこうげき! ピカチュウ の10万ボルト!
