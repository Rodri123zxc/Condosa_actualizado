function buscarPersona() {
    var dni = $("#dni-input").val();

    $.ajax({
      url: "/buscar_persona",
      method: "POST",
      data: { dni: dni },
      success: function(response) {
        if (response.encontrada) {
          mostrarDatosPersona(response);
        } else {
          mostrarMensajeNoEncontrado();
        }
      },
      error: function() {
        mostrarMensajeError();
      }
    });
  }

  function mostrarDatosPersona(datos) {
    $("#edad").text(datos.edad);
    $("#fecha-nacimiento").text(datos.fecha_nacimiento);
    $("#direccion").text(datos.direccion);
    $("#departamento").text(datos.departamento);
    $("#provincia").text(datos.provincia);
    $("#distrito").text(datos.distrito);
    $("#telefono").text(datos.telefono);
    $("#correo").text(datos.correo);
  }

  function mostrarMensajeNoEncontrado() {
    $("#mensaje").text("Persona no encontrada.");
    resetearDatosPersona();
  }

  function mostrarMensajeError() {
    $("#mensaje").text("Error al buscar la persona.");
    resetearDatosPersona();
  }

  function resetearDatosPersona() {
    $("#edad").text("");
    $("#fecha-nacimiento").text("");
    $("#direccion").text("");
    $("#departamento").text("");
    $("#provincia").text("");
    $("#distrito").text("");
    $("#telefono").text("");
    $("#correo").text("");
  }