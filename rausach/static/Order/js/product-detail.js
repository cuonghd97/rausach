$(document).ready(function () {
    $("#btn-add-to-cart").on("click", function () {
        if (parseInt($("#so_luong_mua").val()) > parseInt($("#so_luong_con").val())) {
            Swal.fire({
                type: 'error',
                title: 'Lỗi',
                text: 'Số lượng hàng đặt phải nhỏ hơn số lượng có',
            })
        } else if ($("#so_luong_mua").val() <= 0) {
            Swal.fire({
                type: 'error',
                title: 'Lỗi',
                text: 'Số lượng hàng đặt không hợp lệ',
            })
        } else {
            var formData = new FormData()
            formData.append('hang_dat', $("#id").val())
            formData.append('so_luong', $("#so_luong_mua").val())
            formData.append(
                "csrfmiddlewaretoken",
                $("input[name=csrfmiddlewaretoken]").val()
            );
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
                    if (data.status == 'success') {
                        Swal.fire({
                            type: 'success',
                            title: 'Thành công',
                            text: 'Thêm vào giỏ hàng thành công',
                            timer: 1000
                        })
                    } else {
                        Swal.fire({
                            type: 'error',
                            title: 'Lỗi',
                            text: 'Thêm vào giỏ không thành công',
                        })
                    }
                }
            })
        }
    })
})