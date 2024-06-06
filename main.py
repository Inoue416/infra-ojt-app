import gradio as gr
import env
from chatbot import chat, llmbot

# Chatbot app with multimodal input (text, json, csv). Plus shows support for streaming text.
# ASK: できればこのブロックも別ファイルに分けたいがアプリ規模的にもメインになるため分ける必要はないかも
with gr.Blocks() as app:
    chatbot = gr.Chatbot(
        [],
        elem_id="chatbot",
        bubble_full_width=False
    )

    chat_input = gr.MultimodalTextbox(
        interactive=True, 
        file_types=[".json", ".txt", ".csv"], 
        placeholder="Enter message or upload file...",
        show_label=False
    )

    chat_msg = chat_input.submit(chat.addUserInput, [chatbot, chat_input], [chatbot, chat_input])
    # TODO: バリデーションを入れる
    bot_msg = chat_msg.then(
        llmbot.callBot,  # LLMのpredictを呼ぶ
        chatbot, chatbot, api_name="bot_response")
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

app.queue()
app.launch(server_port=env.server_port, server_name=env.server_name)