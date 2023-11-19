from flask_app import app
from flask import render_template, redirect, request, url_for, session

# Import models
from flask_app.models.game_logic import check_guess, generate_code


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        session['secret_code'] = generate_code()
        print(session['secret_code'])
        session['attempts'] = 10
        session['incorrect_attempts'] = 0
        return render_template('game.html', attempts=session['attempts'])
    elif request.method == 'POST':
        guess = request.form['guess']
        secret_code = session.get('secret_code')
        result = 'lose'  # Assume lose unless correct guess

        if check_guess(secret_code, guess):
            return redirect(url_for('end_game', result='win'))
        else:
            session['attempts'] -= 1
            session['incorrect_attempts'] += 1

            if session['attempts'] == 0:
                return redirect(url_for('end_game', result=result))
            elif session['incorrect_attempts'] == 3:
                first_digit = session['secret_code'][0]
                last_digit = session['secret_code'][-1]
                hint = f'Heres a hint! The first digit is {first_digit} and the last digit is {last_digit}'
                return render_template('game.html', attempts=session['attempts'], hint=hint)
        return render_template('game.html', attempts=session['attempts'])
@app.route('/end/<result>')
def end_game(result):
    return render_template('end.html', result=result)