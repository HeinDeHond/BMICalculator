from flask import Flask, render_template, request


app = Flask(__name__)


@app.template_filter('round_decimal')
def round_decimal(value, decimals=2):
    return round(value, decimals)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None

    if request.method == 'POST':
        weight = int(request.form['weight'])
        height = int(request.form['height'])

        if height != 0:
            bmi = weight / (height / 100) ** 2

    return render_template('index.html', bmi=bmi)


if __name__ == '__main__':
    app.run()
