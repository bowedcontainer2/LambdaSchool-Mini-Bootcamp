import requests

my_info = {
"email": "mpineda3247@gmail.com",
"lastname": "Pineda",
"message": "I know its kinda late for this but I still want to try it!",
"name": "Matthew"
}

r = requests.post( 'https://LambdaSchool.com/contact-form',json = my_info )

print( "response: %s status code: %s" % ( r.text, r.status_code ) )
