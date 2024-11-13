from flask import Flask, render_template_string
import nbformat
from nbconvert import HTMLExporter
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Ruta al archivo Jupyter Notebook
    notebook_path = 'RamdomForest.ipynb'

    # Cargar el cuaderno Jupyter
    try:
        with open(notebook_path, encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)


        # Convertir el cuaderno a HTML
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_notebook_node(notebook_content)

        # Pasa el HTML generado a la plantilla
        return render_template_string(body)

    except Exception as e:
        return f"Error al procesar el cuaderno: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)