from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self):
        self._name = ""  # プライベート変数として名前を定義

    @property
    @abstractmethod
    def type1(self):
        pass  # 抽象プロパティ

    @property
    @abstractmethod
    def type2(self):
        pass  # 抽象プロパティ

    @property
    @abstractmethod
    def hp(self):
        pass  # 抽象プロパティ

    @abstractmethod
    def attack(self):
        pass  # 抽象メソッド

    def change_name(self, new_name: str):
        # 不適切な名前はエラー
        if new_name == "うんこ":
            print("不適切な名前です")
            return
        self._name = new_name  # 名前を変更

    def get_name(self) -> str:
        return self._name  # 名前を取得

class Pikachu(Pokemon):
    def __init__(self, type1="でんき", type2="", hp=100):
        super().__init__()  # 親クラスのコンストラクタを呼び出す
        self._type1 = type1  # タイプ1
        self._type2 = type2  # タイプ2
        self._hp = hp  # ヒットポイント

    @property
    def type1(self):
        return self._type1  # タイプ1を返す

    @property
    def type2(self):
        return self._type2  # タイプ2を返す

    @property
    def hp(self):
        return self._hp  # ヒットポイントを返す

    def attack(self):
        return f"{self.get_name()} の10万ボルト!"  # 攻撃メッセージを返す

if __name__ == "__main__":
    pika = Pikachu()  # Pikachuのインスタンスを作成
    pika.change_name("ピカチュウ")  # 名前を変更
    print(pika.get_name())  # ピカチュウ
    print(pika.attack())  # ピカチュウ の10万ボルト!

    pika.change_name("テキセツ")
    print(pika.get_name())     # テキセツ

    pika.change_name("うんこ")   # 「不適切な名前です」と表示される
    print(pika.get_name())     # テキセツ のまま
