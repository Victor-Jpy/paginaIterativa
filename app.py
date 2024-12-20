from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    dt = pd.read_csv('saude.csv')
    regioes = dt['nome'].iloc[1:6]
    centrais = dt['CENTRAL DE ABASTECIMENTO'].iloc[1:6]
    fig, ax = plt.subplots()
    ax.plot(regioes, centrais, marker='o')
    ax.set_title('Quantidade de centros de abastecimento por regiao')
    ax.set_xlabel('regioes')
    ax.set_ylabel('centrais')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek('o')
    grafh_url = base64.b64encode(img.getvalue()).decode()

    return render_template('pag_func.html', grafh_url=grafh_url, data=dt.to_html())

if __name__ == '__main__':
    app.run(debug=True)

