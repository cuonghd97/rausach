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
            { data: "created_at" },
        ],
        columnDefs: [
            {
                width: "30%",
                targets: 4,
                data: null,
                defaultContent: `<div class="btn-group" role="group" aria-label="Basic example">
                                <button class="btn btn-primary" id="xuat">Xuất hóa đơn</button>
                                <button class="btn btn-info" id="">Sửa</button>
                                <button class="btn btn-danger" id="">Xóa</button>
                                </div>`
            }
        ]
    })

    // Lấy data các sản phẩm
    $.ajax({
        type: "get",
        url: "/store/data-san-pham/",
        success: function (data) {
            sessionStorage.setItem("san_pham", JSON.stringify(data))
        }
    })

    // Lấy data trạng thái
    $.ajax({
        type: "get",
        url: "/store/data-trang-thai/",
        success: function (data) {
            sessionStorage.setItem('trang_thai', JSON.stringify(data))
        }
    })

    $("#btn-new-hoa-don").on("click", function () {
        var trang_thai = JSON.parse(sessionStorage.getItem("trang_thai"))
        console.log(trang_thai)
        var elements = `<option>-- Trạng thái --</option>`
        for (item of trang_thai) {
            elements += `<option value="${item.id}">${item.mo_ta}</option>`
        }
        $("#new_hoa_don #trang_thai").html(elements)

        // Load danh sách sản phẩm đang bán
        var san_pham = JSON.parse(sessionStorage.getItem("san_pham"))
        $("#new_hoa_don #san_pham_dang_ban").DataTable({
            destroy: true,
            // info: false,
            responsive: true,
            data: san_pham,
            dataSrc: "",
            columns: [
                {
                    data: "id",
                    render: function (data, type, row) {
                        if (type == "display") {
                            return `<button><</button>`
                        }
                        return data
                    }
                },
                { data: "ten_san_pham" },
                { data: "so_luong" },
                { data: "gia_ban" }
            ]
        })
    })

    $("#list_hoa_don tbody").on("click", "#thanh-toan", function () {
        var data = table.row($(this).parents("tr")).data()
        $("#thanh-toan-hoa-don #id").val(data.id)
        $("#thanh-toan-hoa-don").modal("show")
        var table_chi_tiet = $("#chi-tiet-hoa-don").DataTable({
            destroy: true,
            paging: false,
            info: false,
            searching: false,
            ajax: {
                type: "get",
                url: "/store/data-chi-tiet-hoa-don/" + data.id,
                dataSrc: "data"
            },
            columns: [
                { data: "no" },
                { data: "ten_san_pham" },
                { data: "gia_ban" },
                { data: "so_luong_mua" },
                { data: "thanh_tien" }
            ],
            footerCallback: function (row, data, start, end, display) {
                var api = this.api(), data;

                var intVal = function (i) {
                    return typeof i === "string" ? i.replace(/[\$,]/g, '') * 1 : typeof i === 'number' ?
                        i : 0;
                }

                total = api
                    .column(4)
                    .data()
                    .reduce(function (a, b) {
                        return intVal(a) + intVal(b);
                    }, 0);
                $("#thanh-tien").html(total);
            }
        })
        $("#btn_thanh_toan").on("click", function () {
            var formData = new FormData()
            formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
            formData.append("id_invoice", data.id)
            formData.append("is_paid", "1")
            $.ajax({
                contentType: false,
                processData: false,
                type: "post",
                url: location.url,
                data: formData,
                success: function (data) {
                    table.ajax.reload()
                    $("#thanh-toan-hoa-don").modal("hide")
                    formData = ""
                    if (data.status == "success") {
                        Swal.fire({
                            type: "success",
                            title: "Thành công",
                            text: "Thanh toán thành công",
                            timer: 1000
                        });
                    } else if (data.status == "paided") {
                        Swal.fire({
                            type: "success",
                            title: "Thông báo",
                            text: "Hóa đơn đã được thanh toán",
                            timer: 1000
                        });
                    }
                }
            })
        })

    })

    $("#list_hoa_don tbody").on("click", "#xuat", function () {
        $("#xem-hoa-don").modal("show")
        var data = table.row($(this).parents("tr")).data()
        $.ajax({
            type: "get",
            url: "/store/data-chi-tiet-hoa-don/" + data.id,
            success: function (data) {
                $("#xem-hoa-don #ngay-tao").text(data.ngay_tao)
                $("#xem-hoa-don #nguoi-tao").text(data.nguoi_tao)
                $("#xem-hoa-don #khach-hang").text(data.khach_hang)
                $("#xem-hoa-don #thanh-tien").text(data.thanh_tien)
                var elements = ``
                for (item of data.data) {
                    elements += `<tr class="item">
                    <td>
                        ${item.ten_san_pham}
                    </td>
                    <td>
                        ${item.so_luong_mua}
                    </td>
                    <td>
                        ${item.thanh_tien}
                    </td>
                </tr>`
                }
                $("#xem-hoa-don table #list-san-pham").html(elements)
                $("#xem-hoa-don").modal("show")
                console.log(data)
            }
        })
    })
    $("#xem-hoa-don #btn-in").on("click", function () {
        $("body").first().html($("#xem-hoa-don #khung-modal").html());
        window.print();
        location.reload();
    })

    // Thêm sản phẩm
    $("#new_hoa_don #them-san-pham").on("click", function() {
        $("#danh_sach_hang").modal("show")
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

