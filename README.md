# blenderのスクリプトをあれしてこれするやつ

## いんすと
uv, blender, これ

## うさげ
1. launch_blender.batを起動する。
   中身としてはmain.pyでプロジェクトのパスを通してblenderを起動している
   エラーが出たらblenderのパスが通ってることを確認してもろてって感じで
2. blenderの"スクリプト生成"タブに移動し、main_direct.pyを読み込む
   ![alt text](description/image.png)

## めも
```python
from modules import test2

importlib.reload(test2)
```

今できるのは環境構築だけです。
またこんど！