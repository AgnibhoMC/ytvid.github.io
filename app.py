from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    url = request.form["url"]
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(".")
    filename = stream.default_filename
    return render_template("convert.html", filename=filename)

@app.route('/download/<filename>')
def download(filename):
    response = send_file(filename)
    response.headers['Content-Disposition'] = 'attachment; filename=converted.mp3'
    return response

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
