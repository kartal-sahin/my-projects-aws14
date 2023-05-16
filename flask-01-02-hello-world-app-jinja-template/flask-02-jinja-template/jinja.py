from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def head():
    return render_template('index.html', number1=888, number2=9999)


@app.route('/mult')

def number():
    x=15
    y=20
    return render_template('body.html', num1=5, num2=6, mult=x*y)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
