$(document).ready(function () {
    function to_slug(str) {
        // Chuyển hết sang chữ thường
        str = str.toLowerCase();

        // xóa dấu
        str = str.replace(/(à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ)/g, 'a');
        str = str.replace(/(è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ)/g, 'e');
        str = str.replace(/(ì|í|ị|ỉ|ĩ)/g, 'i');
        str = str.replace(/(ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ)/g, 'o');
        str = str.replace(/(ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ)/g, 'u');
        str = str.replace(/(ỳ|ý|ỵ|ỷ|ỹ)/g, 'y');
        str = str.replace(/(đ)/g, 'd');

        // Xóa ký tự đặc biệt
        str = str.replace(/([^0-9a-z-\s])/g, '');

        // Xóa khoảng trắng thay bằng ký tự -
        str = str.replace(/(\s+)/g, '-');

        // xóa phần dự - ở đầu
        str = str.replace(/^-+/g, '');

        // xóa phần dư - ở cuối
        str = str.replace(/-+$/g, '');

        // return
        return str;
    }
    var table = $("#table-cart").DataTable({
        searching: false,
        destroy: true,
        info: false,
        paging: false,
        ajax: {
            type: "get",
            url: "/data-gio-hang/",
            dataSrc: ""
        },
        columns: [
            {
                data: "no",
                width: "10%"
            },
            {
                width: "50%",
                data: "ten_hang",
                render: function (data, type, row) {
                    if (type == "display") {
                        return `<a href="#">${data}</a>`
                    }
                    return data
                }
            },
            {
                data: "so_luong",
                render: function (data, type, row) {
                    if (type == "display") {
                        return `<input type="number" value="${data}" disabled>`
                    }
                    return data
                }
            }
        ],
        columnDefs: [
            {
                targets: 3,
                data: null,
                defaultContent: `<center><button class="alert button" id="remove"><i class="fi-x"></i><button></center>`
            }
        ],
        createdRow: function (row, data, dataIndex) {
            $(row).find("a").attr("href", `/detail/hang/${to_slug(data["ten_hang"])}_${data["id_hang"]}/`)

        }
    })

    $("#table-cart tbody").on("click", "#remove", function () {
        var data = table.row($(this).parents("tr")).data()
        formData = new FormData()
        formData.append(
            "csrfmiddlewaretoken",
            $("input[name=csrfmiddlewaretoken]").val()
        );
        formData.append("id_hang_dat", data.id)
        formData.append("is_remove", 1)

        $.ajax({
            contentType: false,
            processData: false,
            type: "post",
            url: location.url,
            data: formData,
            beforeSend: function () {
                Swal.fire({
                    title: "Xin chờ...",
                    onBeforeOpen: () => {
                        Swal.showLoading();
                    },
                    allowOutsideClick: false
                });
            },
            success: function (data) {
                table.ajax.reload()
                if (data.status == 'success') {
                    Swal.fire({
                        type: 'success',
                        title: 'Thành công',
                        timer: 1000
                    })
                } else {
                    Swal.fire({
                        type: 'error',
                        title: 'Lỗi',
                    })
                }
            }
        })
    })

    // Đặt hàng
    $("#btn-dat-hang").on("click", function () {
        var data = table.rows().data()
        var cart = []
        for (let i = 0; i < data.length; i++) {
            obj = {}
            obj.id_hang_dat = data[i].id
            obj.id_hang = data[i].id_hang
            obj.so_luong = data[i].so_luong

            cart.push(obj)
        }
        formData = new FormData()
        formData.append(
            "csrfmiddlewaretoken",
            $("input[name=csrfmiddlewaretoken]").val()
        );
        console.log(JSON.stringify(cart))
        cart = JSON.stringify(cart)
        formData.append('data', cart)
        $.ajax({
            contentType: false,
            processData: false,
            type: "post",
            url: location.url,
            data: formData,
            success: function (data) {
                if (data.status == 'success') {
                    Swal.fire({
                        type: 'success',
                        title: 'Thành công',
                        timer: 1000
                    })
                } else {
                    Swal.fire({
                        type: 'error',
                        title: 'Lỗi',
                    })
                }
            }
        })
    })

    // Danh sách hàng đã đặt
    var table_ordered = $("#ordered-cart").DataTable({
        destroy: true,
        info: false,
        paging: false,
        searching: false,
        ajax: {
            type: "get",
            url: "/data-hoa-don/",
            dataSrc: ""
        },
        columns: [
            {
                width: "10%",
                data: "no"
            },
            {
                width: "60%",
                data: "ten_san_pham"
            },
            { data: "so_luong" }
        ]
    })

    $("#btn-da-dat-hang").on("click", function () {
        table_ordered.ajax.reload()
        $("#cart-list").prop("hidden", true)
        $("#ordered-list").prop("hidden", false)
        $("#ordered-list #ordered-cart").css("width", "100%")
        $("#btn-dat-hang").css("display", "none")
        $("#xem-hang-dat").css("display", "initial")
        $(this).css("display", "none")
    })

    $("#xem-hang-dat").on("click", function () {
        $("#cart-list").prop("hidden", false)
        $("#ordered-list").prop("hidden", true)
        $("#btn-dat-hang").css("display", "initial")
        $("#btn-da-dat-hang").css("display", "initial")
        $(this).css("display", "none")
    })
})