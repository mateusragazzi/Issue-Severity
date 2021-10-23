from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controller.searchController import SearchController
from controller.resultController import ResultController

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = "asdasd"
csrf.init_app(app)

@app.route('/',  methods=["GET", "POST"])
def searchPage():
  return SearchController.render()

@app.route('/result',  methods=["GET"])
def resultPage():
  return ResultController.render()

if __name__ == '__main__':
    app.run(debug=True)