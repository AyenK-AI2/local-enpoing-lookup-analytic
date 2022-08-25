# local-enpoing-lookup-analytic


Run ``` uvicorn main:app --reload on the commandline to run the local deployment
 Run the API with uvicorn
   Will run on http://127.0.0.1:8080
    uvicorn.run(app, host='127.0.0.1', port=8080)


To Deploy using Lambda, extract the lambda.py file from the lambda package and upload to AWS lambda. 
Configure s3 bucket with appropriate file and bucket names. 

bug fix for deploying locally: change directory name from tempelates to templates

AWS API endpoint is https://v8ngh65skk.execute-api.us-east-1.amazonaws.com/default/lookup_try1A?customerID=

Local endpoint after running the local server is : http://127.0.0.1:8080/get-customer/?CustomerID=



To view Model results in a demo webpage, hit the url : http://127.0.0.1:8080/view  and run the AI squared model on the page  via the extension

Upload churn_predictions.air into the ai squared extension to begin using the model. 
Alternatively, recreate the .air file uisng the compile_churn air.ipynb file
