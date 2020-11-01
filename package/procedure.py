from flask_restful import Resource, Api, request
from package.model import conn



class Procedures(Resource):
    """This contain apis to carry out activity with all procedures"""

    def get(self):
        """Retrive all the procedure and return in form of json"""

        procedure = conn.execute("SELECT * from procedure").fetchall()
        return procedure

    def post(self):
        """Api to add procedure in the database"""

        procedure = request.get_json(force=True)
        code = procedure['code']
        name = procedure['name']
        cost = procedure['cost']
        conn.execute('''INSERT INTO procedure(code, name, cost) VALUES(?,?,?)''', (code, name, cost))
        conn.commit()
        return procedure



class Procedure(Resource):
    """This contain all api doing activity with single procedure"""

    def get(self,code):
        """retrive a singe procedure details by its code"""

        procedure = conn.execute("SELECT * FROM procedure WHERE code=?",(code,)).fetchall()
        return procedure


    def delete(self,code):
        """Delete the procedure by its code"""

        conn.execute("DELETE FROM procedure WHERE code=?",(code,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,code):
        """Update the procedure details by the code"""

        procedure = request.get_json(force=True)
        name = procedure['name']
        cost = procedure['cost']
        conn.execute("UPDATE procedure SET name=?,cost=? WHERE code=?", (name, cost, code))
        conn.commit()
        return procedure