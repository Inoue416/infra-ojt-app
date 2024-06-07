import time
import env
# TODO: LLMのPredict、RAGを呼ぶ
def callBot(history):
    response = ""
    if env.mode == "mock":
        response = "Demo Message!"
    elif env.mode == "product":
        # TODO: call LLM
        pass
    else:
        response = "Mode Error..."

    history[-1][1] = ""
    for character in response:
        history[-1][1] += character
        time.sleep(0.05)
        yield history
