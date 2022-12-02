Ce programme vous permet de convertir avec le plus grand détail vos fichiers PDF au format HTML, les examples sont dans le dossier html.

La librairie utilisé est local et open source.





TESTED ON UBUNTU ONLY
PATH ARE NOT ABSOLUTE
Please clone the project on /home/{YOUR_LOGGED_USER}/

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

Method: @POST 

Endpoint: http://127.0.0.1:8000/converter

Body: JSON

Body Example:
 {
    "url" : "https://www.archipel-thau.com/medias/images/prestataires/Archipel-Magazine-Archipel-de-Thau-Destination-Mediterranee.pdf"
 }

Response: HTML FILE





ON WINDOWS change the sh script link with 
pdf_to_html.sh file
docker run -ti --rm -v c:/pdf_to_html:/pdf bwits/pdf2htmlex pdf2htmlEX $1 $2