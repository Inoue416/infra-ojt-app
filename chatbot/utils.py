import os
import env
import gradio as gr
from chatbot import validations

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

def isSameFile(filename, all_file_path):
    pass

def showModal(isSuccess: bool):
    if isSuccess:
        gr.Info("アップロードしました。")
    else:
        raise gr.Error("アップロードに失敗しました。")

# TODO: 新しいベクトルデータを入力、追加
def uploadFile(file_path):
    isSuccess = True
    if validations.checkFileFormat(file_path):
        if env.mode == "mock":
            isSuccess = writeFile(file_path, os.path.join(os.getcwd(), "sample.txt"))
        elif env.mode == "product":
            # TODO: ここに新しいファイルのアップロード時の処理追加
            pass
    else:
        isSuccess = False
    showModal(isSuccess)

def fileFormClear():
    return None

def writeFile(file, output_path):
    filename = file.split("/")[-1]
    # TODO: 同じファイルがあるか検索
    try:
        with open(file, "r") as f:
            data = f.read()
        with open(output_path, "w") as f:
            f.write(data)
    except:
        return False
    return True


def callLLM(userInput):
    pass