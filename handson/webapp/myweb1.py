from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return('Homepage here')

@app.route("/about/")
def aboutpage():
    return('Please put your about content here')

if __name__=='__main__':
    app.run(debug=True)
