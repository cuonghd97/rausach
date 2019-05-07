$(document).ready(function() {
    function callData() {
        $.ajax({
            type: "get",
            url: "/data-ten-san-pham/",
            success: function(data) {
                localStorage.setItem("data_name", JSON.stringify(data))
            }
        })
    }
    callData()
    $( function() {
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
        $( "#search-text" ).autocomplete({
          source: availableTags
        });
      } );
})