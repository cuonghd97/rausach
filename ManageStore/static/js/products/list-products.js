$(document).ready(() => {
    $("#image").on("change", () => {
        if ($("#image")[0].files.length > 5) {
            $('#submit').prop('disabled', 'disabled')
            alert('bạn chỉ được chọn tối đa 5 ảnh')
        } else {
            $('#submit').prop('disabled', false)
        }
    })
    $.ajax({
        method: 'get',
        url: '/manage-shop/data-products',
        success: (data) => {
            var elements = ``
            data.map(item => {
                elements += `<tr>
                    <td>${item.no}</td>
                    <td>${item.ten_hang}</td>
                    <td>${item.ngay_nhap}</td>
                    <td>${item.gia_ban}</td>
                    <td>${item.gia_von}</td>
                    <td><button data-idhang=${item.id} id='detail'>click</button></td>
                </tr>`
            })

            $("#body-table").html(elements)
        }
    })

    $('#datatable').DataTable()

    $("#body-table").on('click', 'button', function() {
        console.log($(this).data())
    })
})