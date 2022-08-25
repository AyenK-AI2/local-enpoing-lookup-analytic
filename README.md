# local-enpoing-lookup-analytic


Run ``` uvicorn main:app --reload on the commandline to run the local deployment
 Run the API with uvicorn
   Will run on http://127.0.0.1:8080
    uvicorn.run(app, host='127.0.0.1', port=8080)
d

To Deploy using Lambda, extract the lambda.py file from the lambda package and upload to AWS lambda. 
Configure s3 bucket with appropriate file and bucket names. 

bug fix for deploying locally: change directory name from tempelates to templates

AWS API endpoint is https://v8ngh65skk.execute-api.us-east-1.amazonaws.com/default/lookup_try1A?customerID=

Local endpoint after running the local server is : http://127.0.0.1:8080/get-customer/?CustomerID=

