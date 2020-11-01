$(document).ready(function () {

    var table

    function addUndergoes(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "undergoes",
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
            $.notify("Undergoes Added Successfully", { "status": "success" });
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getUndergoes()
        });

    }

    function getUndergoes() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "undergoes",
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
                        mData: 'proc_code'
                    },
                    {
                        mData: 'u_date'
                    },
                    {
                        mData: 'nur_id'
                    },
                    {
                        mData: 'nur_first_name'
                    },
                    {
                        mData: 'nur_last_name'
                    },
                    {
                        mData: 'room_no'
                    }
                ]
            });
            $('#datatable4 tbody').on('click', '.delete-btn', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                deleteUndergoes(data.pat_id)

            });
            $('.btn-edit').one("click", function (e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savetheundergoes").off("click").on("click", function (e) {
                        var instance = $('#detailform').parsley();
                        instance.validate()
                        console.log(instance.isValid())
                        if (instance.isValid()) {
                            jsondata = $('#detailform').serializeJSON();
                            updateUndergoes(jsondata, data.pat_id)
                        }

                    })
                })



            });

        });


    }




    $("#addUndergoes").click(function () {
        $('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

            $(".form_datetime").datetimepicker({
                format: 'yyyy-mm-dd hh:ii:ss',
                startDate: new Date(),
                initialDate: new Date()
            });
            console.log("innn")
            $("#savetheundergoes").off("click").on("click", function (e) {
                console.log("inn")
                var instance = $('#detailform').parsley();
                instance.validate()
                if (instance.isValid()) {
                    jsondata = $('#detailform').serializeJSON();
                    addUndergoes(jsondata)
                }

            })

        })

    })


    getUndergoes()
})
