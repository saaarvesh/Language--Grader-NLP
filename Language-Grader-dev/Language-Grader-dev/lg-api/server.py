import flask
import mysql.connector
import json
from flask import request, jsonify
from flask_cors import CORS


app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="tat"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT * FROM user_data")

myresult = mycursor.fetchone()

print(myresult)

# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
    # {'id': 0,
     # 'title': 'A Fire Upon the Deep',
     # 'author': 'Vernor Vinge',
     # 'first_sentence': 'The coldsleep itself was dreamless.',
     # 'year_published': '1992'},
    # {'id': 1,
     # 'title': 'The Ones Who Walk Away From Omelas',
     # 'author': 'Ursula K. Le Guin',
     # 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     # 'published': '1973'},
    # {'id': 2,
     # 'title': 'Dhalgren',
     # 'author': 'Samuel R. Delany',
     # 'first_sentence': 'to wound the autumnal city.',
     # 'published': '1975'}
# ]





@app.route('/', methods=['GET'])
def home():
    return '''<h1>Text Analysis tool</h1>
<p>Welcome to the API of the TAT. You can login and get your textual content check using this API or you can prefer to use our newly built website!</p>'''


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

@app.route('/tat/register', methods=["POST"])
def tat_register():
    error = ''
    try:
        if request.method == "POST":
            credentials = json.loads(request.get_data().decode("utf-8"))
            attempted_username = credentials["name"]
            attempted_useremail = credentials["email"]
            attempted_password = credentials["pass"]
            attempted_userphone = credentials["phone"]
            attempted_usercategory = credentials["category"]
            user_query=f"INSERT INTO `user_data` (`user_name`, `user_email`, `user_password`, `user_phone`, `user_type`) VALUES ('{attempted_username}','{attempted_useremail}','{attempted_password}','{attempted_userphone}','{attempted_usercategory}')"
            mycursor.execute(user_query)
            mydb.commit()
            myresult = mycursor.fetchone()
            # import pdb; pdb.set_trace()
            print(myresult)
            registerSuccessful={"registration":True,"auth":True}
            response = jsonify(registerSuccessful)
            return response
    except Exception as e:
        # import pdb; pdb.set_trace()
        regisFail={"registration":False,"auth":False}
        return jsonify(regisFail)

@app.route('/tat/auth', methods=["POST"])
def tat_auth():
    error = ''
    try:
        if request.method == "POST":
            credentials = json.loads(request.get_data().decode("utf-8"))
            attempted_username = credentials["email"]
            attempted_password = credentials["pass"]
            user_query="select * from user_data where user_email='"+attempted_username+"' and user_password='"+attempted_password+"'"
            mycursor.execute(user_query)
            myresult = mycursor.fetchone()
            print(myresult)
            # import pdb; pdb.set_trace()
            loginSuccessful={"auth":True,"username":myresult[1]}
            response = jsonify(loginSuccessful)
            # response.headers.add('Access-Control-Allow-Origin', '*')
            # response.headers.add('Access-Control-Allow-Headers', "*")
            # response.headers.add('Access-Control-Allow-Methods', "*")
            return response
        else:
            print("no error")
            return jsonify({})

    except Exception as e:
        loginfailed={"auth":False}
        print('Error in authorization')
        print(e)
        return jsonify(loginfailed)

@app.route('/tat/grade', methods=["POST"])
def tat_grade():
    error = ''
    try:
        if request.method == "POST":
            response = {
                "text":request.form['text'],
                "subject":request.form['subject'],
                "word_count":105,
                "feedback":[
                {
                    "feedback_type":"Spelling Error",
                    "feedback_value":10
                }, 
                {
                    "feedback_type":"Word Repetition",
                    "feedback_value":5
                }, 
                {
                    "feedback_type":"Reduntunt words",
                    "feedback_value":5
                }, 
                {
                    "feedback_type":"Readability",
                    "feedback_value":5
                }
                ]
            }
            print(response) 
            return jsonify(response)

    except Exception as e:
        gradingfailed={"response":False}
        return jsonify(gradingfailed)
    

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

#     # Create an empty list for our results
#     results = []

#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)

#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)
