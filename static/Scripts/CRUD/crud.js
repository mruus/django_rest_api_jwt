GetAllAccounts();

let insertionType = "Insert";

$("#crudForm").on("submit", function (e) {
  e.preventDefault();

  let methodType, URL_Link;

  let formData = new FormData();

  formData.append("Name", $("#Name").val());
  formData.append("Email", $("#Email").val());
  formData.append("Phone", $("#Phone").val());
  formData.append("Username", $("#Username").val());
  formData.append("Password", $("#Password").val());

  if (insertionType == "Insert") {
    methodType = "POST";
    URL_Link = BASE_URL + "API/CRUD/crud_noid";
  } else {
    const ID = $("#ID").val();
    methodType = "PUT";
    URL_Link = BASE_URL + `API/CRUD/crud_id/` + ID + ``;
  }

  $.ajax({
    method: methodType,
    url: URL_Link,
    processData: false,
    contentType: false,
    data: formData,
    async: false,
    success: function (data) {
      if (!data.isError) {
        rows = data.Message;
        GetAllAccounts();
        insertionType = "Insert";
        $("#crudForm").trigger("reset");
      }
    },
    error: function (error) {
      console.log(error);
    },
  });
});

$("#accountsTable tbody").on("click", ".delete", function () {
  const ID = $(this).attr("delete");

  if (confirm("Are you sure you want to delete")) {
    $.ajax({
      method: "DELETE",
      url: BASE_URL + `API/CRUD/crud_id/` + ID + ``,
      async: false,
      success: function (data) {
        if (!data.isError) {
          GetAllAccounts();
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  }
});

$("#accountsTable tbody").on("click", ".edit", function () {
  const ID = $(this).attr("edit");

  $.ajax({
    method: "GET",
    url: BASE_URL + `API/CRUD/crud_id/` + ID + ``,
    async: false,
    success: function (data) {
      if (!data.isError) {
        $("#Name").val(data.Message.Name);
        $("#Email").val(data.Message.Email);
        $("#Phone").val(data.Message.Phone);
        $("#Username").val(data.Message.Username);
        $("#Password").val(data.Message.Password);
        $("#ID").val(data.Message.id);

        insertionType = "Update";
      }
    },
    error: function (error) {
      console.log(error);
    },
  });
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
  }

  $("#accountsTable tbody").html(rData);
}
