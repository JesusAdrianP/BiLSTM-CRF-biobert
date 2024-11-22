Requiere versión 3.10 de python

crear entorno virtual:  
python3.10 -m venv venv

activar entorno virtual:  
en linux:  
source venv/bin/activate  
en windows:  
source venv/scripts/activate

instalar librerias:  
pip install -r requirements.txt

Para el modelo que utiliza embeddings en la carpeta "inputs" se debe agregar el archivo .txt vectorizado con el nombre: text_fasttext_skip_model_300