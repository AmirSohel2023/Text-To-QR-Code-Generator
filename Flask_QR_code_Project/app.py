from flask import Flask, render_template, request, send_file
import qrcode


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        text = request.form['text']

        filename = "qrcode.png"
        img = qrcode.make(text)
        img.save(filename)

        return send_file(filename, mimetype='image/png')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

 