$(document).ready(function () {
    // Load dữ liệu hóa đơn
    var table = $("#list_hoa_don").DataTable({
        destroy: true,
        info: false,
        ajax: {
            type: "get",
            url: "/store/data-hoa-don/",
            dataSrc: ""
        },
        columns: [
            { data: "no" },
            { data: "khach_hang" },
            { data: "nguoi_tao" },
            { data: "ngay_lap" },
            {
                data: "is_paid",
                render: function (data, type, row) {
                    if (type == "display") {
                        if (data == 0) {
                            return `<input type="radio">`
                        } else {
                            return `<input type="radio" checked>`
                        }
                    }
                    return data
                }
            }
        ],
        columnDefs: [
            {
                targets: 5,
                data: null,
                defaultContent: `<button class="btn btn-info" id="thanh-toan">Thanh toán</button> <button class="btn btn-primary" id="xuat">Xuất</button>`
            }
        ]
    })
    $("#list_hoa_don tbody").on("click", "#thanh-toan", function () {
        var data = table.row($(this).parents("tr")).data()
        $("#thanh-toan-hoa-don").modal("show")
        $("#chi-tiet-hoa-don").DataTable({
            paging: false,
            info: false,
            searching: false,
            ajax: {
                type: "get",
                url: ""
            }
        })
    })
})
// var data = table.row($(this).parents("tr")).data()
//         formData = new FormData()
//         formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
//         formData.append("id_invoice", data.id)
//         formData.append("is_paid", "1")

//         $.ajax({
//             contentType: false,
//             processData: false,
//             type: "post",
//             url: location.url,
//             data: formData,
//             success: function (data) {
//                 if (data.status == "success") {
//                     Swal.fire({
//                         type: "success",
//                         title: "Thành công",
//                         text: "Thanh toán thành công"
//                     });
//                 }
//             }
//         })

