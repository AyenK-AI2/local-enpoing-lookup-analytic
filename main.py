# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:07:51 2020

@author: win10
"""
#pip install fastapi uvicorn

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI,Request
import lookup
from lookup import search_table
# from lookup import csv2
from fastapi.templating import Jinja2Templates



# 2. Create the app object
app = FastAPI()
templates = Jinja2Templates(directory="templates/")



# 3. Index route, opens automatically on 
@app.get('/')
async def welcome():

    
    return lookup.List_customers()

@app.get("/view")
def view(request: Request):
    result = "Customers"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

   



@app.get('/customer/{customerID}')   #path parameter 

async def get_customer_id(customerID):
    response={"customer_id": customerID }
     
    return response




@app.get('/get-customer/')   #query parameter
async def read_customerID(customerID: str):

    return search_table(customerID)


  




# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8080
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
#uvicorn main:app --reload



