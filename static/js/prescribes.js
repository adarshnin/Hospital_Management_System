$(document).ready(function () {

    var table

    function addPrescribes(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "prescribes",
            "method": "POST",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache",
                "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Prescribes Added Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getPrescribes()
        });

    }

    function getPrescribes() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "prescribes",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }

        $.ajax(settings).done(function (response) {



            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                "aaSorting": [],
                aoColumns: [
                {
                    mData: 'doc_id'
                },
                {
                    mData: 'doc_first_name'
                },
                {
                    mData: 'doc_last_name'
                },
                {
                    mData: 'pat_id'
                },
                {
                    mData: 'pat_first_name'
                },
                {
                    mData: 'pat_last_name'
                },
                {
                    mData: 'med_code'
                },
                {
                    mData: 'p_date'
                },
                {
                    mData: 'app_id'
                },
                {
                    mData: 'dose'
                }
                ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deletePrescribes(data.doc_id)

            });
            $('.btn-edit').one("click", function(e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savetheprescribes").off("click").on("click", function(e) {
                        var instance = $('#detailform').parsley();
                        instance.validate()
                        console.log(instance.isValid())
                        if(instance.isValid()){
                            jsondata = $('#detailform').serializeJSON();
                            updatePrescribes(jsondata, data.doc_id)
                        }

                    })
                })



            });

        });


    }




    $("#addPrescribes").click(function () {
        $('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

            $(".form_datetime").datetimepicker({
             format: 'yyyy-mm-dd hh:ii:ss',
             startDate:new Date(),
             initialDate: new Date()
            });
            console.log("innn")
            $("#savetheprescribes").off("click").on("click", function(e) {
                console.log("inn")
                var instance = $('#detailform').parsley();
                instance.validate()
                if(instance.isValid()){
                    jsondata = $('#detailform').serializeJSON();
                    addPrescribes(jsondata)
                }

            })

        })

    })


    getPrescribes()
})
