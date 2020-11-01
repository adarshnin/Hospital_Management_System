#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Medications(Resource):
    """This contain apis to carry out activity with all medicines"""

    def get(self):
        """Retrive all the medication and return in form of json"""

        medication = conn.execute("SELECT * from medication").fetchall()
        return medication

    def post(self):
        """Api to add medication in the database"""

        medication = request.get_json(force=True)
        code = medication['code']
        name = medication['name']
        brand = medication['brand']
        description = medication['description']
        conn.execute('''INSERT INTO medication(code, name, brand, description) VALUES(?,?,?,?)''', (code, name, brand, description))
        conn.commit()
        return medication



class Medication(Resource):
    """This contain all api doing activity with single medication"""

    def get(self,code):
        """retrive a singe medication details by its code"""

        medication = conn.execute("SELECT * FROM medication WHERE code=?",(code,)).fetchall()
        return medication


    def delete(self,code):
        """Delete teh medication by its medication"""

        conn.execute("DELETE FROM medication WHERE code=?",(code,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,code):
        """Update the medication details by the code"""

        medication = request.get_json(force=True)
        name = medication['name']
        brand = medication['brand']
        description = medication['description']
        conn.execute("UPDATE medication SET name=?,brand=?,description=? WHERE code=?", (name, brand, description, code))
        conn.commit()
        return medication