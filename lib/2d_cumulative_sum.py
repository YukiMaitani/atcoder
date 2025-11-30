from typing import List, Callable, Tuple, Optional

def tdCumsum(data: List[List[int]]) -> List[List[int]]:
    """
    2次元配列の累積和を求める。
    Args:
        data (List[List[int]]): 2次元配列
    Returns:
        List[List[int]]: 累積和を取った配列
    """

    h = len(data)
    w = len(data[0])
    for i in range(h):
        for j in range(1, w):
            data[i][j] += data[i][j-1]
    for j in range(w):
        for i in range(1, h):
            data[i][j] += data[i-1][j]
    return data

def tdBinaryFilter(data: List[List[int]], predicate: Callable[[int], bool]) -> List[List[int]]:
    """
    2次元配列から条件を満たす要素を1、満たさない要素を0にした2次元配列を返す。
    これの累積和を取れば、特定の値の個数を高速に求められる。
    Args:
        data (List[List[int]]): 2次元配列
        predicate (Callable[[int], bool]): 特定の値を判定する関数
    Returns:
        List[List[int]]: 条件に応じて1/0に変換された2次元配列
    """
    h = len(data)
    w = len(data[0])
    return [[1 if predicate(data[i][j]) else 0 for j in range(w)] for i in range(h)]

def tdCount(data: List[List[int]], predicate: Callable[[int], bool], h: Optional[int] = None, w: Optional[int] = None) -> int:
    """
    2次元配列の特定の値の個数を数える。
    Args:
        data (List[List[int]]): 2次元配列
        predicate (Callable[[int], bool]): 特定の値を判定する関数
        h (Optional[int]): 配列の高さ。指定されていない場合はdataの高さを使用する。
        w (Optional[int]): 配列の幅。 指定されていない場合はdataの幅を使用する。
    Returns:
        int: 特定の値の個数
    """
    count = 0
    h = len(data) if h is None else h
    w = len(data[0]) if w is None else w
    for i in range(h):
        for j in range(w):
            if predicate(data[i][j]):
                count += 1
    return count

def tdCumsumArea(data: List[List[int]], area: Tuple[int, int, int, int]) -> int:
    """
    2次元累積和の特定の範囲の和を求める。
    Args:
        data (List[List[int]]): 2次元累積和配列
        area (Tuple[int, int, int, int]): 範囲 (上, 下, 左, 右)
    Returns:
        int: 範囲の和
    """
    t, b, l, r = area
    res = data[b][r]
    if t > 0:
        res -= data[t-1][r]
    if l > 0:
        res -= data[b][l-1]
    if t > 0 and l > 0:
        res += data[t-1][l-1]
    return res

def imosCreate(areas: List[Tuple[int, int, int, int]], h: int, w: int) -> List[List[int]]:
    """
    いもす配列を作成する。
    Args:
        List[Tuple[int, int, int, int]]: 矩形の範囲の配列。-1はしないので注意。要素は範囲 (上, 下, 左, 右)。
        h (int): 配列の高さ
        w (int): 配列の幅
    Returns:
        List[List[int]]: いもす配列
    """

    data = [[0]*(w+1) for _ in range(h+1)]
    for t, b, l, r in areas:
        data[t][l] += 1
        data[t][r+1] -= 1
        data[b+1][l] -= 1
        data[b+1][r+1] += 1
    return data
