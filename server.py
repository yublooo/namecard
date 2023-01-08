from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    print(year)
    return render_template("index.html", yr=year)

if __name__ == "__main__":
    app.run(debug=True)