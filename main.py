import gradio as gr
import env
from chatbot import chat, llmbot
from chatbot import utils

# Chatbot app with multimodal input (text, json, csv). Plus shows support for streaming text.
# ASK: できればこのブロックも別ファイルに分けたいがアプリ規模的にもメインになるため分ける必要はないかも
with gr.Blocks() as app:
    with gr.Tab("ChatBot"):
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
        bot_msg = chat_msg.then(
        llmbot.callBot,  # LLMのpredictを呼ぶ
        chatbot, chatbot, api_name="bot_response")
        bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

    with gr.Tab("Add Vec Data"):
        input_filename_list = utils.getVecDataFileList(env.vec_data_dir_path)
        with gr.Accordion("--- Input Data List ---", open=False):
            for filename in input_filename_list:
                gr.Markdown("- "+filename)
        with gr.Column():
            gr.Markdown("# Add New Data")
            gr.Markdown("## Please input file (.txt or .csv or .json)")
            upload_result_message = ""
            input_file = gr.File(file_types=[".txt", ".csv", ".json"])
            input_file.upload(utils.uploadFile, inputs=input_file)
            upload_button = gr.Button("アップロード", variant="primary")
            upload_button.click(utils.uploadFile, inputs=input_file)


app.queue()
app.launch(server_port=env.server_port, server_name=env.server_name)