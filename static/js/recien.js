function buscarPersona() {
    var dni = $("#dni-input").val();

    $.ajax({
      url: "/buscar_persona",
      method: "POST",
      data: { dni: dni },
      success: function(response) {
        if (response.encontrada) {
          mostrarDatosPersona(response);
          ocultarMensajeNoEncontrado();
        } else {
          mostrarMensajeNoEncontrado();
        }
      },
      error: function() {
        mostrarMensajeError();
      }
    });
  }

  function ocultarMensajeNoEncontrado() {
    $("#mensaje").text("");
  }
  function mostrarMensajeNoEncontrado() {
    $("#mensaje").text("Persona no encontrada.");
    resetearDatosPersona();
    $("#mensaje").css({
      "font-size": "24px",
      "color": "red"
    });
  }

  function mostrarMensajeError() {
    $("#mensaje").text("Error al buscar la persona.");
    resetearDatosPersona();
    $("#mensaje").css({
      "font-size": "24px",
      "color": "red"
    });
  }

  function mostrarDatosPersona(datos) {
    $("#nombres").text(datos.nombres);
    $("#apellido_paterno").text(datos.apellido_paterno);
    $("#apellido_materno").text(datos.apellido_materno);
    $("#edad").text(datos.edad);
    $("#fecha-nacimiento").text(datos.fecha_nacimiento);
    $("#direccion").text(datos.direccion);
    $("#departamento").text(datos.departamento);
    $("#provincia").text(datos.provincia);
    $("#distrito").text(datos.distrito);
    $("#telefono").text(datos.telefono);
    $("#correo").text(datos.correo);
  }



  function resetearDatosPersona() {
    $("#nombres").text("");
    $("#apellido_paterno").text("");
    $("#apellido_materno").text("");
    $("#edad").text("");
    $("#fecha-nacimiento").text("");
    $("#direccion").text("");
    $("#departamento").text("");
    $("#provincia").text("");
    $("#distrito").text("");
    $("#telefono").text("");
    $("#correo").text("");
  }