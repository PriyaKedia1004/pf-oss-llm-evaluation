from promptflow import tool
from promptflow.connections import CustomConnection
import urllib
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(message: str, myconn: CustomConnection) -> str:
    # Get authentication key-values from the custom connection
    url = myconn.api_base
    api_key = myconn.api_key
    
    data = {"input_data": {
        "input_string": [
            {
                "role": "user",
                "content": "You are an AI assistant that helps users answer questions given a specific context. You will be given a context and asked a question based on that context. If the information is not present in the context or if you don\\'t know the answer, simply respond by saying that I don\\'t know the answer, please try asking a different question. Your answer should be as precise as possible and should only come from the context.\\n" + message
                },
                ],
                "parameters": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_new_tokens": 200
                    }
                }}
    body = str.encode(json.dumps(data))

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': myconn.deployment }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        result = json.loads(result.decode('utf-8'))["output"]
        return result
    except urllib.error.HTTPError as error:
        return "The request failed with status code: " + str(error.code)