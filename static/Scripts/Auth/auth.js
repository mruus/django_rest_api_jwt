console.log(BASE_URL);

$("#registerForm").on("submit", function (e) {
  e.preventDefault();

  let formData = new FormData();

  let name = $("#name").val();
  let email = $("#email").val();
  let password = $("#password").val();

  formData.append("name", name);
  formData.append("email", email);
  formData.append("password", password);

  $.ajax({
    method: "POST",
    url: BASE_URL + "API/AuthRegister",
    processData: false,
    contentType: false,
    data: formData,
    async: false,
    success: function (response) {
      console.log(response);
    },
    error: function (response) {
      console.log(response.responseJSON.Data);
      $(".message").text(response.responseJSON.Data);
    },
  });
});

$("#loginForm").on("submit", function (e) {
  e.preventDefault();

  let formData = new FormData();

  let email = $("#email").val();
  let password = $("#password").val();

  formData.append("email", email);
  formData.append("password", password);

  $.ajax({
    method: "POST",
    url: BASE_URL + "API/AuthLogin",
    processData: false,
    contentType: false,
    data: formData,
    async: false,
    success: function (response) {
      console.log(response);
      if (!response.Data.Error) {
        document.cookie = "TokenKey= " + response.Token;
      }
    },
    error: function (response) {
      console.log(response.responseJSON.Data);
      $(".message").text(response.responseJSON.Data);
    },
  });
});

$("#logout").on("submit", function (e) {
  e.preventDefault();
  document.cookie = "TokenKey=''";
});
