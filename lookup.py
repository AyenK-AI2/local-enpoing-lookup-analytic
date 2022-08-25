import pandas
import json
import ast



def search_table(queried_customer):
    #pandas.read method takes the entire csv file and converts it to a pandas data frame 
    csv=pandas.read_csv('Churn_unpredicted .csv')
    
    # queried_customer="7590-VHVEG"
    # queried_customer="3668-QPYBK"
    
    
    #table_selection is a data frame object, kind of like a table; in this case it is a table like so 
    #  customerID Predicted Churn
    # 0  7590-VHVEG     ChurnLikely
    
    #the .loc method allows you to select any particular row or column or any single item from the entire table 
    table_selection = csv.loc[csv['customerID']==queried_customer, ['customerID', 'Predicted Churn']]
    
    
   
    
    # table_selection.to_json method converts the data frame object to a string object 
    #selection is now a string object 
    # [{"customerID":"7590-VHVEG","Predicted Churn":"ChurnLikely"}]
    selection=table_selection.to_json( orient='records')
    
    # using json.loads on the selection string object converts it to a list; a list of dictionaries 
    # [{'customerID': '7590-VHVEG', 'Predicted Churn': 'ChurnLikely'}]
    
    selection = json.loads(selection)

    #Finally, picking a single item from the selection list , you end up with a single dictionary item 
    selection_item = selection[0]
    #somehow it seems the ai squared thing doesnt like the selection - it gives index error: list index out of 
    #range whenever that endpoint  is tapped.
    # selection=json.loads(selection_item)
    # print(selection_item)
    
    #returning the selection back to json object
    # selection_item=json.dumps(selection_item)

    print("item returned from lookup",selection_item)

    return selection_item



########################################################################################################








def List_customers():

     #pandas.read method takes the entire csv file and converts it to a pandas data frame 
    csv=pandas.read_csv('Churn_unpredicted .csv')


    cols= ['customerID', 'Predicted Churn']
    
    #selecting all rows and the two colummns
    table_Allselection = csv.loc[:, cols]


    selectionAll=table_Allselection.to_json( orient='records')
    # print("dataframe to_json: ",type(selectionAll))


    #loading to python list so I can narrow the selection
    selectionAll=json.loads(selectionAll)
    # print("json.loads: ",type(selectionAll))

    #selcting 3 items from the entire selection
    selection_items=selectionAll[1:5]
    # print("selection items: ",type(selection_items))
    # print(selection_items)

   

    # customer_list = [customer['customerID'] for customer in selection_items]
    # # print(type(customer_list))

    

    # for customer in customer_list: 
    #     return (customer)
       


    # #converting back to json object
    # selection_items=json.dumps(selection_items)
    # # print("jsondumps selection_items",type(selection_items))


    # print('Items returned from list customers',selection_items)
    
    return selection_items




    
print(List_customers())


