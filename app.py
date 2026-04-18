from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form.get('date')
        email = request.form.get('email')

        return render_template('result7.html', date=date, email=email)

    return render_template('index6.html')


if __name__ == '__main__':
    app.run(debug=True)
