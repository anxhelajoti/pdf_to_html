# app.py

import os
import requests
import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from subprocess import Popen
from fastapi.responses import HTMLResponse


app = FastAPI()

class Item(BaseModel):
    url: str

@app.post("/converter/",response_class=HTMLResponse)
async def pdf_to_html(item:Item):

    #retrieve url
    url=getattr(item,"url")
    print (url)
    

    
    #checkFileType
    checking=url.lower().endswith(('.pdf'))
    if checking==False:
        print ("extension error")
        with open ("./error/extension_error.html","r") as f:
            html_content_0=f.read()
        return HTMLResponse(content=html_content_0, status_code=405)
        



    
    #init file title
    item_title= url.rsplit('/', 1)[1]
    real_item_title=item_title.rsplit('.',1)[0]
    print (real_item_title)
    pdf_file= Path(real_item_title+'.pdf')
    html_path=Path(real_item_title+'.html')


    

    #download the pdf
    try:
        response= requests.get(url,verify=False)
        pdf_file.write_bytes(response.content)
    except:
        print("An error occured with downloading")
        with open ("./error/downloading_error.html","r") as f:
            html_content_0=f.read()
        return HTMLResponse(content=html_content_0, status_code=406)
        


    
    #convert PDF  to html
    try:
        p=Popen('./pdf_to_html.sh  %s %s' % (str(item_title),str(real_item_title+".html")), shell=True)
        p_status = p.wait()
    except:
        print("An error occured with converting")
        with open ("./error/converting_error.html","r") as f:
            html_content_0=f.read()
        return HTMLResponse(content=html_content_0, status_code=407)



    
    #prepare the html 
    with open (real_item_title+".html","r") as f:
         html_content=f.read()



         
    #clean pdf temp file
    try:
        file_path = item_title
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted")
        else:
            print("File does not exist")
            
        file_path = real_item_title+".html"
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted")
        else:
            print("File does not exist")
    except:
        print("An error occured with deleting")
        return HTMLResponse(content=html_content, status_code=206)



    
    #sending the response
    return HTMLResponse(content=html_content, status_code=200)
    
  




    
 


    




