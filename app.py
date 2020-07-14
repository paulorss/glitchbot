from flask import Flask, render_template, request
from newspaper import Article
from googlesearch import search

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    msg = userText
    rec = 'site:receita.economia.gov.br intitle:' + msg
    listag = []
    for urla in search(rec, tld='com.br', lang='pt-br', stop=3, pause=2):
        listag.append(urla)
    
    g = int(len(listag))
    print(g)

    listago = []
    for z in range(0, g):
        ur = str(listag[z])
        listago.append(ur)
    
    print(listago)
    qo = int(len(listago))

    reports2 = []
    for r in range(0, qo):
        ia = str(listago[r])
        article = Article(ia, language="pt")
        article.download()
        article.parse()
        article.text
        reports2.append(str(article.text).replace('\n', ' '))

    resposta_final = str(reports2).replace('\n', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace("'", '').replace('"', ' ')
       
    return str(resposta_final) 
  
if __name__ == "__main__":
    app.run()
