from fastapi import Response

def SuccessResponse(data : any,client_msg : str,dev_msg : str):
    Response.status_code = 200
    return{
        "success" : True,
        "data" : data,
        "clientMessage" : client_msg,
        "devMessage" : dev_msg
    }

def ErrorResponse(data : any,client_msg : str,dev_msg : str):
    Response.status_code = 400
    return{
        "success" : False,
        "data" : data,
        "clientMessage" : client_msg,
        "devMessage" : dev_msg
    }

def ServerError(err : str, errMsg : str):
    Response.status_code = 500
    return{
        "success" : True,
        "data" : err,
        "clientMessage" : "Sorry,something went wrong, please try again in sometime!",
        "devMessage" : errMsg
    }

def NotFoundError():
    Response.status_code = 404
    return{
        "success" : False,
        "data" : None,
        "clientMessage" : "The requested resource was not found on the server",
        "devMessage" : "Not found the resource based on ID"
    }