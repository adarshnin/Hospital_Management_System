from flask_restful import Resource, Api, request
from package.model import conn



class Undergoess(Resource):
    """This contain apis to carry out activity with all undergoess"""

    def get(self):
        """Retrive all the undergoes and return in form of json"""

        # undergoes = conn.execute("SELECT * from undergoes").fetchall()
        undergoes = conn.execute("SELECT undergoes.doc_id, doctor.doc_first_name, doctor.doc_last_name, undergoes.pat_id, patient.pat_first_name, patient.pat_last_name, undergoes.proc_code, undergoes.u_date, undergoes.nur_id, nurse.nur_first_name, nurse.nur_last_name, undergoes.room_no FROM undergoes INNER JOIN doctor ON undergoes.doc_id = doctor.doc_id INNER JOIN patient ON undergoes.pat_id = patient.pat_id INNER JOIN nurse ON undergoes.nur_id = nurse.nur_id").fetchall()

        return undergoes

    def post(self):
        """Api to add undergoes in the database"""

        undergoes = request.get_json(force=True)
        doc_id = undergoes['doc_id']
        pat_id = undergoes['pat_id']
        proc_code = undergoes['proc_code']
        u_date = undergoes['u_date']
        nur_id = undergoes['nur_id']
        room_no = undergoes['room_no']
        conn.execute('''INSERT INTO undergoes(pat_id, proc_code, u_date, doc_id, nur_id, room_no) VALUES(?,?,?,?,?,?)''', (pat_id, proc_code, u_date, doc_id, nur_id, room_no))
        conn.commit()
        return undergoes



class Undergoes(Resource):
    """This contain all api doing activity with single undergoes"""

    def get(self,pat_id):
        """retrive a singe undergoes details by its pat_id"""

        undergoes = conn.execute("SELECT * FROM undergoes WHERE pat_id=?",(pat_id,)).fetchall()
        return undergoes


    def delete(self,pat_id):
        """Delete the undergoes by its doc_id"""

        conn.execute("DELETE FROM undergoes WHERE pat_id=?",(pat_id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,pat_id):
        """Update the undergoes details by the doc_id"""

        undergoes = request.get_json(force=True)
        doc_id = undergoes['doc_id']
        pat_id = undergoes['pat_id']
        proc_code = undergoes['proc_code']
        u_date = undergoes['u_date']
        app_id = undergoes['app_id']
        room_no = undergoes['room_no']
        conn.execute("UPDATE undergoes SET doc_id=?,pat_id=?,proc_code=?,u_date=?,app_id=?,room_no=?, WHERE pat_id=?", (doc_id, pat_id, proc_code, u_date, app_id, room_no, pat_id))
        conn.commit()
        return undergoes