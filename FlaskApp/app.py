from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', output_text=None)

@app.route('/compute', methods=['POST'])
def compute():
    input_text = request.form.get('input_text')

    output_text = " this this your input text : "+input_text

    return render_template('home.html', output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
