"""
ジュースを表すモジュール
"""

class Juice:
    """
    ジュースを表すクラス
    """
    def __init__(self, name, price):
        """
        ジュースを初期化します。
        
        Args:
            name (str): ジュースの名前
            price (int): ジュースの価格
        """
        self.__name = name
        self.__price = price
    
    def get_name(self):
        """
        ジュースの名前を取得します。
        
        Returns:
            str: ジュースの名前
        """
        return self.__name
    
    def set_name(self, name):
        """
        ジュースの名前を設定します。
        """
        self.__name = name
    
    def get_price(self):
        """
        ジュースの価格を取得します。
        
        Returns:
            int: ジュースの価格
        """
        return self.__price 
    
    def set_price(self, price):
        """
        ジュースの価格を設定します。
        """
        self.__price = price

