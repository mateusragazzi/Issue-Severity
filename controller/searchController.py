import os

from flask import render_template
from helpers.searchForm import SearchForm
from helpers.resolveRequest import ResolveRequest
from sqlalchemy import create_engine, insert, table, column
class SearchController():

  @staticmethod
  def saveSearch(request):
    mysql_user = os.environ.get('MYSQL_USER')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_database = os.environ.get('MYSQL_DATABASE')
    conn_address = "mariadb+pymysql://%s:%s@%s/%s?charset=utf8mb4" % (mysql_user, mysql_password, mysql_host, mysql_database) 
    engine = create_engine(conn_address)

    feedback = 1 if request.form["feedback"] == "true" else 0
    issue = request.form["issue"]
    severity = request.form["severity"]
    severityChoosed = request.form["severityChoosed"]

    tableOfDB = table('searches', column('issue'), column('severity'), column('feedback'), column('severitychoosed'))
    stmt = insert(tableOfDB).values(issue=issue, severity=severity, feedback=feedback, severitychoosed=severityChoosed)
    engine.execute(stmt)
    

  @staticmethod
  def render(X_test, y_test_final, vectorizer, severityMap):
    form = SearchForm()

    if form.validate_on_submit():
      result = ResolveRequest(
        form, 
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
