from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('game_options.html')

@app.route('/game')
def game():
    mode = request.args.get('mode', 1)
    return render_template('game.html', mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
