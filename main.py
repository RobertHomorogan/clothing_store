from flask import Flask, request
from flask_cors import CORS, cross_origin

from Model.client_model import ClientSQLModel

client_model = ClientSQLModel()

app = Flask('my_amazing_flask_app')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return 'Index Page'


@app.route('/get_all_clients')
@cross_origin()
def get_all_clients():
    clients = client_model.get_all_clients()
    clients_json = {'clients': []}
    for client in clients:
        clients_json['clients'].append({
            'cnp': client.get_cnp(),
            'first_name': client.first_name,
            'last_name': client.last_name,
            'age_group': client.age_group,
            'email': client.email
        })

    return clients_json


@app.route('/get_client/<cnp>')
@cross_origin()
def get_client(cnp):
    client = client_model.find_by_id(cnp=cnp)
    client_json = {'client': {
        'cnp': client.get_cnp(),
        'first_name': client.first_name,
        'last_name': client.last_name,
        'age_group': client.age_group,
        'email': client.email
    }}
    return client_json


@app.route('/add_client', methods=['POST'])
@cross_origin()
def add_client():
    data = request.get_json()
    print(data)
    client_model.create_client(
        cnp=data['cnp'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
    )

    return "200"


@app.route('/remove_client', methods=['POST'])
@cross_origin()
def remove_client():
    data = request.get_json()
    print(data)
    client_model.delete_client(cnp=data['cnp'])

    return "200"


@app.route('/update_client', methods=['POST'])
@cross_origin()
def update_client():
    data = request.get_json()
    print(data)
    client_model.update_client(
        cnp=data['cnp'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
    )

    return "200"

# TODO: ADAUGAT FUNCTII PENTRU PRODUSE (ASEMANATOARE CU CELE DE LA CLIENT)


if __name__ == '__main__':
    app.run(debug=True)
