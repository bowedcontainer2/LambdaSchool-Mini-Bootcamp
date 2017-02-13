from flask import Flask, render_template, jsonify

app = Flask( __name__ )

@app.route( '/' )
def home():
    return render_template( 'home.html' )

@app.route( '/about' )
def about():
    return render_template( 'about.html' )

@app.route( '/contact' )
def contact():
    return render_template( 'contact.html' )

@app.route( '/birthday' )
def birthday():
        return 'November 2, 1999'

@app.route( '/greeting/<name>' )
def greeting( name ):
    return 'Hello ' + name + '!'

@app.route( '/add/<int:num>/<int:numTwo>' )
def add( num, numTwo ):
    sum = num + numTwo
    return str( sum )


@app.route( '/multiply/<int:num>/<int:numTwo>' )
def multi( num, numTwo ):
    product = num * numTwo
    return str( product )
    #return output

@app.route( '/subtract/<int:num>/<int:numTwo>' )
def subtract( num, numTwo ):
    diff = num = numTwo
    return str( diff )

@app.route( '/favoritefoods' )
def faveFood():
    faves = ['ravioli', 'lasanga', 'nutella', 'ramen soup']
    return jsonify( faves )
