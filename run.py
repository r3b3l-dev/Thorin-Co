# import os from the standard library
import os
# import the flask class
from flask import Flask, render_template

# create an instance of flask and store it in the varibale called app
# the 1st argument of flask class is name of  apps module/package
# since we're just using a single module we're just using __name__ which is a built in 
# python variable. Flask needs this so it knows where to look for templates and static files 
app = Flask(__name__)

# use the route decorator to tell flask what url should trigger the funtion that follows
# a decorator starts with the @ symbol. A way of wrapping funtions.
# when we navigate to / root index() is triggered.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# if name is = main then we're going to run our app with 
# the following arguments
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # allows us to debug code in dev stage
        debug=True)