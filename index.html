<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI 寫作助手</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            max-width: 800px;
            margin-top: 50px;
        }
        .topic-area {
            margin-bottom: 20px;
        }
        .loading {
            display: none;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center">AI 寫作助手</h1>
        <div class="topic-area">
            <h3>題目：</h3>
            <p id="topic"></p>
            <button id="generate-topic" class="btn btn-primary">生成題目</button>
            <div id="loading-topic" class="loading">正在生成題目...</div>
        </div>
        <form id="writing-form" method="POST" action="/submit">
            <div class="mb-3">
                <textarea name="user_input" class="form-control" rows="10" placeholder="請輸入您的寫作內容"></textarea>
            </div>
            <input type="hidden" name="topic" id="hidden-topic">
            <button type="submit" class="btn btn-success">提交</button>
            <div id="loading-submit" class="loading">正在處理...</div>
        </form>
        {% if ai_response %}
            <h3 class="mt-5">AI 修訂與點評：</h3>
            <pre class="bg-light p-3">{{ ai_response }}</pre>
        {% endif %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.getElementById('generate-topic').addEventListener('click', function() {
            document.getElementById('loading-topic').style.display = 'block';
            fetch('/generate_topic', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('topic').textContent = data.topic;
                document.getElementById('hidden-topic').value = data.topic;
                document.getElementById('loading-topic').style.display = 'none';
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('loading-topic').style.display = 'none';
            });
        });

        document.getElementById('writing-form').addEventListener('submit', function() {
            document.getElementById('loading-submit').style.display = 'block';
        });
    </script>
</body>
</html>
