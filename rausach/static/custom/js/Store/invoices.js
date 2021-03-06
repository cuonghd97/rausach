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
            { data: "trang_thai" },
            { data: "created_at" },
        ],
        columnDefs: [
            {
                width: "30%",
                targets: 4,
                data: null,
                defaultContent: `<div class="btn-group" role="group" aria-label="Basic example">
                                <button class="btn btn-primary" id="xuat">Xuất hóa đơn</button>
                                <button class="btn btn-info" id="sua">Duyệt</button>
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

    // Xóa đơn hàng
    $("#list_hoa_don tbody").on("click", "#xoa", function () {
        var data = table.row($(this).parents("tr")).data()
        var id_hoa_don = data.id

        $.ajax({
            type: "post",
            url: location.url,
            data: {
                id_hoa_don: id_hoa_don,
                is_delete_hd: 1,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data) {
                table.ajax.reload()
                if (data.status == "success") {
                    Swal.fire({
                        type: "success",
                        title: "Thành công",
                        text: data.messages,
                        timer: 1000
                    });
                } else {
                    Swal.fire({
                        type: "error",
                        title: "Lỗi",
                        text: data.messages,
                        timer: 1000
                    });
                }
            }
        })
    })

    // Sửa thông tin đơn hàng
    $("#list_hoa_don tbody").on("click", "#sua", function () {
        var data = table.row($(this).parents("tr")).data()
        $("#sua-trang-thai #id").val(data.id)
        $("#sua-trang-thai").modal("show")
        $("#sua-trang-thai #khung-modal select").empty()
        $("#sua-trang-thai #khach-hang").html(data.khach_hang)
        $("#sua-trang-thai #dia-chi").html(data.dia_chi)
        $("#sua-trang-thai #so-dien-thoai").html(data.so_dien_thoai)
        $("#sua-trang-thai #thoi-gian-dat").html(data.created_at)
        var ma_trang_thai = data.ma_trang_thai
        $.ajax({
            type: "get",
            url: "/store/data-trang-thai/",
            success: function (data) {
                var elements = ``
                for (item of data) {
                    // if (item.ma )
                    elements += `<option value="${item.ma}">${item.mo_ta}</option>`
                }
                $("#sua-trang-thai #trang_thai").html(elements)
                $("#sua-trang-thai #trang_thai").val(ma_trang_thai)
            },
            // complete:
        })
        var chi_tiet_hoa_don_table = $("#sua-trang-thai #hoa-don").DataTable({
            destroy: true,
            paging: false,
            searching: false,
            info: false,
            ajax: {
                type: "get",
                url: "/store/data-chi-tiet-hoa-don/" + data.id,
                dataSrc: "data"
            },
            columns: [
                { data: "ten_san_pham" },
                { data: "so_luong_mua" },
                { data: "trang_thai" },
                { data: "gia_ban" }
            ],
            columnDefs: [
                {
                    targets: 4,
                    data: null,
                    defaultContent: `<button
                                        class="btn btn-danger btn-xs"
                                        id="btn-remove"
                                    >
                                        <i class="fa fa-times"></i>
                                    </button>`
                }
            ],
            createdRow: function (row, data, dataIndex) {
                $(row).find("#btn-remove").attr("data-id", data["id"])
            },
            initComplete: function (settings, json) {
                $("#sua-trang-thai #btn-remove").on("click", function () {
                    console.log($(this).data("id"))
                    var id_san_pham_cthd = $(this).data("id")
                    $.ajax({
                        type: "post",
                        url: location.url,
                        data: {
                            is_remove_in_order_detail: 1,
                            id_san_pham_cthd: id_san_pham_cthd,
                            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                        },
                        success: function (data) {
                            chi_tiet_hoa_don_table.ajax.reload()
                        }
                    })
                })
            }
        })
    })

    $("#sua-trang-thai #btn-luu").on("click", function () {
        console.log($("#sua-trang-thai #trang_thai").val())
        var formData = new FormData();
        formData.append("id_hoa_don", $("#sua-trang-thai #id").val())
        formData.append("trang_thai", $("#sua-trang-thai #trang_thai").val())
        formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
        formData.append("is_change_status", 1)
        $.ajax({
            contentType: false,
            processData: false,
            type: "post",
            url: location.url,
            data: formData,
            success: function (data) {
                console.log(data)
                $("#sua-trang-thai").modal("hide")
                if (data.status == "success") {
                    Swal.fire({
                        type: "success",
                        title: "Thành công",
                        text: data.messages,
                        timer: 1000
                    });
                } else {
                    Swal.fire({
                        type: "error",
                        title: "Lỗi",
                        text: data.messages,
                        timer: 1000
                    });
                }
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

