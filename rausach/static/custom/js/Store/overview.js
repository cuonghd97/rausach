$(document).ready(function () {

    const valid_date = /(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)/

    // Hàm chuyển về định dạng mm/dd/yyyy
    function convertDate(date) {
        initial = date.split(/\//);
        return [initial[1], initial[0], initial[2]].join('/');
    }

    // Lọc hóa đơn
    $.ajax({
        type: "get",
        url: "/store/data-trang-thai/",
        success: function (data) {
            var element = `<option value="${-1}">Tất cả đơn hàng</option>`
            for (let item of data) {
                element += `<option value="${item.id}">${item.mo_ta}</option>`
            }
            $("#hoa-don #trang-thai").html(element)
        }
    })

    $.ajax({
        type: "get",
        url: "/store/data-dem-hoa-don/",
        success: function (data) {
            var element = ``
            var sum = 0
            for (let item of data) {
                element += `<tr>
                                <td>${item.mo_ta}</td><td>${item.count}</td>
                            </tr>`
                sum += item.count
            }
            element += `<tr>
                            <td>Tổng</td><td>${sum}</td>
                        </tr>`
            $("#hoa-don #summary tbody").html(element)
        }
    })
    function getData(data) {
        var table_hoa_don = $("#hoa-don #invoices").DataTable({
            destroy: true,
            searching: false,
            info: false,
            data: data,
            dataSrc: "",
            columns: [
                {
                    data: "created_at"
                },
                {
                    data: "khach_hang"
                }
            ],
            initComplete: function (settings, json) {
                $("#hoa-don #invoices").on("click", "tr", function () {
                    let data = table_hoa_don.row($(this)).data()
                    console.log(data)
                    $("#chi-tiet-hoa-don").modal("show")
                    $("#chi-tiet-hoa-don #khach-hang").html(data.khach_hang)
                    $("#chi-tiet-hoa-don #dia-chi").html(data.dia_chi)
                    $("#chi-tiet-hoa-don #so-dien-thoai").html(data.so_dien_thoai)
                    $("#chi-tiet-hoa-don #thoi-gian-dat").html(data.created_at)
                    $.ajax({
                        type: "get",
                        url: "/store/data-chi-tiet-hoa-don/" + data.id,
                        success: function (response) {
                            response = response.data
                            let element = ``
                            for (item of response) {
                                element += `<tr>
                                            <td>${item.ten_san_pham}</td>
                                            <td>${item.so_luong_mua}</td>
                                            <td>${item.gia_ban}</td>
                                            </tr>`
                            }
                            $("#chi-tiet-hoa-don table tbody").html(element)
                        }
                    })
                })
            }
        })
    }
    $("#hoa-don #filter").on("click", function () {
        var tu_ngay = $("#hoa-don #tu-ngay").val()
        var den_ngay = $("#hoa-don #den-ngay").val()
        var loc_data = $("#trang-thai").val()
        if (tu_ngay == '' && den_ngay != '') {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đầy đủ khoảng thời gian",
            });
        } else if (tu_ngay != '' && den_ngay == '') {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đầy đủ khoảng thời gian",
            });
        } else if ((!valid_date.test(tu_ngay) || !valid_date.test(den_ngay)) && (tu_ngay != '' && den_ngay != '')) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đúng định dạng thời gian",
            });
        } else {
            if (tu_ngay != '') {
                tu_ngay = tu_ngay.replace(/\//g, "-");
                tu_ngay = tu_ngay
            }
            if (den_ngay != '') {
                den_ngay = den_ngay.replace(/\//g, "-");
                den_ngay = den_ngay
            }

            formData = new FormData()
            formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
            formData.append("tu_ngay", tu_ngay)
            formData.append("den_ngay", den_ngay)
            formData.append("loc_data", loc_data)
            $.ajax({
                contentType: false,
                processData: false,
                type: "post",
                url: "/store/data-loc-hoa-don/",
                data: formData,
                success: function (response) {
                    getData(response)
                }
            })
        }
    })

    // Thống kê sản phẩm
    $.ajax({
        type: "get",
        url: "/store/data-dem-san-pham/",
        success: function(data) {
            $("#san-pham #tong-so").html(data.so_luong_san_pham)
            let theo_loai_hang = data.theo_loai_hang
            let theo_nha_cung_cap = data.theo_nha_cung_cap
            element = ``
            for (item of theo_loai_hang) {
                element += `<tr>
                                <td>${item.ten_loai}</td><td>${item.count}</td>
                            </tr>`
            }
            $("#san-pham #theo-loai-hang tbody").html(element)
            element = ``
            for (item of theo_nha_cung_cap) {
                element += `<tr>
                                <td>${item.ten_nha_cung_cap}</td><td>${item.count}</td>
                            </tr>`
            }
            $("#san-pham #theo-nha-cung-cap tbody").html(element)
        }
    })

    // Thống kê doanh thu
    $("#doanh-thu #filter").on("click", function () {
        var tu_ngay = $("#doanh-thu #tu-ngay").val()
        var den_ngay = $("#doanh-thu #den-ngay").val()
        if (tu_ngay == '' && den_ngay != '') {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đầy đủ khoảng thời gian",
            });
        } else if (tu_ngay != '' && den_ngay == '') {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đầy đủ khoảng thời gian",
            });
        } else if ((!valid_date.test(tu_ngay) || !valid_date.test(den_ngay)) && (tu_ngay != '' && den_ngay != '')) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Vui lòng nhập đúng định dạng thời gian",
            });
        } else {
            if (tu_ngay != '') {
                tu_ngay = tu_ngay.replace(/\//g, "-");
                tu_ngay = tu_ngay
            }
            if (den_ngay != '') {
                den_ngay = den_ngay.replace(/\//g, "-");
                den_ngay = den_ngay
            }
            formData = new FormData()
            formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
            formData.append("tu_ngay", tu_ngay)
            formData.append("den_ngay", den_ngay)

            $.ajax({
                contentType: false,
                processData: false,
                type: "post",
                url: "/store/data-doanh-thu/",
                data: formData,
                success: function(data) {
                    console.log(data)
                    $("#doanh-thu #doanh-thu-data").html(data.tong)

                    var table_doanh_thu = $("#doanh-thu #invoices").DataTable({
                        destroy: true,
                        searching: false,
                        info: false,
                            data: data.data,
                            dataSrc: "",
                        columns: [
                            {data: "created_at"},
                            {data: "khach_hang"}
                        ],
                        initComplete: function(settings, json) {
                            $("#doanh-thu #invoices").on("click", "tr", function () {
                                let data = table_doanh_thu.row($(this)).data()
                                console.log(data)
                                $("#chi-tiet-hoa-don").modal("show")
                                $("#chi-tiet-hoa-don #khach-hang").html(data.khach_hang)
                                $("#chi-tiet-hoa-don #dia-chi").html(data.dia_chi)
                                $("#chi-tiet-hoa-don #so-dien-thoai").html(data.so_dien_thoai)
                                $("#chi-tiet-hoa-don #thoi-gian-dat").html(data.created_at)
                                $.ajax({
                                    type: "get",
                                    url: "/store/data-chi-tiet-hoa-don/" + data.id,
                                    success: function (response) {
                                        response = response.data
                                        let element = ``
                                        for (item of response) {
                                            element += `<tr>
                                                        <td>${item.ten_san_pham}</td>
                                                        <td>${item.so_luong_mua}</td>
                                                        <td>${item.gia_ban}</td>
                                                        </tr>`
                                        }
                                        $("#chi-tiet-hoa-don table tbody").html(element)
                                    }
                                })
                            })
                        }
                    })
                }
            })
        }
    })
})