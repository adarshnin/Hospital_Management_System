$(document).ready(function () {

  var settings = {
    "async": true,
    "crossDomain": true,
    "url": "common",
    "method": "GET",
    "headers": {
      "cache-control": "no-cache"
    }
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
    $('#patientcount').text(response.patient)
    $('#doctorcount').text(response.doctor)
    $('#appointmentcount').text(response.appointment)
    $('#medicationcount').text(response.medication)
    $('#departmentcount').text(response.department)
    $('#nursecount').text(response.nurse)
    $('#roomcount').text(response.room)
    $('#proccount').text(response.procedure)
    $('#prescribescount').text(response.prescribes)
    $('#undergoescount').text(response.undergoes)
  });


})
