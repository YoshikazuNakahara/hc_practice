import pytest
from src.vending_machine import VendingMachine
from src.suica import Suica
from src.juice import Juice

def test_initial_sales():
    """自動販売機の初期売上が0であることを確認"""
    machine = VendingMachine()
    assert machine.get_sales() == 0

def test_initial_stock():
    """自動販売機の初期在庫が正しいことを確認"""
    machine = VendingMachine()
    assert machine.get_stock("ペプシ") == 5
    assert machine.get_stock("モンスター") == 5
    assert machine.get_stock("いろはす") == 5

def test_purchase_success():
    """ペプシを購入できることを確認"""
    suica = Suica()  # 初期チャージ500円
    machine = VendingMachine()
    
    machine.purchase("ペプシ", suica)
    
    assert machine.get_sales() == 150  # 売上が150円になる
    assert suica.get_charge() == 350  # Suica残高が350円になる
    assert machine.get_stock("ペプシ") == 4  # 在庫が1本減る

def test_purchase_insufficient_balance():
    """チャージ残高が不足している場合に例外が発生することを確認"""
    suica = Suica()  # 初期チャージ500円
    machine = VendingMachine()
    
    # Suicaの残高を減らすために、ペプシの価格よりも少ない金額を支払う
    suica.pay(400)  # 残高は100円になる
    
    with pytest.raises(ValueError, match="購入できません。"):
        machine.purchase("ペプシ", suica)  # 残高が不足しているため購入できない

def test_purchase_out_of_stock():
    """在庫がない場合に例外が発生することを確認"""
    suica = Suica(1000)  # 初期チャージ1000円
    machine = VendingMachine()
    
    # ペプシを5回購入して在庫を0にする
    for _ in range(5):
        machine.purchase("ペプシ", suica)
    
    # 在庫が0になったので、再度購入を試みる
    with pytest.raises(ValueError, match="購入できません。"):
        machine.purchase("ペプシ", suica)

def test_purchase_non_existent_drink():
    """存在しないドリンクを購入しようとした場合に例外が発生することを確認"""
    suica = Suica()  # 初期チャージ500円
    machine = VendingMachine()
    
    with pytest.raises(ValueError, match="購入できません。"):
        machine.purchase("存在しないドリンク", suica)

def test_pay_insufficient_balance_zero():
    """チャージ残高がゼロの場合に例外が発生することを確認"""
    suica = Suica()  # 初期チャージ500円
    suica.pay(500)   # 残高をゼロにする
    
    with pytest.raises(ValueError, match="購入できません。"):
        machine = VendingMachine()
        machine.purchase("ペプシ", suica)  # 残高が不足しているため購入できない

def test_add_stock():
    """在庫を補充できることを確認"""
    machine = VendingMachine()
    machine.add_stock("ペプシ", 3)
    assert machine.get_stock("ペプシ") == 8  # 在庫が8本になる

def test_juice_initialization():
    """ジュースの初期化が正しく行われることを確認"""
    juice = Juice("ペプシ", 150)
    assert juice.get_name() == "ペプシ"
    assert juice.get_price() == 150

if __name__ == "__main__":
    pytest.main() 