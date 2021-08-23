from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
def root():
  return render_template("form.html")

@app.route("/removeddit", methods=['POST'])
def removeddit():
  form_data = request.form['reddit_link']
  if 'reddit.com' not in form_data:
    return render_template("form.html", error="Invalid reddit link provided.")
  else:
    
    # reddit_link = reddit_link.replace("&", "&amp;")
    redirect_url = form_data.replace("reddit", "removeddit")
    return redirect(redirect_url, code=302)
