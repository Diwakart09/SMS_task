from flask import Flask,request
from flask_restful import Resource, Api
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

Chem_elem={'6':'C','7':'N','8':'O'}
Comp={'6':{'id':6,'name':"Plate&Stuctural","price":"1234.50","chemical_composition":{"elem":{"id":13,"name":'Al'},"percentage":"25"}}}

def abort_if_id_doesnt_exist(id):
    if id not in Comp:
        abort(404, message="id {} doesn't exist".format(id))

class chemi_elem(Resource):
    def get(self):
        return Chem_elem
    def put (self,id):
        chemi_elem[id]=request.form['data']
        return {id: Chem_elem[id]},201

class chemi_comp(Resource):
    def get(selfself,id):
        abort_if_id_doesnt_exist(id)
        print(Comp[id])
        return Comp[id],201
    def put (self,id):
        Comp[id]=request.form['data']
        return Comp[id],201

api.add_resource(chemi_elem, '/getallids')
api.add_resource(chemi_comp, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=False)