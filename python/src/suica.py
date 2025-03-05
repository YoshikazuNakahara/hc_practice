"""
Suicaカードを表すモジュール
"""

class Suica:
    """
    Suicaカードを表すクラス
    """
    def __init__(self, initial_charge=500):
        """
        Suicaカードを初期化します。
        
        Args:
            initial_charge (int): 初期チャージ金額 (デフォルト: 500円)
        """
        if initial_charge < 0:
            raise ValueError("初期チャージ金額は0以上である必要があります。")
        
        self.__charge = initial_charge
    
    def charge(self, amount):
        """
        Suicaにチャージします。
        
        Args:
            amount (int): チャージ金額
        
        Raises:
            ValueError: 100円未満のチャージ時
        """
        if amount < 100:
            raise ValueError("チャージ金額は100円以上である必要があります。")
        
        self.__charge += amount
    
    def get_charge(self):
        """
        現在のチャージ残高を取得します。
        
        Returns:
            int: チャージ残高
        """
        return self.__charge
    
    def pay(self, amount):
        """
        Suicaから支払いを行います。
        
        Args:
            amount (int): 支払い金額
        
        Raises:
            ValueError: チャージ残高が不足している場合
        """
        if self.__charge < amount:
            raise ValueError("チャージ残高が不足しています。")
        
        self.__charge -= amount 