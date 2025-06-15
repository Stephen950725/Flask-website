from flask import Flask, render_template, abort
from data.foods import TAICHUNG_FOODS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", foods=TAICHUNG_FOODS)

@app.route("/food/<int:food_id>")
def detail(food_id):
    food = next((item for item in TAICHUNG_FOODS if item['id'] == food_id), None)
    if not food:
        abort(404)
    return render_template("detail.html", food=food)

if __name__ == '__main__':
    app.run(debug=True, port=5555)


