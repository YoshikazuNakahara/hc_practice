"""
Chapter2: クラスとは
"""

from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, name, type1, type2, hp):
        self.name = name  # 名前
        self.type1 = type1  # タイプ1
        self.type2 = type2  # タイプ2
        self.hp = hp  # ヒットポイント

    @abstractmethod
    def attack(self):
        pass  # 抽象メソッドとして定義

class Pikachu(Pokemon):
    def __init__(self, name="ピカチュウ", type1="でんき", type2="", hp=100):
        super().__init__(name, type1, type2, hp)  # 親クラスのコンストラクタを呼び出す

    def attack(self):
        parent_attack_message = f"{self.name} のこうげき!"  # 親クラスの攻撃メッセージ
        return f"{parent_attack_message} そして、{self.name} の10万ボルト!"  # 攻撃メッセージを返す

if __name__ == "__main__":
    pika = Pikachu()  # Pikachuのインスタンスを作成

    print(pika.name)  # ピカチュウ
    print(pika.attack())  # ピカチュウ のこうげき! そして、ピカチュウ の10万ボルト!
