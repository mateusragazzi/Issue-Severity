import pickle

class ResolveRequest:
  form = None
  model = None
  
  def __init__(self, form, X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap):
    self.form = form
    self.X_train = X_train
    self.y_train_final = y_train_final
    self.X_test = X_test
    self.y_test_final = y_test_final
    self.vectorizer = vectorizer
    self.severityMap = severityMap

  def readModelFile(self):
    if (self.model is None):
      self.model = pickle.load(open('train_data.pkl', 'rb'))

    return self.model

  def predictInput(self):
    input = [self.form.data['search']]
    new = self.vectorizer.transform(input)

    return self.model.predict(new)

  def getAccuracy(self):
    accuracy = self.model.score(self.X_test, self.y_test_final) * 100
    return "%.2f" % accuracy

  def formatResponse(self, result):
    return {
        "result": result, 
        "accuracy": self.getAccuracy()
        # "words": [{"tag": "Teste", "weight": 4}]
      }

  def process(self):
    self.readModelFile()
    result = self.predictInput()
    result = list(self.severityMap.keys())[list(self.severityMap.values()).index(result[0])]

    return self.formatResponse(result)

     