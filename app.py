from flask import Flask,json 
import requests
import os #to be used  with environment variables  stored in config.py

"""this create a factory for creating our application"""
app  = Flask(__name__)

# app.config.from_pyfile("settings.py")
environment_configuration = os.environ['CONFIGURATION_SETUP']
app.config.from_object(environment_configuration)
print(f"Environment: {app.config['ENV']}")
print()
print(f"Debug: {app.config['DEBUG']}")
print()
print(f"Secret key: {app.config['SECRET_KEY']}")
print()

@app.route("/",methods=["GET"])
def get_chuck_norris_jokes():
    """this is a get method /or request method for obtaining random chucknnoris jokes"""

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    global i
    for i in response:
        print(i)
         #this does the get method and turn the datat into json dic like objects
    return "<strong>Random jokes from chuck norris: </strong>",response.keys()


if __name__ == "__main":
    app.run(debug=False)