from flask import Flask

#This line creates an instance of the Flask class. 
#This instance, named app, is the main object for your web application. 
#The __name__ variable is passed to the Flask class to tell it where to look for resources like templates and static files.
app = Flask(__name__)


#This is a decorator that tells Flask which URL(only) should trigger the hello_world function. In this case, the root URL (/).
#Decorator performs some action before the function execution. you can also use decorators for authentication before accessing the function or a service(example any aws service)
@app.route('/')  
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':     #block ensures that the application runs only if the script is executed directly (as opposed to being imported as a module). 
    app.run("0.0.0.0")         #starts the Flask development server and makes it listen on all available network interfaces.
    
# __name__ == '__script__' if this code has to be used as module

#to run this app > copy this app in ec2  > install flask using ... pip3 install flask> Run app ...python3 <filename>.py
#flask will start a development server > as flask app run port 5000> on browser ... Ec2publicip:5000/
# output .....Hello, World!

#if on browser > Ec2publicip:5000/xyz > 
#Output ....Not found message (this output sent by Flask and this action is performed by the decorator )


#the use of The Decorator is whenever someone is trying to access this particular API 
#so here in terms of flask it is doing two things one is it is saying flask that okay only serve this function on "/" only
#and second if someone is trying to access it on a different URL then send this particular message as per flask package.