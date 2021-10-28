from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controller.searchController import SearchController
from controller.resultController import ResultController
from helpers.loadDataset import LoadDataset

X_train = None
y_train_final = None
X_test = None
y_test_final = None
vectorizer = None
severityMap = None

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = "asdasd"
csrf.init_app(app)

def readDataset():
  global X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap
  if (X_train is None and vectorizer is None):
    X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap = LoadDataset().initData()

@app.route('/',  methods=["GET", "POST"])
def searchPage():
  global X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap
  return SearchController.render(X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap)

@app.route('/result',  methods=["GET"])
def resultPage():
  return ResultController.render()

if __name__ == '__main__':
  readDataset()
  app.run(debug=True)