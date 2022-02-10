from flask import Flask, render_template
import re

app = Flask(__name__)

@app.route("/")
@app.route("/<CPF>/")
def index(CPF=None):
    state = "RUNNING"
    if CPF:
        def format_cpf(c): return re.sub('[^0-9]', '', c)
        cpf_formated = format_cpf(CPF)
        state = "FREE"
        with open("./blacklist.txt", "r") as blacklist:
            for cpf in blacklist:
                if format_cpf(cpf) == cpf_formated:
                    state = "BLOCK"
                    break

    return render_template("index.html",  result=state)

if __name__ == "__main__":
    app.run(debug=True)