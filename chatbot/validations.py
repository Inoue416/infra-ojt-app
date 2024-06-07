import os

# TODO: もしcsv, txt, json以外のファイルが入力された時のバリデーション
def checkFileFormat(filename):
    # 許可されたファイル拡張子
    allowed_extensions = ['.txt', '.csv', '.json']
    
    # ファイルの拡張子を取得
    _, file_extension = os.path.splitext(filename)
    
    # 拡張子が許可されたものかをチェック
    if file_extension in allowed_extensions:
        return True
    else:
        return False