import pytest
from src.juice import Juice

def test_juice_initialization():
    """ジュースの初期化が正しく行われることを確認"""
    juice = Juice("ペプシ", 150)
    assert juice.get_name() == "ペプシ"
    assert juice.get_price() == 150

def test_set_juice_price():
    """ジュースの価格が正しく取得できることを確認"""
    juice = Juice("モンスター", 230)
    juice.set_price(250)
    assert juice.get_price() == 250

def test_set_juice_name():
    """ジュースの名前が正しく取得できることを確認"""
    juice = Juice("いろはす", 120)
    juice.set_name("コーラ")
    assert juice.get_name() == "コーラ"

if __name__ == "__main__":
    pytest.main() 