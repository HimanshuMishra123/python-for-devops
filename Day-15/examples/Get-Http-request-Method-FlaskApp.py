from flask import Flask

#This line creates an instance of the Flask class. 
#This instance, named app, is the main object for your web application. 
#The __name__ variable is passed to the Flask class to tell it where to look for resources like templates and static files.
app = Flask(__name__)

@app.route('/')  #This is a decorator that tells Flask which URL should trigger the hello_world function. In this case, the root URL (/).
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':     #block ensures that the application runs only if the script is executed directly (as opposed to being imported as a module). 
    app.run("0.0.0.0")         #starts the Flask development server and makes it listen on all available network interfaces.
    
# __name__ == '__script__' if this code has to be used as module
