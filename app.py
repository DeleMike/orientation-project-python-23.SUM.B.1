'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png"),
        Education("Computer Science", 
                  "Harvard", 
                  "October 2019", 
                  "June 2024", 
                  "70%", 
                  "example-logo.png"),
        Education("Cybersecurity", 
                  "University of florida", 
                  "August 2016", 
                  "January 2022", 
                  "90%", 
                  "example-logo.png")            

    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education/<index>', methods=['GET', 'POST'])
def education(index):
    '''
    Handles education requests
    '''  
    if request.method == 'GET' and index.isnumeric():        
        index_num = int(index)
        if index_num > 0 and index_num <= len(data["education"]):
            return jsonify(data["education"][index_num - 1])
        else:
            return jsonify("Error: Not correct education index")  
    
    if request.method == 'POST':
        return jsonify({}) 
       
    return jsonify("Error: Not correct education index")  


@app.route('/resume/education', methods=["GET"])
def all_education():
    '''Return all education in a list format'''
    
    if request.method == "GET":                                             
        return data["education"]


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return data['skill'], 200

    if request.method == 'POST':
        # handle POST request by adding skill to data dictionary
        body = request.json
        required_fields = ['name', 'proficiency', 'logo']

        # validate that the body fields has all required fields
        if all(field in body for field in required_fields):
            skill = Skill(body['name'], body['proficiency'], body['logo'])

            data['skill'].append(skill) # add to list
            index = data['skill'].index(skill)

            return jsonify({
            'message': 'Skill created successfully',
            'index':index,
            'body': skill
        }), 201
        else:
            return jsonify({
            'error': 'Missing required fields in the request body'
        }), 400
       

    return jsonify({'message':'Something went wrong'}), 500


@app.route('/resume/skill/<index>', methods=['GET', 'POST'])
def a_skill(index):
    '''Return a single skill based on its index'''
    if request.method == 'GET':
        id = int(index)
        if id > 0 and id <= len(data["skill"]):
            return jsonify(data['skill'][id - 1]), 200
        else:
            return jsonify({'message':'Skill with ID {id} does not exist'.format(id=id)}), 400
    
