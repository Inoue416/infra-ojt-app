import os
import env
def getVecDataFileList(path: str):
    if env.mode == "mock":
        return [
            "demoFile1.txt",
            "demoFile2.txt",
            "demoFile3.txt"
        ]
    elif env.mode == "product":
        # TODO:
        return []
    return []


# TODO: 新しいベクトルデータを入力、追加
def uploadFile(file):
    if env.mode == "mock":
        writeFile(file, "./sample_txt")
    elif env.mode == "product":
        # TODO: ここに新しいファイルのアップロード時の処理追加
        pass

def writeFile(file, path):
    pass