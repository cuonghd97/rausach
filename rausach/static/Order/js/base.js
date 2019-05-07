$(document).ready(function () {
    function formatNumber(num) {
        return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,') + ' ' + '&#8363;'
    }
    $(".gia-ban").each(function () {
        $(this).html(formatNumber($(this).text()))
    })
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
    $(".loc-hang").on("click", function () {
        var loai_hang = to_slug($(this).text())
        var id = $(this).data("id")
        $(this).attr("href", `/filter/${loai_hang}_${id}`)
    })
    $(".ten_san_pham").on("click", function () {
        var ten = $(this).data("tensp") + ""
        var ten_san_pham = to_slug(ten)
        var id = $(this).data("id")
        $(this).attr("href", `/detail/hang/${ten_san_pham}_${id}`)
    })

    function callData() {
        $.ajax({
            type: "get",
            url: "/data-ten-san-pham/",
            success: function (data) {
                localStorage.setItem("data_name", JSON.stringify(data))
            }
        })
    }
    callData()
    $(function () {
        var availableTags;
        if (localStorage.getItem("data_name") == "") {
            callData()
        } else {
            data = localStorage.getItem("data_name")
            availableTags = JSON.parse(data)
        }
        // var availableTags = [
        //   "ActionScript",
        //   "AppleScript",
        //   "Asp",
        //   "BASIC",
        //   "C",
        //   "C++",
        //   "Clojure",
        //   "COBOL",
        //   "ColdFusion",
        //   "Erlang",
        //   "Fortran",
        //   "Groovy",
        //   "Haskell",
        //   "Java",
        //   "JavaScript",
        //   "Lisp",
        //   "Perl",
        //   "PHP",
        //   "Python",
        //   "Ruby",
        //   "Scala",
        //   "Scheme"
        // ];
        $("#search-text").autocomplete({
            source: availableTags
        });
    });
    $("#search-button").on("click", function () {
        $(this).attr("href", `/search/${$("#search-text").val()}`)
    })
})