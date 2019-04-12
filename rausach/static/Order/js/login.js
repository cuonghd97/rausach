$(document).ready(function () {
    $(".btn-login").on("click", function () {
        var formData = new FormData();
        var username = $("#username").val()
        var password = $("#password").val()
        formData.append("username", username)
        formData.append("password", password)
        formData.append(
            "csrfmiddlewaretoken",
            $("input[name=csrfmiddlewaretoken]").val()
        );

        $.ajax({
            contentType: false,
            processData: false,
            type: "post",
            url: "/auth/login/",
            data: formData,
            beforeSend: function() {
                Swal.fire({
                    title: "Xin chờ...",
                    onBeforeOpen: () => {
                        Swal.showLoading();
                    },
                    allowOutsideClick: false
                });
            },
            success: function(data) {
                var result = JSON.parse(JSON.stringify(data));
                if(result.status == 'error'){
                    Swal.fire({
                        type: 'error',
                        title: 'Lỗi',
                        text: result.messages,
                    });
                }
                else{
                    Swal.fire({
                        type: 'success',
                        title: 'Thành công',
                        text: 'Đăng nhập thành công',
                        showConfirmButton: false,
                        timer: 1000
                    }).then(() =>{
                        window.location.href = result.messages;
                    })
                };
            }
        })
    })
})