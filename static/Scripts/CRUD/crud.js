GetAllAccounts();

$("#crudForm").on("submit", function (e) {
  e.preventDefault();

  let formData = new FormData();

  formData.append("Name", $("#FirstName").val() + " " + $("#LastName").val());
  formData.append("Email", $("#Email").val());
  formData.append("Phone", $("#Phone").val());
  formData.append("Username", $("#Username").val());
  formData.append("Password", $("#Password").val());

  $.ajax({
    method: "POST",
    url: BASE_URL + "API/CRUD/crud_noid",
    processData: false,
    contentType: false,
    data: formData,
    async: false,
    success: function (data) {
      if (!data.isError) {
        rows = data.Message;
      }

      GetAllAccounts();
    },
    error: function (error) {
      console.log(error);
    },
  });
});

$("#accountsTable").on("click", "tbody .delete", function () {
  const ID = $(this).attr("delete");
  alert("Delete Account" , ID);
});

function GetAllAccounts() {
  let rows;
  $.ajax({
    method: "GET",
    url: BASE_URL + "API/CRUD/crud_noid",
    async: false,
    success: function (data) {
      if (!data.isError) {
        rows = data.Message;
      }
    },
    error: function (error) {
      console.log(error);
    },
  });
  let rData = "";
  if (rows.length > 0) {
    for (var i = 0; i < rows.length; i++) {
      rData +=
        `
        <tr>
        <td>` +
        rows[i].Name +
        `</td>
        <td>` +
        rows[i].Email +
        `</td>
        <td>` +
        rows[i].Phone +
        `</td>
        <td>` +
        rows[i].Username +
        `</td>
        <td>` +
        rows[i].Password +
        `</td>
        <td>
            <button class="btn btn-danger delete" delete = ` +
        rows[i].id +
        `><i class="fas fa-trash-alt"></i></button>
            <button class="btn btn-success edit" edit = ` +
        rows[i].id +
        `><i class="fa fa-pencil"></i></button>
        </td>
    </tr>
        `;
    }

    $("#accountsTable tbody").html(rData);
  }
}
