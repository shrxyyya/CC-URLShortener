# long url/OG url = https://google.com/absxys/kjeren
# its short url form = http://localhost:5000/<short_url>
# localhost = 127.0.0.1   => basically the default server
# 5000  => port on which flask runs  =>  127.0.0.1:5000 => the port/address on which the application will run.
# <short_url> will be the url generated => has random letters + digits
# the short url is to then redirect the user to the original url

import random
import string

from flask import Flask, render_template, redirect, request

app = Flask (__name__)
shortened_urls = {}

def generate_short_url(length=6):    #specify short url length -- default=6
    chars = string.ascii_letters + string.digits       # random letters+digits
    short_url = "".join(random.choice (chars) for _ in range(length))      # chooses random characters from 'chars' for specified length
    return short_url

# '/' is the root url or the url/port/address on which the application runs
# 'GET' gets/loads the home/application page
# 'POST' is for when the user enters the long url which then needs to be processed
@app.route("/", methods=["GET", "POST"])      
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()     # if that short_url has already been generated (if it already exists in the dict) then re-generate another short_url  =>  more than 1 short_url can be generated for the same long_url

        shortened_urls[short_url] = long_url   # map the short_url to the long_url
        return f"Shortened URL: {request.url_root}{short_url}"
    return render_template("index.html")     #  if mmethod is not POST => method = GET, then just render/run wtv is in index.html file => basically load the html page

@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404
    
if __name__ == "__main__":
    app.run(debug=True)