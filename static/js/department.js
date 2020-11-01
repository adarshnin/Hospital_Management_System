$(document).ready(function () {

    var table


    function adddepartment(data) {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "department",
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
            $.notify("Department Added Successfully", { "status": "success" });
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getdepartment()
        });

    }

    function updatedepartment(data, department_id) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "department/" + department_id,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Department Updated Successfully", { "status": "success" });
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getdepartment()
        });


    }

    function getdepartment() {

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "department",
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
                        mData: 'department_id'
                    },
                    {
                        mData: 'name'
                    },
                    {
                        mData: 'head_id'
                    },
                    {
                        mData: 'doc_first_name'
                    },
                    {
                        mData: 'doc_last_name'
                    },
                    {
                        mRender: function (o) {
                            return '<button class="btn-xs btn btn-info btn-edit" type="button">Edit</button>';
                        }
                    }
                ]
            });
            $('.btn-edit').one("click", function (e) {
                var data = table.row($(this).parents('tr')).data();
                $('#myModal').modal().one('shown.bs.modal', function (e) {
                    for (var key in data) {
                        $("[name=" + key + "]").val(data[key])
                    }
                    $("#savethedepartment").off("click").on("click", function (e) {
                        var instance = $('#detailform').parsley();
                        instance.validate()
                        console.log(instance.isValid())
                        if (instance.isValid()) {
                            jsondata = $('#detailform').serializeJSON();
                            updatedepartment(jsondata, data.department_id)
                        }

                    })
                })



            });

        });


    }

    $("#adddepartment").click(function () {
        $('#detailform input,textarea').val("")
        $('#myModal').modal().one('shown.bs.modal', function (e) {

            console.log('innn')
            $("#savethedepartment").off("click").on("click", function (e) {
                console.log("inn")
                var instance = $('#detailform').parsley();
                instance.validate()
                if (instance.isValid()) {
                    jsondata = $('#detailform').serializeJSON();
                    adddepartment(jsondata)
                }

            })

        })



    })


    getdepartment()
})
