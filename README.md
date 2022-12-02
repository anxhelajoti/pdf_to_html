# pdf_to_html
PDF to HTML Convertor Anxhela &amp; Oualid

Library Credits to:  coolwanglu /pdf2htmlEX




### Pré-requis
- ```lancer Docker (il faut avoir ajouter auparavant l'utilisateur au groupe docker)```
- ```Python 3 with pip```

### To start on new environment
- ```docker pull bwits/pdf2htmlex```
- ```pip install fastapi pydantic uvicorn requests```

### To run at the root app do:

- ```uvicorn app:app --reload```


## Testing

@POST http://127.0.0.1:8000/converter

 {
    "url" : "myurl.pdf"
 }
