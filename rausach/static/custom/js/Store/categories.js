$(document).ready(function() {
	// Load dữ liệu vào bảng
	var table = $("#list_loai_hang").DataTable({
		ajax: {
			type: "get",
			url: "/store/data-loai-hang/",
			dataSrc: ""
		},
		columns: [{ data: "no" }, { data: "ten_loai" }],
		columnDefs: [
			{
				targets: 2,
				data: null,
				defaultContent: `<center>
                                    <button class="btn btn-danger" id="delete"><i class="fa fa-remove"></i></button>
                                    <button class="btn btn-primary" id="edit" data-toggle="modal" data-target="#edit_loai_hang">
                                        <i class="fa fa-edit"></i>
                                    </button>
                                </center>`
			}
		]
	});

	// Thêm loại hàng
	$("#new_loai_hang #btn_create_loai_hang").on("click", function() {
		var ten_loai = $("#new_loai_hang #ten_loai_hang").val();
		if (ten_loai == "") {
			Swal.fire({
				type: "error",
				title: "Lỗi",
				text: "Tên loại không được để trống"
			});
		} else {
			$.ajax({
				type: "post",
				url: "/store/post-loai-hang/",
				data: {
					ten_loai: ten_loai,
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
					$("#new_loai_hang").modal("hide");
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
							text: "Thêm không thành công"
						});
					}
				}
			});
		}
	});
	// Sửa tên loại hàng
	$("#list_loai_hang tbody").on("click", "#edit", function() {
		var data = table.row($(this).parents("tr")).data();
		$("#edit_loai_hang #id").val(data["id"]);
		$("#edit_loai_hang #ten_loai_hang").val(data["ten_loai"]);
	});
	$("#btn_edit_loai_hang").on("click", function() {
		var id = $("#edit_loai_hang #id").val();
        var ten_loai = $("#edit_loai_hang #ten_loai_hang").val();
        console.log(id)
        console.log(ten_loai)
		$.ajax({
			type: "post",
			url: "/store/post-loai-hang/",
			data: {
				ten_loai: ten_loai,
				id_loai_hang: id,
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
				$("#edit_loai_hang").modal("hide");
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
						text: "Thêm không thành công"
					});
				}
			}
		});
    });
    
    // Xóa loại hàng
	$("#list_loai_hang tbody").on("click", "#delete", function() {
        var data = table.row($(this).parents("tr")).data();
        var id_loai_hang = data["id"];
        swal
			.fire({
				title: "Xóa loại hàng này?",
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
						url: "/store/post-loai-hang/",
						data: {
							id_loai_hang: id_loai_hang,
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
							}
                        },
					});
				}
			});
	});
});
