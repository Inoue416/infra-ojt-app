# 使用する際に自身の設定に変更して用いる
# cp env-copy.py env.pyでenv.pyを作成する

#  "mock" or "product"
# "mock" -> demoの関数を用いてLLMが本来出力する部分を補完
# "product" -> LLMの推論を用いる
mode: str = "mock"

server_name: str = "127.0.0.1"
server_port: int = 7861
