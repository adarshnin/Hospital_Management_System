#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Departments(Resource):
    """This contain apis to carry out activity with all appiontments"""

    def get(self):
        """Retrive all the department and return in form of json"""

        # department = conn.execute("SELECT * from department").fetchall()
        department = conn.execute("SELECT department_id, name, head_id, doc_first_name, doc_last_name FROM department INNER JOIN doctor ON doctor.doc_id = department.head_id").fetchall()
        return department

    def post(self):
        """Api to add departmentf in the database"""

        department = request.get_json(force=True)
        department_id = department['department_id']
        name = department['name']
        head_id = department['head_id']
        conn.execute('''INSERT INTO department(department_id, name, head_id) VALUES(?,?,?)''', (department_id, name, head_id))
        conn.commit()
        return department



class Department(Resource):
    """This contain all api doing activity with single department"""

    def get(self,department_id):
        """retrive a singe department details by its id"""

        department = conn.execute("SELECT * FROM department WHERE department_id=?",(department_id,)).fetchall()
        return department


    # def delete(self,code):
    #     """Delete teh appointment by its id"""

    #     conn.execute("DELETE FROM department WHERE department_id=?",(code,))
    #     conn.commit()
    #     return {'msg': 'sucessfully deleted'}

    def put(self,department_id):
        """Update the department details by the department id"""

        department = request.get_json(force=True)
        name = department['name']
        head_id = department['head_id']
        conn.execute("UPDATE department SET name=?,head_id=? WHERE department_id=?", (name, head_id, department_id))
        conn.commit()
        return department