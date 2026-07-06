from flask import flask ,render_template 
@app.route("/")
def home():
  return render_template("OneKeyReaction")
