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

@app.route('/<int:num>')
def home_route(num):
  corpus = open('ready_player_one.txt')
  text = ''
  for line in corpus:
    text +=line[:-1]+' '
  chain = gen_markov(text, 2)
  sentence = gen_sentence(chain, num)
  return HTML.format(styles, sentence)

# def hello_world(num):
#   words = 'red orange yellow green blue indigo violet'
#   dictogram = dict_histogram(words)
#   random_colors = []
#   for _ in range(num):
#     random_colors.append(sample(dictogram))
#   for i, color in enumerate(random_colors):
#     random_colors[i] = '<div class="box" style="background-color:{};"></div>'.format(color) 
#   return_list = ' '.join(random_colors)
#   return HTML.format(styles, return_list)