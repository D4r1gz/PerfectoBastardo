function contrasenna() {


  var contra1 = document.getElementById("contrasena").value;
  var contra2 = document.getElementById("peace").value;

  if (contra1 == "", contra2 == "") {
    document.getElementById("errorcontrasena").innerHTML = "Debe escribir una contraseña";
    document.getElementById("contrasena").style.borderColor = "#dc143c";
    document.getElementById("peace").style.borderColor = "#dc143c";
  } else {

  }
  if (contra1 != contra2) {
    document.getElementById("errorcontrasena").innerHTML = "Las contraseñas no son iguales";
    document.getElementById("contrasena").style.borderColor = "#dc143c";
    document.getElementById("peace").style.borderColor = "#dc143c";
  }


}


function email() {
  var email = document.getElementById("emaail").value;
  var a = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;

  if (email.length == 0) {
    document.getElementById("erroremail").innerHTML = "Debe escribir un email";
    document.getElementById("emaail").style.borderColor = "#dc143c";
  } else {

  }
  if (!a.exec(email)) {
    document.getElementById("erroremail").innerHTML = "El email no es válido";
    document.getElementById("emaail").style.borderColor = "#dc143c";
  }

}

function nombrefr() {
  var nombre = document.getElementById("nombrefr").value;
  var apellido = document.getElementById("apellidofr").value;
  if (nombre.length == 0 && apellido.length == 0) {
    document.getElementById("errornombre").innerHTML = "Debe escribir un nombre";
    document.getElementById("errorapellido").innerHTML = "Debe escribir al menos un apellido ";
    document.getElementById("nombrefr").style.borderColor = "#dc143c";
    document.getElementById("apellidofr").style.borderColor = "#dc143c";
  }
}

function telefono() {
  var telefono = document.getElementById("telefono").value;
  if (telefono.length == 0) {
    document.getElementById("errortelefono").innerHTML = "Debe escribir un teléfono";
    document.getElementById("telefono").style.borderColor = "#dc143c";
  }
}

function contacto() {
  var nombrec = document.getElementById("nombrec").value;
  var emailc = document.getElementById("emailc").value;
  var mensajec = document.getElementById("mensajec").value;
  var a = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;

  if (nombrec.length == 0) {
    document.getElementById("errornomc").innerHTML = "Debe escribir un nombre";
  }

  if (emailc.length == 0) {
    document.getElementById("erroremc").innerHTML = "Debe escribir un correo";
  } else {

  }
  if (!a.exec(emailc)) {
    document.getElementById("erroremc").innerHTML = "El email no es válido";
  }

  if (mensajec.length == 0) {
    document.getElementById("errormensc").innerHTML = "Debe escribir un mensaje";
  }

}



//jquery
$(document).ready(function () {
  $("#is").click(function () {
    var nombreis = $("#nombreis").val();
    var nombrefr = $("nombrefr").val();
    if (nombreis == "") {
      $("#errornombreis").html("Ingrese un nombre");
      $("#nombreis").css({
        'borderColor': '#dc143c'
      });

    } else if (nombreis != nombrefr) {
      $("#errornombreis").html("El nombre no es Válido");
      $("#nombreis").css({
        'borderColor': '#dc143c'
      });
    }

  });

  $("#is").click(function () {
    var contrais = $("#contra3").val();
    var contrafr = $("#peace").val();

    if (contrais == "") {
      $("#errorcontrasenais").html("Escribe una contraseña");
      $("#contra3").css({
        'borderColor': '#dc143c'
      });
    } else if (contrais != contrafr) {
      $("#errorcontrasenais").html("La contraseña no es coreccta");
      $("#contra3").css({
        'borderColor': '#dc143c'
      });
    }
  });

  $(function(){
    $.getJSON("https://jsonplaceholder.typicode.com/posts/1/comments",function(data){
    
      var data= data;
      $.each(data,function(i,item){
        $("#comentarios").append(
            "<tr><td>" + item.id + "</td> <td>" + item.name+"</td> <td>" + item.email +"</td> <td>"+item.body+ "</td></tr>"
        );
    });
    

    });
  });
  

});

//
function todos() {
  contrasenna();
  email();
  nombrefr();
  telefono();
}