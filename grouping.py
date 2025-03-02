"""
このモジュールは、メンバーのリストをランダムに2つのグループに分割する関数を含んでいます。
"""

import random

def group_split():
    """
    6人のメンバーをランダムに2つのグループ（3+3または2+4）に分割します。
    
    Returns:
        list: アルファベット順にソートされた2つのグループ
    """
    # グループメンバーのリスト
    members = ['A', 'B', 'C', 'D', 'E', 'F']
    
    # 3+3または2+4の分割をランダムに決定
    if random.random() < 0.5:
        # 3+3の分割
        group1 = random.sample(members, 3)
        group2 = [member for member in members if member not in group1]
    else:
        # 2+4の分割
        group1 = random.sample(members, 2)
        group2 = [member for member in members if member not in group1]
    
    # 両方のグループをアルファベット順にソート
    group1.sort()
    group2.sort()
    
    # 例の出力に合わせてグループを返す
    return [group1, group2]

def main():
    """
    グループ分割を実行し、結果を表示します。
    """
    groups = group_split()
    print(groups)

if __name__ == "__main__":
    main()
