import pytest
from src.suica import Suica

def test_initial_charge_valid():
    """初期チャージが500円であることを確認"""
    suica = Suica()
    assert suica.get_charge() == 500

def test_initial_charge_invalid():
    """初期チャージが0円未満の場合に例外が発生することを確認"""
    with pytest.raises(ValueError, match="初期チャージ金額は0以上である必要があります。"):
        Suica(-100)

def test_charge_and_multiple_charges():
    """100円以上のチャージと複数回のチャージが成功することを確認"""
    suica = Suica()
    suica.charge(100)  # 600円にする
    assert suica.get_charge() == 600
    
    suica.charge(200)  # 800円にする
    suica.charge(300)  # 1100円にする
    assert suica.get_charge() == 1100  # 500 + 100 + 200 + 300

def test_pay_and_multiple_payments():
    """チャージ残高からの支払いが成功することを確認"""
    suica = Suica()
    suica.charge(300)  # 800円にする
    suica.pay(200)      # 600円にする
    assert suica.get_charge() == 600
    suica.pay(300)      # 300円にする
    assert suica.get_charge() == 300

def test_multiple_charges_and_multiple_payments():
    """複数回のチャージと複数回の支払いが成功することを確認"""
    suica = Suica()
    suica.charge(100)  # 600円にする
    suica.charge(200)  # 800円にする
    suica.charge(300)  # 1100円にする
    assert suica.get_charge() == 1100  # 500 + 100 + 200 + 300
    suica.pay(200)      # 900円にする
    suica.pay(300)      # 600円にする
    assert suica.get_charge() == 600

def test_pay_insufficient_balance():
    """チャージ残高が不足している場合に例外が発生することを確認"""
    suica = Suica()
    with pytest.raises(ValueError, match="チャージ残高が不足しています。"):
        suica.pay(600)  # 500円しかないので失敗

if __name__ == "__main__":
    pytest.main() 