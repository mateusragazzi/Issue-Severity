from flask import render_template
from helpers.searchForm import SearchForm
from helpers.resolveRequest import ResolveRequest

class SearchController():

  @staticmethod
  def render(X_train, y_train_final, X_test, y_test_final, vectorizer, severityMap):
    form = SearchForm()

    if form.validate_on_submit():
      result = ResolveRequest(
        form, 
        X_train,
        y_train_final,
        X_test,
        y_test_final,
        vectorizer,
        severityMap
      ).process()
      
      return render_template(
        "search/index.jinja2",
        form=form,
        result=result
    )

    return render_template(
        "search/index.jinja2",
        form=form
    )
