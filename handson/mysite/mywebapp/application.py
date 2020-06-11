from flask import Flask, render_template

application = app = Flask(__name__)


#adding another comment
#adding one more comment
@app.route("/")
def homepage():
    return render_template('home_e.html')

@app.route("/about/")
def aboutpage():
    return render_template('about_e.html')

if __name__=='__main__':
    application.run(debug=True)
