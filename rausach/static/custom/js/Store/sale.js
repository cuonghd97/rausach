$(document).ready(function () {
    $("#list_san_pham").DataTable({
        ajax: {
            type: "get",
            url: "/store/data-san-pham/",
            dataSrc: ""
        },
        columns: [
            { data: "no" },
            { data: "ten_san_pham" },
            { data: "gia_ban" },
            { data: "ton_kho" }
        ],
        drawCallback: function () {
            $('tr').popover({
                "html": true,
                trigger: 'manual',
                placement: 'left',
                "content": function () {
                    return "<div>Popover content</div>";
                }
            })
        }
    })

    // $("#list-san-pham tr").popover({
    //     html: true,
    //     trigger: "hover",
    //     placement: "bottom",
    //     content: function() {
    //         return `<img src="placehold.it/100x50">`
    //     }
    // })
})