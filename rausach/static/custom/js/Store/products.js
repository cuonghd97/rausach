$(document).ready(function() {
	$.ajax({
		type: "get",
		url: "/store/data-nha-cung-cap/",
		success: function(data) {
			sessionStorage.setItem("nha_cung_cap", JSON.stringify(data));
		}
	});

	$.ajax({
		type: "get",
		url: "/store/data-loai-hang/",
		success: function(data) {
			sessionStorage.setItem("loai_hang", JSON.stringify(data));
		}
	});

	$("#btn_add_product").on("click", function() {
		nha_cung_cap = JSON.parse(sessionStorage.getItem("nha_cung_cap"));
		var ncc = `<option>--Nhà cung cấp--</option>`;
		nha_cung_cap.map(function(item) {
			ncc += `<option value="${item.id}">${item.ten_nha_cung_cap}</option>`;
		});
		$("#new_san_pham #nha_cung_cap").html(ncc);

		loai_hang = JSON.parse(sessionStorage.getItem("loai_hang"));
		hang = `<option>--Loại hàng--</option>`;
		loai_hang.map(function(item) {
			hang += `<option value="${item.id}">${item.ten_loai}</option>`;
		});
		$("#new_san_pham #loai_hang").html(hang);
	});

	// Thêm sản phẩm
	$("#new_san_pham #btn_create_product").on("click", function() {
		var formData = new FormData();

		var ten_san_pham = $("#new_san_pham #ten_san_pham").val();
		var gia_von = $("#new_san_pham #gia_von").val();
		var gia_ban = $("#new_san_pham #gia_ban").val();
		var so_luong = $("#new_san_pham #so_luong").val();
		var loai_hang = $("#new_san_pham #loai_hang").val();
		var nha_cung_cap = $("#new_san_pham #nha_cung_cap").val();
		var mo_ta = $("#new_san_pham #mo_ta").val();

        var image = $("#new_san_pham #image")[0].files;
        data = []
        for (let i=0; i<image.length; i++) {
            formData.append("anh", image[i])
		}

		formData.append("ten_san_pham", ten_san_pham)
		formData.append("gia_von", gia_von)
		formData.append("gia_ban", gia_ban)
		formData.append("so_luong", so_luong)
		formData.append("loai_hang", loai_hang)
		formData.append("nha_cung_cap", nha_cung_cap)
		formData.append("mo_ta", mo_ta)
		formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
		console.log(formData)
		$.ajax({
            contentType: false,
            processData: false,
			type: "post",
			url: "/store/post-san-pham/",
			data: formData,
			success:  function() {
				console.log("success")
			}
		});
	});
});
