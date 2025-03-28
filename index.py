

from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# DeepSeek API 配置
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-r1:free"

# 構造 API 請求頭
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 您的筆記內容
NOTE = """
出題要求：
- 題目要適合中學生。
- 鼓勵使用生動的描寫。
- 題目要能引導學生思考。

點評標準：
- 語法正確。
- 句子流暢。
- 鼓勵使用豐富的詞彙。
- 點評要具體，指出優點和改進之處。
"""

def get_ai_response(prompt, note=NOTE):
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": f"你是一個AI寫作助手，負責出寫作題目、修訂學生作品並提供點評。請參考以下筆記：\n{note}"},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"錯誤：{response.status_code}, {response.text}"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_topic', methods=['POST'])
def generate_topic():
    topic_prompt = "請給我一個簡單的寫作題目，適合學生練習片段或句子描寫。除了題目之外，不需要顯示其他資訊。格式如下：《XXXXX》。請用繁體字。"
    topic = get_ai_response(topic_prompt)
    return jsonify({"topic": topic})

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    topic = request.form['topic']
    revision_prompt = f"學生的寫作內容如下：\n\n{user_input}\n\n請修訂這段文字，使其更流暢、更符合語法，並提供具體的點評，指出優點和需要改進的地方。"
    ai_response = get_ai_response(revision_prompt)
    return render_template('index.html', topic=topic, ai_response=ai_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
