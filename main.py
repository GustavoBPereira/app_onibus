from flask import Flask, render_template
from linhas import get_linha
app = Flask(__name__)

@app.route('/')
def index():

    return ('<h1>Auto aviação Lotus</h1>')

@app.route('/linha<int:id>')
def horario_engxpres(id):
    horarios = get_linha(id)
    if(horarios == 404):
        return ('<h1>Linha não encontrada</h1>')
    
    return render_template('index.html', horarios1=horarios['fim_semana_ida'], horarios2=horarios['fim_semana_volta'])



app.run(debug=True)