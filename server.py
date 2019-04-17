from flask import Flask
from sampling import sample
from histogram import dict_histogram

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

@app.route('/colors/<int:num>')
def hello_world(num):
  words = 'red orange yellow green blue indigo violet'
  dictogram = dict_histogram(words)
  random_colors = []
  for _ in range(num):
    random_colors.append(sample(dictogram))
  for i, color in enumerate(random_colors):
    random_colors[i] = '<div class="box" style="background-color:{};"></div>'.format(color) 
  return_list = ' '.join(random_colors)
  return HTML.format(styles, return_list)