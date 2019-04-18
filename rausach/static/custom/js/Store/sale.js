$(document).ready(function () {
    var table = $("#list_san_pham").DataTable({
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
        ]
    })

    $("#table_body").on("click", "tr", function() {
        console.log("click")
        $("#chi_tiet_hang").modal("show")
    })
})