"""
自動販売機システムモジュール

このモジュールは、Suicaと自動販売機の基本的な機能を実装します。
"""
from src.suica import Suica

class VendingMachine:
    """
    自動販売機を表すクラス。

    このクラスは、ドリンクの購入、在庫管理、売上の追跡を行います。
    ドリンクの価格は固定されており、在庫は初期化時に設定されます。

    Attributes:
        __sales (int): 現在の売上金額。
        __stock (dict): 各ドリンクの在庫数を保持する辞書。
    """
    
    # ドリンク価格表
    __DRINK_PRICES = {
        "ペプシ": 150,
        "モンスター": 230,
        "いろはす": 120
    }
    
    def __init__(self):
        """
        自動販売機を初期化します。
        売上金額と在庫を設定します。
        """
        # 売上金額
        self.__sales = 0
        # 在庫
        self.__stock = {
            "ペプシ": 5,
            "モンスター": 5,
            "いろはす": 5
        }
    
    def get_sales(self):
        """
        現在の売上金額を取得します。
        
        Returns:
            int: 売上金額
        """
        return self.__sales
    
    def get_stock(self, drink_name):
        """
        指定されたドリンクの在庫数を取得します。
        
        Args:
            drink_name (str): ドリンクの名前
        
        Returns:
            int: 在庫数
        """
        return self.__stock.get(drink_name, 0)
    
    def get_available_drinks(self):
        """
        購入可能なドリンクのリストを取得します。
        
        Returns:
            list: 購入可能なドリンクのリスト
        """
        return [
            name for name, count in self.__stock.items() 
            if count > 0
        ]
    
    def can_purchase(self, drink_name, suica):
        """
        指定されたドリンクが購入可能かを確認します。
        
        Args:
            drink_name (str): ドリンクの名前
            suica (Suica): 支払いに使用するSuicaカード
        
        Returns:
            bool: 購入可能な場合はTrue、そうでない場合はFalse
        """
        if drink_name not in self.__DRINK_PRICES.keys():
            return False
        
        if self.__stock[drink_name] <= 0: 
            return False
        
        drink_price = self.__DRINK_PRICES[drink_name]
        return suica.get_charge() >= drink_price
    
    def purchase(self, drink_name, suica):
        """
        ドリンクを購入します。
        
        Args:
            drink_name (str): ドリンクの名前
            suica (Suica): 支払いに使用するSuicaカード
        
        Raises:
            ValueError: 購入できない場合
        """
        if not self.can_purchase(drink_name, suica):
            raise ValueError("購入できません。")
        
        # ドリンクの価格を取得
        drink_price = self.__DRINK_PRICES[drink_name]
        
        # Suicaから支払い
        suica.pay(drink_price)
        
        # 売上を増やす
        self.__sales += drink_price
        
        # 在庫を減らす
        self.__stock[drink_name] -= 1
    
    def add_stock(self, drink_name, count):
        """
        指定されたドリンクの在庫を補充します。
        
        Args:
            drink_name (str): ドリンクの名前
            count (int): 補充する本数
        
        Raises:
            ValueError: 存在しないドリンクの場合
        """
        if drink_name not in self.__DRINK_PRICES:
            raise ValueError(f"{drink_name}は販売していません。")
        
        self.__stock[drink_name] += count

def main():
    """
    自動販売機システムのデモンストレーション
    """
    # Suicaの作成
    suica = Suica()
    
    # 自動販売機の作成
    machine = VendingMachine()
    
    # 追加チャージ
    suica.charge(500)
    
    # 購入可能なドリンクの確認
    print("購入可能なドリンク:", machine.get_available_drinks())
    
    # ペプシの購入
    machine.purchase("ペプシ", suica)
    
    # 売上と残高の確認
    print("売上:", machine.get_sales())
    print("Suica残高:", suica.get_charge())
    
    # 在庫補充
    machine.add_stock("ペプシ", 3)
    print("ペプシの在庫:", machine.get_stock("ペプシ"))

if __name__ == "__main__":
    main() 