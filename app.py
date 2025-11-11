from flask import Flask, render_template, request, redirect, url_for,jsonify
from utils.llm_model import generate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form.get('topic')
        length = request.form.get('length')
        return redirect(url_for('result', topic=topic, length=length))
    return render_template('index.html')

@app.route('/result')
def result():
    topic = request.args.get('topic')
    length = request.args.get('length')
    text = generate_text(topic, length)
    return render_template('result.html', topic=topic, length=length, text=text)

    
if __name__ == '__main__':
    app.run(debug=True,port=5001)
