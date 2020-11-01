from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrive the patient, doctor, appointment, medication count for the dashboard page"""

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM appointment").fetchone()
        getMedicationCount = conn.execute("SELECT COUNT(*) AS medication from medication").fetchone()
        getDepartmentCount = conn.execute("SELECT COUNT(*) AS department FROM department").fetchone()
        getNurseCount = conn.execute("SELECT COUNT(*) AS nurse FROM nurse").fetchone()
        getRoomCount = conn.execute("SELECT COUNT(*) AS room FROM room").fetchone()
        getProcedureCount = conn.execute("SELECT COUNT(*) AS procedure FROM procedure").fetchone()
        getPrescribesCount = conn.execute("SELECT COUNT(*) AS prescribes FROM prescribes").fetchone()
        getUndergoesCount = conn.execute("SELECT COUNT(*) AS undergoes FROM undergoes").fetchone()

        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        getPatientCount.update(getMedicationCount)
        getPatientCount.update(getDepartmentCount)
        getPatientCount.update(getNurseCount)
        getPatientCount.update(getRoomCount)
        getPatientCount.update(getProcedureCount)
        getPatientCount.update(getPrescribesCount)
        getPatientCount.update(getUndergoesCount)

        return getPatientCount