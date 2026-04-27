from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <style>
                body {
                    background-color: #0f1117;
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container { text-align: center; }
                h1 { color: #ff9900; font-size: 3rem; }
                p { color: #cccccc; }
                .badge {
                    background: #ff9900;
                    color: #0f1117;
                    padding: 8px 16px;
                    border-radius: 20px;
                    margin: 5px;
                    font-weight: bold;
                    display: inline-block;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Eddie Opong</h1>
                <h2>Cloud Engineer</h2>
                <p>Containerized Flask app running on AWS ECS Fargate</p>
                <br>
                <span class="badge">Docker</span>
                <span class="badge">ECS Fargate</span>
                <span class="badge">Terraform</span>
                <span class="badge">CI/CD</span>
            </div>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)