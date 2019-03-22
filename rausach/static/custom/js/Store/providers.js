$(document).ready(function() {
	// Load dữ liệu lên bảng danh sách nhà cung cấp
	var table = $("#list_nha_cung_cap").DataTable({
		ajax: {
			type: "get",
			url: "/store/data-nha-cung-cap/",
			dataSrc: ""
		},
		columns: [
			{ data: "no" },
			{ data: "ten_nha_cung_cap" },
			{ data: "so_dien_thoai" },
			{ data: "email" },
			{
				data: "is_active",
				render: function(data, type) {
					if (type == "display") {
						if (data == 1) {
							return `<input type="radio" checked disabled>`;
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
				targets: 5,
				data: null,
				defaultContent: `<div class="btn-group" role="group" aria-label="Basic example">
									<button type="button" id="delete" class="btn btn-danger" data-toggle="tooltip" title="Xóa"><i class="fa fa-remove"></i></button>
									<button type="button" id="edit" class="btn btn-primary" data-toggle="tooltip" title="Chỉnh sửa"><i class="fa fa-edit"></i></button>
								</div>`
			}
		]
	});

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

	$("#btn_nha_cung_cap").on("click", function() {
		var elements = `<option>--Tỉnh--</option>`;
		var tinh = JSON.parse(sessionStorage.getItem("tinh"));
		tinh.map(function(item) {
			elements += `<option value="${item.provinceid}">${item.name}</option>`;
		});
		$("#new_nha_cung_cap #tinh").html(elements);
	});

	$("#new_nha_cung_cap #tinh").on("change", function() {
		var id_tinh = $(this).val();
		var huyen = JSON.parse(sessionStorage.getItem("huyen"));
		var elements = `<option>--Huyện--</option>`;
		huyen.map(function(item) {
			if (item.provinceid == id_tinh) {
				elements += `<option value="${item.districtid}">${item.name}</option>`;
			}
		});
		$("#new_nha_cung_cap #huyen").html(elements);
	});

	// Sửa nhà cung cấp
	$("#list_nha_cung_cap tbody").on("click", "#edit", function() {
		$(this)
			.attr("data-toggle", "modal")
			.attr("data-target", "#edit_nha_cung_cap");
		var data = table.row($(this).parents("tr")).data();
		$("#edit_nha_cung_cap #id").val(data["id"]);
		$("#edit_nha_cung_cap #ten_nha_cung_cap").val(data["ten_nha_cung_cap"]);
		$("#edit_nha_cung_cap #dia_chi").val(data["dia_chi"]);
		$("#edit_nha_cung_cap #mo_ta").val(data["mo_ta"]);
		$("#edit_nha_cung_cap #email").val(data["email"]);
		$("#edit_nha_cung_cap #sdt").val(data["so_dien_thoai"]);

		if (data["is_active"] == 1) {
			$("#is_active").prop("checked", true);
		}

		var tinh = JSON.parse(sessionStorage.getItem("tinh"));
		var huyen = JSON.parse(sessionStorage.getItem("huyen"));

		var elements_tinh = `<option>--Tỉnh--</option>`;
		tinh.map(function(item) {
			elements_tinh += `<option value="${item.provinceid}">${
				item.name
			}</option>`;
		});
		$("#edit_nha_cung_cap #tinh").html(elements_tinh);

		var elements_huyen = `<option>--Huyện--</option>`;
		huyen.map(function(item) {
			if (item.provinceid == data["tinh"]) {
				console.log(item.provinceid);
				elements_huyen += `<option value="${item.districtid}">${
					item.name
				}</option>`;
			}
		});
		$("#edit_nha_cung_cap #huyen").html(elements_huyen);

		$("#edit_nha_cung_cap #tinh").on("change", function() {
			var id_tinh = $(this).val();
			var huyen = JSON.parse(sessionStorage.getItem("huyen"));
			var elements = `<option>--Huyện--</option>`;
			huyen.map(function(item) {
				if (item.provinceid == id_tinh) {
					elements += `<option value="${item.districtid}">${
						item.name
					}</option>`;
				}
			});
			$("#edit_nha_cung_cap #huyen").html(elements);
		});

		$("#edit_nha_cung_cap #tinh").val(data["tinh"]);

		$("#edit_nha_cung_cap #huyen").val(data["huyen"]);
	});

	// Ajax add
	$("#new_nha_cung_cap #btn_create_nha_cung_cap").on("click", function() {
		var ten_nha_cung_cap = $("#new_nha_cung_cap #ten_nha_cung_cap").val();
		var dia_chi = $("#new_nha_cung_cap #dia_chi").val();
		var tinh = $("#new_nha_cung_cap #tinh").val();
		var huyen = $("#new_nha_cung_cap #huyen").val();
		var mo_ta = $("#new_nha_cung_cap #mo_ta").val();
		var email = $("#new_nha_cung_cap #email").val();
		var sdt = $("#new_nha_cung_cap #sdt").val();
		var id_ncc = $("#new_nha_cung_cap #id").val();

		$.ajax({
			type: "post",
			url: "/store/post-nha-cung-cap/",
			data: {
				ten_nha_cung_cap: ten_nha_cung_cap,
				dia_chi: dia_chi,
				tinh: tinh,
				huyen: huyen,
				mo_ta: mo_ta,
				email: email,
				sdt: sdt,
				id_ncc: id_ncc,
				is_add: 1,
				csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
			},
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
				table.ajax.reload();
				$("#new_nha_cung_cap").modal("hide");
				if (data.status == "success") {
					Swal.fire({
						type: "success",
						title: "Thành công",
						text: data.messages,
						timer: 1000
					});
				} else {
					Swal.fire({
						type: "error",
						title: "Lỗi",
						text: "Lỗi",
						timer: 1000
					});
				}
			}
		});
	});
	// Ajax edit
	$("#edit_nha_cung_cap #btn_edit_nha_cung_cap").on("click", function() {
		var ten_nha_cung_cap = $("#edit_nha_cung_cap #ten_nha_cung_cap").val();
		var dia_chi = $("#edit_nha_cung_cap #dia_chi").val();
		var tinh = $("#edit_nha_cung_cap #tinh").val();
		var huyen = $("#edit_nha_cung_cap #huyen").val();
		var mo_ta = $("#edit_nha_cung_cap #mo_ta").val();
		var email = $("#edit_nha_cung_cap #email").val();
		var sdt = $("#edit_nha_cung_cap #sdt").val();
		var id_ncc = $("#edit_nha_cung_cap #id").val();
		var is_active = 1;
		if ($("#is_active").is(":checked") == false) {
			is_active = 0;
		}

		$.ajax({
			type: "post",
			url: "/store/post-nha-cung-cap/",
			data: {
				ten_nha_cung_cap: ten_nha_cung_cap,
				dia_chi: dia_chi,
				tinh: tinh,
				huyen: huyen,
				mo_ta: mo_ta,
				email: email,
				sdt: sdt,
				id_ncc: id_ncc,
				is_active: is_active,
				is_edit: 1,
				csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
			},
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
				table.ajax.reload();
				$("#edit_nha_cung_cap").modal("hide");
				if (data.status == "success") {
					Swal.fire({
						type: "success",
						title: "Thành công",
						text: data.messages,
						timer: 1000
					});
				} else {
					Swal.fire({
						type: "error",
						title: "Lỗi",
						text: "Lỗi",
						timer: 1000
					});
				}
			}
		});
	});

	// Xóa nhà cung cấp
	$("#list_nha_cung_cap tbody").on("click", "#delete", function() {
		var data = table.row($(this).parents("tr")).data();
		var id_ncc = data["id"]
		Swal
			.fire({
				title: "Xóa nhà cung cấp này?",
				text: "Dữ liệu sẽ không thể phục hồi!",
				type: "warning",
				showCancelButton: true,
				confirmButtonColor: "#3085d6",
				cancelButtonColor: "#d33",
				cancelButtonText: "Hủy",
				confirmButtonText: "Xóa!"
			})
			.then(function(result) {
				if (result.value) {
					$.ajax({
						type: "post",
						url: "/store/post-nha-cung-cap/",
						data: {
							id_ncc: id_ncc,
							is_delete: 1,
							csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
						},
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
							table.ajax.reload();
							if (data.status == "success") {
								Swal.fire({
									type: "success",
									title: "Thành công",
									text: data.messages,
									timer: 1000
								});
							} else {
								Swal.fire({
									type: "error",
									title: "Lỗi",
									text: "Lỗi",
								});
							}
						}
					});
				}
			});
	});
});
