from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_me', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/diacut', methods=['GET'])
def diacut():
    return render_template('dia.html')

@app.route('/location', methods=['GET'])
def location():
    return render_template('location.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

def main(ip='127.0.0.1', port=8080):
    app.debug = True
    app.run(host=ip, port=port)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default='127.0.0.1', type=str, required=False)
    parser.add_argument('--port', default=8080, type=int, required=False)
    args = parser.parse_args()

    main(args.ip, args.port)

