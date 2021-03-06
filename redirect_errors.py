from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
  # Test for user logged in failed
  # So redirect to logn URL
  return redirect(url_for('login'))

@app.route('/login')
def login():
  return "Now we would get username & password"

@app.errorhandler (404)
def page_not_found (error):
  return "Couldn't Find The Page You Have Requested. SORRY!", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
