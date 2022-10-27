import os

from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from controller.searchController import SearchController
from helpers.loadDataset import LoadDataset

X_test = None
y_test_final = None
vectorizer = None
severityMap = None

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = "juafbuasfuiosdaiu3opdo"
csrf.init_app(app)

@app.before_first_request
def readDataset():
  global X_test, y_test_final, vectorizer, severityMap
  if (X_test is None and vectorizer is None):
    X_test, y_test_final, vectorizer, severityMap = LoadDataset().initData()

@app.route('/',  methods=["GET", "POST"])
def searchPage():
  global X_test, y_test_final, vectorizer, severityMap
  return SearchController.render(X_test, y_test_final, vectorizer, severityMap)

@csrf.exempt
@app.route('/save-query',  methods=["POST"])
def persistSearch():
  SearchController.saveSearch(request)
  return "";

if __name__ == '__main__':
  app.run(debug=os.environ.get('FLASK_DEBUG'))