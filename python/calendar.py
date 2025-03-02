"""
calendar.py

このモジュールは、指定された月と年のカレンダーを表示するシンプルなコマンドラインカレンダーアプリケーションを提供します。
月が指定されていない場合は、現在の月がデフォルトとなります。カレンダーは月曜日から始まります。
"""

import sys
import datetime

def validate_month(month_arg):
    """
    月の引数を検証します。

    引数:
        month_arg (str): 検証する月の引数。

    戻り値:
        int: 検証された月の番号。

    例外:
        SystemExit: 月が有効な番号または名前でない場合。
    """
    try:
        month = int(month_arg)
        if month < 1 or month > 12:
            print(f"{month_arg} is neither a month number (1..12) nor a name")
            sys.exit(1)
        return month
    except ValueError:
        print(f"{month_arg} is neither a month number (1..12) nor a name")
        sys.exit(1)

def get_calendar_month(year, month):
    """
    指定された月の最初の日と最後の日を取得します。

    引数:
        year (int): 年
        month (int): 月

    戻り値:
        tuple: 月の最初の日と最後の日を含むタプル
    """
    first_day = datetime.date(year, month, 1)
    
    if month == 12:
        last_day = datetime.date(year, month, 31)
    else:
        last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    return first_day, last_day

def print_calendar_header(year, month):
    """
    月の名前と年を含むカレンダーのヘッダーを印刷します。

    引数:
        year (int): 年
        month (int): 月
    """
    month_names = [
        "", "1月", "2月", "3月", "4月", 
        "5月", "6月", "7月", "8月", 
        "9月", "10月", "11月", "12月"
    ]
    print(f"{month_names[month]} {year}".center(20))
    print("月 火 水 木 金 土 日")

def print_calendar(year, month):
    """
    指定された月のカレンダーを印刷します。

    引数:
        year (int): 年
        month (int): 月
    """
    first_day, last_day = get_calendar_month(year, month)
    
    start_weekday = first_day.weekday()
    
    print(" " * (start_weekday * 3), end="")
    
    for day in range(1, last_day.day + 1):
        current_date = datetime.date(year, month, day)
        weekday = current_date.weekday()
        
        print(f"{day:2d}", end=" ")
        
        if weekday == 6:
            print()
    
    if last_day.weekday() != 6:
        print()

def main():
    """
    コマンドライン引数に基づいてカレンダー表示を処理するメイン関数。
    """
    current_date = datetime.date.today()
    year = current_date.year
    month = current_date.month

    if len(sys.argv) > 1:
        if sys.argv[1] == "-m" and len(sys.argv) > 2:
            month = validate_month(sys.argv[2])
    
    print_calendar_header(year, month)
    print_calendar(year, month)

if __name__ == "__main__":
    main() 