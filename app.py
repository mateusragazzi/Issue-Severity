from flask import Flask
from flask_wtf.csrf import CSRFProtect
from controller.searchController import SearchController
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

@app.before_first_request
def readDataset():
  global X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap
  if (X_train is None and vectorizer is None):
    X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap = LoadDataset().initData()

@app.route('/',  methods=["GET", "POST"])
def searchPage():
  global X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap
  return SearchController.render(X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap)

if __name__ == '__main__':
  app.run(debug=True)