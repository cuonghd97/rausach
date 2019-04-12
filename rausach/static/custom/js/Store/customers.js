$(document).ready(function () {
    // Load data tỉnh
    var location = {};
    $.ajax({
        type: "get",
        url: "/store/data-tinh/",
        success: function (data) {
            sessionStorage.setItem("tinh", JSON.stringify(data));
        }
    });

    // Load data huyện
    $.ajax({
        type: "get",
        url: "/store/data-huyen/",
        success: function (data) {
            sessionStorage.setItem("huyen", JSON.stringify(data));
        }
    });

    // Load bảng nhân viên
    // $.ajax({
    // type: "get",
    // url: "/store/data-nhan-vien/",
    // success: function(data) {
    // console.log(data)
    // }
    // })
    var table = $("#list_nguoi_dung").DataTable({
        destroy: true,
        ajax: {
            type: "get",
            url: "/store/data-nguoi-dung/",
            dataSrc: ""
        },
        columns: [
            { data: "no" },
            { data: "ho_ten" },
            {
                data: "gioi_tinh",
                render: function (data, type, row) {
                    if (type == "display") {
                        if (data == "nam") {
                            return "Nam";
                        } else if (data == "nu") {
                            return "Nữ";
                        } else if (data == "oth") {
                            return "Khác";
                        } else {
                            return " ";
                        }
                    }
                    return data;
                }
            },
            {
                data: "is_active",
                render: function (data, type, row) {
                    if (type == "display") {
                        if (data == true) {
                            return `<input type="radio" disabled checked>`;
                        } else {
                            return `<input type="radio" disabled>`;
                        }
                    }
                    return data;
                }
            }
        ],
        columnDefs: [
            {
                targets: 4,
                data: null,
                defaultContent: `<center>
				<button class="btn btn-danger" id="delete" data-toggle="tooltip" title="Xóa người dùng này"><i class="fa fa-times"></i></button>
				<button class="btn btn-primary" id="edit" data-toggle="tooltip" title="Sửa người dùng này"><i class="fa fa-edit"></i></button>
				</center>`
            }
        ]
    });

    const valid_date = /^(19[5-9][0-9]|20[0-4][0-9]|2050)[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12][0-9]|3[01])$/;
    // Thêm mới nhân viên
    $("#btn_new_nguoi_dung").on("click", function () {
        $("#new_nguoi_dung .form-group")
            .find("input")
            .val("");
        $("#new_nguoi_dung .form-group")
            .find("select")
            .val("");
        var elements = `<option>--Tỉnh--</option>`;
        var tinh = JSON.parse(sessionStorage.getItem("tinh"));
        tinh.map(function (item) {
            elements += `<option value="${item.provinceid}">${item.name}</option>`;
        });
        $("#new_nguoi_dung #tinh").html(elements);
    });

    $("#new_nguoi_dung #tinh").on("change", function () {
        var id_tinh = $(this).val();
        var huyen = JSON.parse(sessionStorage.getItem("huyen"));
        var elements = `<option>--Huyện--</option>`;
        huyen.map(function (item) {
            if (item.provinceid == id_tinh) {
                elements += `<option value="${item.districtid}">${item.name}</option>`;
            }
        });
        $("#new_nguoi_dung #huyen").html(elements);
    });

    // Tạo mới nhân viên
    $("#btn_create_nguoi_dung").on("click", function () {
        var ten_nguoi_dung = $("#new_nguoi_dung #ten_nguoi_dung").val();
        var username = $("#new_nguoi_dung #username").val();
        var gioi_tinh = $("#new_nguoi_dung #gioi_tinh").val();
        var email = $("#new_nguoi_dung #email").val();
        var sdt = $("#new_nguoi_dung #sdt").val();
        var address = $("#new_nguoi_dung #address").val();
        var tinh = $("#new_nguoi_dung #tinh").val();
        var huyen = $("#new_nguoi_dung #huyen").val();
        var role = 3
        var ngay_sinh = $("#new_nguoi_dung #ngay_sinh").val();
        var luong = $("#new_nguoi_dung #luong").val();
        var anh = $("#new_nguoi_dung #image")[0].files[0];
        var formData = new FormData();
        if (
            ten_nguoi_dung == "" ||
            username == "" ||
            gioi_tinh == "" ||
            email == "" ||
            sdt == "" ||
            ngay_sinh == "" ||
            luong == "" ||
            anh == ""
        ) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Các trường không được bỏ trống"
            });
        } else if (valid_date.test(ngay_sinh) == false) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Nhập sai ngày sinh"
            });
        } else {
            formData.append("ten_nguoi_dung", ten_nguoi_dung);
            formData.append("username", username);
            formData.append("gioi_tinh", gioi_tinh);
            formData.append("email", email);
            formData.append("sdt", sdt);
            formData.append("address", address);
            formData.append("tinh", tinh);
            formData.append("huyen", huyen);
            formData.append("role", role);
            formData.append("ngay_sinh", ngay_sinh);
            formData.append("luong", luong);
            formData.append("anh", anh);
            formData.append("is_add", 1);
            formData.append(
                "csrfmiddlewaretoken",
                $("input[name=csrfmiddlewaretoken]").val()
            );
            $.ajax({
                contentType: false,
                processData: false,
                type: "post",
                url: "/store/post-nguoi-dung/",
                data: formData,
                beforeSend: function () {
                    Swal.fire({
                        title: "Đang tải...",
                        onBeforeOpen: () => {
                            Swal.showLoading();
                        },
                        allowOutsideClick: false
                    });
                },
                success: function (data) {
                    Swal.close();
                    table.ajax.reload()
                }
            });
        }
    });

    // Sửa thông tin nhân viên
    $("#list_nguoi_dung tbody").on("click", "#edit", function () {
        $("#edit_nguoi_dung").modal("show");
        var data = table.row($(this).parents("tr")).data();
        console.log(data)

        if (data.is_active == true) {
            $("#edit_nguoi_dung").find("#is_active").prop("checked", true);
        } else {
            $("#edit_nguoi_dung").find("#is_active").prop("checked", false);
        }
        // Load danh sách tỉnh
        var elements = `<option>--Tỉnh--</option>`;
        var tinh = JSON.parse(sessionStorage.getItem("tinh"));
        tinh.map(function (item) {
            elements += `<option value="${item.provinceid}">${item.name}</option>`;
        });
        $("#edit_nguoi_dung #tinh").html(elements);

        // Load danh sách huyện
        var id_tinh = data.tinh;
        var huyen = JSON.parse(sessionStorage.getItem("huyen"));
        var elements = `<option>--Huyện--</option>`;
        huyen.map(function (item) {
            if (item.provinceid == id_tinh) {
                elements += `<option value="${item.districtid}">${item.name}</option>`;
            }
        });
        $("#edit_nguoi_dung #huyen").html(elements);

        // Huyện thay đổi theo tỉnh
        $("#edit_nguoi_dung #tinh").on("change", function () {
            var id_tinh = $(this).val();
            var huyen = JSON.parse(sessionStorage.getItem("huyen"));
            var elements = `<option>--Huyện--</option>`;
            huyen.map(function (item) {
                if (item.provinceid == id_tinh) {
                    elements += `<option value="${item.districtid}">${
                        item.name
                        }</option>`;
                }
            });
            $("#edit_nguoi_dung #huyen").html(elements);
        });

        // Lấy data của nhân viên đưa lên modal sửa
        $("#edit_nguoi_dung #tinh").val(data.tinh)
        $("#edit_nguoi_dung #huyen").val(data.huyen)
        $("#edit_nguoi_dung #ten_nguoi_dung").val(data.ho_ten)
        $("#edit_nguoi_dung #username").val(data.username)
        $("#edit_nguoi_dung #gioi_tinh").val(data.gioi_tinh)
        $("#edit_nguoi_dung #email").val(data.email)
        $("#edit_nguoi_dung #sdt").val(data.sdt)
        $("#edit_nguoi_dung #address").val(data.dia_chi)
        $("#edit_nguoi_dung #ngay_sinh").val(data.ngay_sinh)
        $("#edit_nguoi_dung #luong").val(data.luong)
        $("#edit_nguoi_dung #id").val(data.id)
        $("#edit_nguoi_dung #image").attr("src", "/media/" + data.avatar)
    });

    $("#btn_save_nguoi_dung").on("click", function () {
        var is_active = 0;
        if ($('#edit_nguoi_dung #is_active').is(":checked") == true) {
            is_active = 1;
        }
        var ten_nguoi_dung = $("#edit_nguoi_dung #ten_nguoi_dung").val();
        var username = $("#edit_nguoi_dung #username").val();
        var gioi_tinh = $("#edit_nguoi_dung #gioi_tinh").val();
        var email = $("#edit_nguoi_dung #email").val();
        var sdt = $("#edit_nguoi_dung #sdt").val();
        var address = $("#edit_nguoi_dung #address").val();
        var tinh = $("#edit_nguoi_dung #tinh").val();
        var huyen = $("#edit_nguoi_dung #huyen").val();
        var role = 3;
        var ngay_sinh = $("#edit_nguoi_dung #ngay_sinh").val();
        var luong = $("#edit_nguoi_dung #luong").val();
        var id = $("#edit_nguoi_dung #id").val();
        var anh = $("#edit_nguoi_dung #new_image")[0].files[0];
        var formData = new FormData();
        if (
            ten_nguoi_dung == "" ||
            username == "" ||
            gioi_tinh == "" ||
            email == "" ||
            sdt == "" ||
            ngay_sinh == "" ||
            luong == "" ||
            anh == ""
        ) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Các trường không được bỏ trống"
            });
        } else if (valid_date.test(ngay_sinh) == false) {
            Swal.fire({
                type: "error",
                title: "Lỗi",
                text: "Nhập sai ngày sinh"
            });
        } else {
            formData.append("ten_nguoi_dung", ten_nguoi_dung);
            formData.append("username", username);
            formData.append("gioi_tinh", gioi_tinh);
            formData.append("email", email);
            formData.append("sdt", sdt);
            formData.append("address", address);
            formData.append("tinh", tinh);
            formData.append("huyen", huyen);
            formData.append("role", role);
            formData.append("ngay_sinh", ngay_sinh);
            formData.append("luong", luong);
            formData.append("id", id);
            formData.append("anh", anh);
            formData.append("is_edit", 1);
            formData.append("is_active", is_active);
            formData.append(
                "csrfmiddlewaretoken",
                $("input[name=csrfmiddlewaretoken]").val()
            );
            $.ajax({
                contentType: false,
                processData: false,
                type: "post",
                url: "/store/post-nguoi-dung/",
                data: formData,
                beforeSend: function () {
                    Swal.fire({
                        title: "Đang tải...",
                        onBeforeOpen: () => {
                            Swal.showLoading();
                        },
                        allowOutsideClick: false
                    });
                },
                success: function (data) {
                    $("#edit_nguoi_dung").modal("hide");
                    Swal.close();
                    table.ajax.reload()
                }
            });
        }
    })

    $("#list_nguoi_dung tbody").on("click", "#delete", function () {
        var formData = new FormData();
        var data = table.row($(this).parents("tr")).data();
        Swal.fire({
            title: "Xóa giáo sản nhân viên này?",
            text: "Dữ liệu sẽ không thể phục hồi!",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            cancelButtonText: "Hủy",
            confirmButtonText: "Xóa!"
        }).then(function (result) {
            if (result.value) {
                formData.append("id", data.id);
                formData.append("is_delete", 1);
                formData.append(
                    "csrfmiddlewaretoken",
                    $("input[name=csrfmiddlewaretoken]").val()
                );
                $.ajax({
                    contentType: false,
                    processData: false,
                    type: "post",
                    url: "/store/post-nguoi-dung/",
                    data: formData,
                    beforeSend: function () {
                        Swal.fire({
                            title: "Đang tải...",
                            onBeforeOpen: () => {
                                Swal.showLoading();
                            },
                            allowOutsideClick: false
                        });
                    },
                    success: function () {
                        table.ajax.reload();
                        Swal.fire({
                            type: "success",
                            title: "Thành công",
                            text: "Xóa thành công",
                            timer: 1000
                        });
                    }
                });
            }
        });
    })
});
