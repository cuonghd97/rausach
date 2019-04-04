$(document).ready(function() {
	// Load data tỉnh
	var location = {};
	$.ajax({
		type: "get",
		url: "/store/data-tinh/",
		success: function(data) {
			sessionStorage.setItem("tinh", JSON.stringify(data));
		}
	});

	// Load data huyện
	$.ajax({
		type: "get",
		url: "/store/data-huyen/",
		success: function(data) {
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
	$("#list_nhan_vien").DataTable({
		destroy: true,
		ajax: {
			type: "get",
			url: "/store/data-nhan-vien/",
			dataSrc: ""
		},
		columns: [
			{ data: "no" },
			{ data: "ho_ten" },
			{ data: "role" },
			{ data: "luong" },
			{ data: "gioi_tinh" },
			{ data: "is_active" }
		],
		columnDefs: [
			{
				targets: 6,
				data: null,
				defaultContent: `<button>click</button>`
			}
		]
	});

	const valid_date = /^(19[5-9][0-9]|20[0-4][0-9]|2050)[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12][0-9]|3[01])$/;
	$("#btn_new_nhan_vien").on("click", function() {
		$("#new_nhan_vien .form-group")
			.find("input")
			.val("");
		$("#new_nhan_vien .form-group")
			.find("select")
			.val("");
		var elements = `<option>--Tỉnh--</option>`;
		var tinh = JSON.parse(sessionStorage.getItem("tinh"));
		tinh.map(function(item) {
			elements += `<option value="${item.provinceid}">${item.name}</option>`;
		});
		$("#new_nhan_vien #tinh").html(elements);
	});

	$("#new_nhan_vien #tinh").on("change", function() {
		var id_tinh = $(this).val();
		var huyen = JSON.parse(sessionStorage.getItem("huyen"));
		var elements = `<option>--Huyện--</option>`;
		huyen.map(function(item) {
			if (item.provinceid == id_tinh) {
				elements += `<option value="${item.districtid}">${item.name}</option>`;
			}
		});
		$("#new_nhan_vien #huyen").html(elements);
	});

	// Tạo mới nhân viên
	$("#btn_create_nhan_vien").on("click", function() {
		var ten_nhan_vien = $("#new_nhan_vien #ten_nhan_vien").val();
		var username = $("#new_nhan_vien #username").val();
		var gioi_tinh = $("#new_nhan_vien #gioi_tinh").val();
		var email = $("#new_nhan_vien #email").val();
		var sdt = $("#new_nhan_vien #sdt").val();
		var address = $("#new_nhan_vien #address").val();
		var tinh = $("#new_nhan_vien #tinh").val();
		var huyen = $("#new_nhan_vien #huyen").val();
		var role = $("#new_nhan_vien #role").val();
		var ngay_sinh = $("#new_nhan_vien #ngay_sinh").val();
		var luong = $("#new_nhan_vien #luong").val();
		var anh = $("#new_nhan_vien #image")[0].files[0];
		var formData = new FormData();
		if (
			ten_nhan_vien == "" ||
			username == "" ||
			gioi_tinh == "" ||
			email == "" ||
			sdt == "" ||
			role == "" ||
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
			ten_nhan_vien;
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
				url: "/store/post-nhan-vien/",
				data: formData,
				beforeSend: function() {
					Swal.fire({
						title: "Đang tải...",
						onBeforeOpen: () => {
							Swal.showLoading();
						},
						allowOutsideClick: false
					});
				},
				success: function(data) {
					Swal.close();
					console.log(data);
				}
			});
		}
	});
});
