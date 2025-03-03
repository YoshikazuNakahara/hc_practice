"""
ゴルフスコア計算モジュール

このモジュールは、各ホールのパーとストローク数に基づいてゴルフスコアを計算し、
標準的なゴルフ用語を使用してプレイヤーのパフォーマンスを判定します。
"""

def calculate_golf_score(par, strokes):
    """
    パーとストローク数に基づいてゴルフスコアを計算します。
    
    引数:
        par (int): ホールのパー値 (3 ≤ par ≤ 5)
        strokes (int): プレイヤーのストローク数 (1 ≤ strokes)
    
    戻り値:
        str: ゴルフスコアの説明
    
    例外:
        ValueError: 不正なスコア計算の場合
    """
    # パーとストローク数の制約チェック
    if not (3 <= par <= 5):
        raise ValueError(f"パーは3から5の間である必要があります。入力値: {par}")
    
    if not (1 <= strokes):
        raise ValueError(f"ストローク数は1以上である必要があります。入力値: {strokes}")
    
    # コンドルのケース
    if par == 5 and strokes == 1:
        return "コンドル"
        # ホールインワンの特殊ケース
    if strokes == 1:
        return "ホールインワン"
    
    # パーとストローク数の差を計算
    diff = strokes - par
    
    # スコアマッピング
    score_map = {
        0: "パー",
        1: "ボギー",
        2: "2ボギー",
        3: "3ボギー",
        -1: "バーディ",
        -2: "イーグル",
        -3: "アルバトロス"
    }
    
    # 複数ボギーの処理
    if diff > 3:
        return f"{diff}ボギー"
    
    # スコアマップから結果を返す（該当しない場合はエラー）
    if diff not in score_map:
        raise ValueError(f"不正なスコア: パー {par}, ストローク数 {strokes}")
    
    return score_map[diff]

def main():
    """
    入力されたゴルフスコアを処理するメイン関数
    """
    try:
        # 標準入力からの読み取り
        input_data = sys.stdin.read().strip().splitlines()
        
        # 入力の行数を確認
        if len(input_data) != 2:
            raise ValueError("入力データは2行である必要があります。1行目にパー値、2行目にストローク数を入力してください。")
        
        # 入力の分割
        par_input = input_data[0].strip().split(',')
        strokes_input = input_data[1].strip().split(',')
        
        # 入力を整数に変換
        pars = [int(p) for p in par_input]
        strokes = [int(s) for s in strokes_input]
        
        # 各ホールのスコアを計算
        scores = [calculate_golf_score(par, stroke) for par, stroke in zip(pars, strokes)]
        
        # スコアをカンマ区切りで出力
        print(','.join(scores))
    
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)
    except EOFError:
        print("入力が終了しました。プログラムを終了します。")
        sys.exit(1)

if __name__ == "__main__":
    import sys
    main()