"""
Chapter2: クラスとは
"""

class Pokemon:
    def __init__(self, name="リザードン", type1="ほのお", type2="ひこう", hp=100, mp=10):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.mp = mp

    def attack(self):
        print(f"{self.name}の攻撃")
        
    def __del__(self):
        print(f"{self.name}が消去されました。")

if __name__ == "__main__":
    poke = Pokemon()

    print(poke.name)   # リザードン
    print(poke.type1)  # ほのお
    poke.attack()        # リザードン のこうげき！

    print(poke.mp)
