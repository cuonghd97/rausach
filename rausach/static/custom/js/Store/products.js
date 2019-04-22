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

	// Load sản phẩm
	var table = $("#list_san_pham").DataTable({
		destroy: true,
		ajax: {
			type: "get",
			url: "/store/data-san-pham/",
			dataSrc: ""
		},
		columns: [
			{ data: "no" },
			{ data: "ten_san_pham" },
			{ data: "gia_ban" },
			{ data: "loai_hang" },
			{ data: "ton_kho" },
			{ data: "nha_cung_cap" },
			{
				data: "is_active",
				render: function(data, type, row) {
					if (type == "display") {
						if (data == "1") {
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
				targets: 7,
				data: null,
				defaultContent: `<button class="btn btn-primary" id="edit" data-toggle="modal" data-target="#edit_san_pham"><i class="fa fa-edit"></i></button>
				<button class="btn btn-danger" id="delete"><i class="fa fa-times"></i></button>
				`
			}
		]
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
		var image_avt = $("#new_san_pham #image_avt")[0].files[0];
		var image = $("#new_san_pham #image")[0].files;

		if (image.length > 5) {
			Swal.fire({
				type: "error",
				title: "Lỗi",
				text: "Không được thêm quá 5 ảnh chi tiết sản phẩm"
			});
		} else if (
			ten_san_pham == "" ||
			gia_ban == "" ||
			gia_von == "" ||
			so_luong == "" ||
			loai_hang == "" ||
			nha_cung_cap == "" ||
			mo_ta == "" ||
			image_avt.length == "" ||
			image == ""
		) {
			Swal.fire({
				type: "error",
				title: "Lỗi",
				text: "Không được để trống các trường"
			});
		} else {
			data = [];
			for (let i = 0; i < image.length; i++) {
				formData.append("anh", image[i]);
			}
			formData.append("image_avt", image_avt);
			formData.append("ten_san_pham", ten_san_pham);
			formData.append("gia_von", gia_von);
			formData.append("gia_ban", gia_ban);
			formData.append("so_luong", so_luong);
			formData.append("loai_hang", loai_hang);
			formData.append("nha_cung_cap", nha_cung_cap);
			formData.append("mo_ta", mo_ta);
			formData.append("is_add", 1);
			formData.append(
				"csrfmiddlewaretoken",
				$("input[name=csrfmiddlewaretoken]").val()
			);
			$.ajax({
				contentType: false,
				processData: false,
				type: "post",
				url: "/store/post-san-pham/",
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
				success: function() {
					$("#new_san_pham").modal("hide")
					Swal.fire({
						type: "success",
						title: "Thành công",
						text: "Thêm thành công"
					});
					table.ajax.reload();
				}
			});
		}
	});

	// Xem chi tiết sản phẩm
	$("#list_san_pham tbody").on("click", "#edit", function() {
		nha_cung_cap = JSON.parse(sessionStorage.getItem("nha_cung_cap"));
		var ncc = `<option>--Nhà cung cấp--</option>`;
		nha_cung_cap.map(function(item) {
			ncc += `<option value="${item.id}">${item.ten_nha_cung_cap}</option>`;
		});
		$("#edit_san_pham #nha_cung_cap").html(ncc);

		loai_hang = JSON.parse(sessionStorage.getItem("loai_hang"));
		hang = `<option>--Loại hàng--</option>`;
		loai_hang.map(function(item) {
			hang += `<option value="${item.id}">${item.ten_loai}</option>`;
		});
		$("#edit_san_pham #loai_hang").html(hang);

		var data = table.row($(this).parents("tr")).data();

		$("#edit_san_pham #ten_san_pham").val(data.ten_san_pham);
		$("#edit_san_pham #id").val(data.id);
		$("#edit_san_pham #gia_von").val(data.gia_von);
		$("#edit_san_pham #gia_ban").val(data.gia_ban);
		$("#edit_san_pham #khuyen_mai").val(data.khuyen_mai);
		$("#edit_san_pham #so_luong").val(data.so_luong);
		if (data.is_active == "1") {
			$("#edit_san_pham #is_active").prop("checked", true);
		}
		$("#edit_san_pham #loai_hang").val(data.id_loai_hang);
		$("#edit_san_pham #nha_cung_cap").val(data.id_nha_cung_cap);
		$("#edit_san_pham #mo_ta").val(data.mo_ta);
		// $("#edit_san_pham img").attr("src", "/media/" + data.anh)
		var anh = `<div class="col-md-6">
			<img
				style="width: 100%; display: block; height: 187px;"
				src="/media/${data.anh}"
				alt="image"
			/>
			<div class="caption">
				<p>Ảnh đại diện sản phẩm</p>
			</div>
		</div>`;
		$.ajax({
			type: "get",
			url: "/store/data-anh-san-pham/" + data.id,
			success: function(data) {
				data.map(function(item) {
					anh += `<div class="col-md-6">
						<img
							style="width: 100%; display: block; height: 187px;"
							src="/media/${item.hinh_anh}"
							alt="image"
						/>
						<div class="caption">
							<p>Ảnh chi tiết sản phẩm</p>
						</div>
					</div>`;
				});
			},
			complete: function() {
				$("#edit_san_pham #img-sp").html(anh);
			}
		});
	});
	// Lưu thông tin chỉnh sửa
	$("#edit_san_pham #btn_edit_product").on("click", function() {
		var formData = new FormData();

		var ten_san_pham = $("#edit_san_pham #ten_san_pham").val();
		var gia_von = $("#edit_san_pham #gia_von").val();
		var gia_ban = $("#edit_san_pham #gia_ban").val();
		var so_luong = $("#edit_san_pham #so_luong").val();
		var loai_hang = $("#edit_san_pham #loai_hang").val();
		var nha_cung_cap = $("#edit_san_pham #nha_cung_cap").val();
		var mo_ta = $("#edit_san_pham #mo_ta").val();
		var image_avt = $("#edit_san_pham #image_avt")[0].files[0];
		var image = $("#edit_san_pham #image")[0].files;
		var id = $("#edit_san_pham #id").val();
		var khuyen_mai = $("#edit_san_pham #khuyen_mai").val();
		var is_active = 0;
		if ($('#edit_san_pham #is_active').is(":checked") == true) {
			is_active = 1;
		}
		if (image.length > 5) {
			Swal.fire({
				type: "error",
				title: "Lỗi",
				text: "Không được thêm quá 5 ảnh chi tiết sản phẩm"
			});
		} else if (
			ten_san_pham == "" ||
			gia_ban == "" ||
			gia_von == "" ||
			so_luong == "" ||
			loai_hang == "" ||
			nha_cung_cap == "" ||
			mo_ta == ""
		) {
			Swal.fire({
				type: "error",
				title: "Lỗi",
				text: "Không được để trống các trường"
			});
		} else {
			data = [];
			for (let i = 0; i < image.length; i++) {
				formData.append("anh", image[i]);
			}

			formData.append("image_avt", image_avt);
			formData.append("ten_san_pham", ten_san_pham);
			formData.append("gia_von", gia_von);
			formData.append("gia_ban", gia_ban);
			formData.append("so_luong", so_luong);
			formData.append("loai_hang", loai_hang);
			formData.append("nha_cung_cap", nha_cung_cap);
			formData.append("mo_ta", mo_ta);
			formData.append("is_active", is_active);
			formData.append("is_edit", 1);
			formData.append("id", id);
			formData.append("khuyen_mai", khuyen_mai);
			formData.append(
				"csrfmiddlewaretoken",
				$("input[name=csrfmiddlewaretoken]").val()
			);
			$.ajax({
				contentType: false,
				processData: false,
				type: "post",
				url: "/store/post-san-pham/",
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
				success: function() {
					$("#edit_san_pham").modal("hide")
					table.ajax.reload();
					Swal.fire({
						type: "success",
						title: "Thành công",
						text: "Sửa thành công"
					});
				}
			});
		}
	});

	// Xóa sản phẩm
	$("#list_san_pham tbody").on("click", "#delete", function() {
		var formData = new FormData();
		var data = table.row($(this).parents("tr")).data();
		Swal.fire({
			title: "Xóa giáo sản phẩm này?",
			text: "Dữ liệu sẽ không thể phục hồi!",
			type: "warning",
			showCancelButton: true,
			confirmButtonColor: "#3085d6",
			cancelButtonColor: "#d33",
			cancelButtonText: "Hủy",
			confirmButtonText: "Xóa!"
		}).then(function(result) {
			if (result.value) {
				formData.append("id", data.id);
				formData.append("is_delete", 1);
				formData.append(
					"csrfmiddlewaretoken",
					$("input[name=csrfmiddlewaretoken]").val()
				);
				$.ajax({
					contentType: false,
					processData: false,
					type: "post",
					url: "/store/post-san-pham/",
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
					success: function() {
						table.ajax.reload();
						Swal.fire({
							type: "success",
							title: "Thành công",
							text: "Xóa thành công",
							timer: 1000
						});
					}
				});
			}
		});
	});
});
