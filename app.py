from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controller.searchController import SearchController

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = "asdasd"
csrf.init_app(app)

@app.route('/')
def searchPage():
  return SearchController.render()

if __name__ == '__main__':
    app.run(debug=True)