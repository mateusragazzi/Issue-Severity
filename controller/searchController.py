from flask import render_template
from helpers.searchForm import SearchForm
from helpers.resolveRequest import ResolveRequest
from sqlalchemy import create_engine, insert, table, column
class SearchController():

  @staticmethod
  def saveSearch(request):
    engine = create_engine("mariadb+pymysql://u587450571_tcc:7K+lQEfp[Qf@185.201.11.23/u587450571_tcc?charset=utf8mb4")

    feedback = 1 if request.form["feedback"] == "true" else 0
    issue = request.form["issue"]
    severity = request.form["severity"]
    severityChoosed = request.form["severityChoosed"]

    tableOfDB = table('searches', column('issue'), column('severity'), column('feedback'), column('severitychoosed'))
    stmt = insert(tableOfDB).values(issue=issue, severity=severity, feedback=feedback, severitychoosed=severityChoosed)
    engine.execute(stmt)
    

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
