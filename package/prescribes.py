from flask_restful import Resource, Api, request
from package.model import conn



class Prescribes(Resource):
    """This contain apis to carry out activity with all prescribess"""

    def get(self):
        """Retrive all the prescribes and return in form of json"""

        # prescribes = conn.execute("SELECT * from prescribes").fetchall()
        prescribes = conn.execute("SELECT prescribes.doc_id, doctor.doc_first_name, doctor.doc_last_name, prescribes.pat_id, patient.pat_first_name, patient.pat_last_name, prescribes.med_code, prescribes.p_date, prescribes.app_id, dose FROM prescribes INNER JOIN doctor ON prescribes.doc_id = doctor.doc_id INNER JOIN patient ON prescribes.pat_id = patient.pat_id").fetchall()
        return prescribes

    def post(self):
        """Api to add prescribes in the database"""

        prescribes = request.get_json(force=True)
        doc_id = prescribes['doc_id']
        pat_id = prescribes['pat_id']
        med_code = prescribes['med_code']
        p_date = prescribes['p_date']
        app_id = prescribes['app_id']
        dose = prescribes['dose']
        conn.execute('''INSERT INTO prescribes(doc_id, pat_id, med_code, p_date, app_id, dose) VALUES(?,?,?,?,?,?)''', (doc_id, pat_id, med_code, p_date, app_id, dose))
        conn.commit()
        return prescribes



class Prescribe(Resource):
    """This contain all api doing activity with single prescribes"""

    def get(self,doc_id):
        """retrive a singe prescribes details by its doc_id"""

        prescribes = conn.execute("SELECT * FROM prescribes WHERE doc_id=?",(doc_id,)).fetchall()
        return prescribes


    def delete(self,doc_id):
        """Delete the prescribes by its doc_id"""

        conn.execute("DELETE FROM prescribes WHERE doc_id=?",(doc_id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,doc_id):
        """Update the prescribes details by the doc_id"""

        prescribes = request.get_json(force=True)
        doc_id = prescribes['doc_id']
        pat_id = prescribes['pat_id']
        med_code = prescribes['med_code']
        p_date = prescribes['p_date']
        app_id = prescribes['app_id']
        dose = prescribes['dose']
        conn.execute("UPDATE prescribes SET doc_id=?,pat_id=?,med_code=?,p_date=?,app_id=?,dose=?, WHERE doc_id=?", (doc_id, pat_id, med_code, p_date, app_id, dose, doc_id))
        conn.commit()
        return prescribes