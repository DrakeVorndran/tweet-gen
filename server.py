from flask import Flask
from markov import gen_markov, gen_sentence

styles = '''
.box {height: 200px; width: 200px; margin: 20px;}
.container {display: flex; flex-wrap: wrap;}
'''

HTML = """
<html>
  <head>
    <title>my app</title>
    <style>
      {}
    </style>
  </head>
  <body>
    <div class="container">{}</div>
  </body>
</html>
"""



app = Flask(__name__)

@app.route('/')
def home_route():
  corpus = open('ready_player_one.txt')
  text = ''
  for line in corpus:
    text +=line[:-1]+' '
  chain = gen_markov(text, 2)
  sentence = gen_sentence(chain)
  return HTML.format(styles, sentence)
