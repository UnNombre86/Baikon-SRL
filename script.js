$(document).ready(function () {
  var O2Hb = $("#O2HB").text();
  $("#Menu").on("click", abrirNav);
  $("#Close").on("click", cerrarNav);
  $("section").on("click", cerrarNav);

  if (O2Hb <= 95) {
    $("#oxim").addClass("danger");
  } else {
    $("#xim").removeClass("danger");
  }
});

function abrirNav() {
  $("#Menu").addClass("active");
  $("#Close").addClass("active");
  $("nav").addClass("active");
  $("section").addClass("active");
}

function cerrarNav() {
  $("#Menu").removeClass("active");
  $("#Close").removeClass("active");
  $("nav").removeClass("active");
  $("section").removeClass("active");
}
