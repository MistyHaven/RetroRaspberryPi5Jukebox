from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Capture the authorization code
    auth_code = request.args.get('code')
    return f"Authorization code: {auth_code}", 200

if __name__ == '__main__':
    app.run(port=8888)
