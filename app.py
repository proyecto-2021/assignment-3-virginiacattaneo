from flask import Flask,jsonify,request, make_response

app = Flask(__name__)

assignments =[]
 
# Get Assignments
@app.route('/assignments', methods=['GET'])
def getAssignments():
    return make_response(jsonify({"assignments":assignments, "title": "Lista de Asignaciones"}))
#curl -L -H 'Content-Type:application/json' -X POST http://localhost:4000/assignments -d '{"description": "Investigate about HTTP", "id": "11", "name": "Assignment 1", "price": "1", "status": "done"}'
#curl -L -H 'Content-Type:application/json' -X POST http://localhost:4000/assignments -d '{"description": "Install python and flask", "id": "12", "name": "Assignment 2", "price": "5", "status": "in progress"}'
#curl -L -H 'Content-Type:application/json' -X POST http://localhost:4000/assignments -d '{"description": "Create a REST API", "id": "13", "name": "Assignment 3", "price": "15", "status": "stalled"}'
#curl -L -X GET http://localhost:4000/assignments
# ESTE ULTIMA MUESTRA LA LISTA


# Create New Assignment
@app.route('/assignments', methods=['POST'])
def addAssignments():
    new_assignment = {
		"id": request.json['id'],
		"name": request.json['name'],
		"description": request.json['description'],
                "price": request.json['price'],
                "status": request.json['status']
    }
    foundAssignment=[assignment for assignment in assignments if assignment["id"]==request.json['id']]
    if (len(foundAssignment)>0):
        return make_response(jsonify({"assignment": "repeated"}),409)
    assignments.insert(0,new_assignment)
    return make_response(jsonify({"assignment":new_assignment}),200)
#curl -L -H 'Content-Type:application/json' -X POST http://localhost:4000/assignments -d '{"id": "10", "name": "New Task", "description": "To do Something", "price": "100", "status": "todo"}'   
# NUEVO ID
#curl -L -H 'Content-Type:application/json' -X POST http://localhost:4000/assignments -d '{"id": "10", "name": "New Task", "description": "To do Something", "price": "100", "status": "todo"}'    
# ID EXISTENTE     


# Get Assignment por ID
@app.route('/assignments/<int:id_get>', methods=['GET'])
def View_assignment(id_get):
    for i in range(len(assignments)):
        if (assignments[i])['id']==id_get:
            return make_response(jsonify({"assignment":assignments}),409) 
    return make_response(jsonify({"assignment":"Not Found!"}),404)        
#curl -L -X GET http://localhost:4000/assignments/11 
# MOSTRAR ID EXISTENTE
#curl -L -X GET http://localhost:4000/assignments/14
# MOSTRAR ID NO EXISTENTE


# Update Assignment
@app.route('/assignments/<int:id_put>', methods=['PUT'])
def UpdateAssignment(id_put):
    for i in range(len(assignments)):
        if (assignments[i])['id']==id_put:
            (assignments[i])['name']=request.json['name']
            return make_response(jsonify({"assignment":assignments}),200)
    return make_response(jsonify({"assignment":"Not Found!"}),404)
#curl -L -H 'Content-Type:application/json' -X PUT http://localhost:4000/assignments/11 -d '{"name": "new name"}'
# ACTUALIZAR UN ID EXISTENTE
#curl -L -H 'Content-Type:application/json' -X PUT http://localhost:4000/assignments/14 -d '{"name": "new name"}'
# ACTUALIZAR UN ID NO EXISTENTE


# Delete Assignment
@app.route('/assignments/<int:delete_id>', methods=['DELETE'])
def delete_assigments(delete_id):
    for i in range(len(assignments)):
        if (assignments[i])['id']==delete_id:
            assignments.remove(assignments[i]) 
            return make_response(jsonify({"assignment":assignments}),200)
    return make_response(jsonify({"assignment":"Not Found!"}),404)
 #curl -L -X DELETE http://localhost:4000/assignments/12 
# ELIMINAR ID EXISTENTE
#curl -L -X DELETE http://localhost:4000/assignments/14 
# ELIMINAR ID NO EXISTENTE  
 

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


