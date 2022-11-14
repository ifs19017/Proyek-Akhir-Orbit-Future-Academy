from flask import Flask, render_template, url_for

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    kalimat='Menyertakan file gambar dan CSS di Flask- www.kelasprogrammer.com'
    return render_template('index.html',kalimat=kalimat)

if __name__ == '__main__':
    application.run(debug=True)