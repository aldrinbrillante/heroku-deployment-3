#Import the Flask library
from flask import Flask
#Set up our app variable so that we can start writing routes.
app = Flask(__name__)

@app.route('/') # indicates the URL of the web page we’ll need to visit in order to see our result
def homepage(): #  defines the route function
    """Shows a greeting to the user.""" # # docstring; describes the route in a human-readable way
    return 'Are you there, world? It\'s me, Ducky!' # returns the page contents.

##########################################################################################################
#Your Fav Animal (Required)
##########################################################################################################
@app.route('/penguins')
def your_animal():
    """Shows a greeting to the user."""
    return "Penguins are cute!"

##########################################################################################################
#my fav animal (required)
##########################################################################################################
@app.route('/dogs')
def my_animal():
    return "Dogs are man's best friend!"

##########################################################################################################
#your user's favorite animal
##########################################################################################################
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


##########################################################################################################
#your user's favorite animal
##########################################################################################################
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that says How did you know I liked <users_dessert>?"""
    return f'How did you know I liked {users_dessert}?'


##########################################################################################################
#Mad Libs
##########################################################################################################
@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Display story to user"""
    return f'One day, {noun} was walking through the forest and spotted a {adjective} clown. {noun} ran away in fear'

##########################################################################################################
# Multiply 2 Numbers

# Write a route multiply that takes in 2 numbers, multiplies them, and displays the results.
# It should use the URL /multiply/<number1>/<number2>, then take in number1 and number2 as parameters.
##########################################################################################################
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        ans = int(number1) * int(number2)
        return f'{number1} times {number2} is {ans}.'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'





if __name__ == '__main__':
    app.run(debug=True)




