$(document).ready(function () {
    $("#table-cart").DataTable({
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
                        return `<input type="number" value="${data}">`
                    }
                    return data
                }
            }
        ],
        columnDefs: [
            {
                targets: 3,
                data: null,
                defaultContent: `<center><button class="alert button"><i class="fi-x"></i><button></center>`
            }
        ],
        createdRow: function (row, data, dataIndex) {
            $(row).find("a").attr("data-id", data["id"]).attr("data-tensp", data["ten_hang"]).addClass("ten_san_pham")
        }
    })
    $(".ten_san_pham").on("click", function () {
        var ten = $(this).data("tensp") + ""
        var ten_san_pham = to_slug(ten)
        var id = $(this).data("id")
        $(this).attr("href", `/detail/hang/${ten_san_pham}_${id}`)
    })
})