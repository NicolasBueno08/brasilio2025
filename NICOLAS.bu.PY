from flask import flask
app=flask (__name__)
@app.route("/")
def home()
return:"servidor rodando!tudo ok!"
 
 @app.route("/mrensagem")
def bem-vindo():
 return "Bem-vindo servidor ok"
if"__name__"=="__main__"
app.run(debug=true)