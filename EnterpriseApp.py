from auth.entra_auth import EntraAuth

auth = EntraAuth()


@app.route("/login")
def login():
    return redirect(auth.login_url())


@app.route("/auth/callback")
def callback():
    code = request.args.get("code")
    auth.callback(code)
    return redirect("/")