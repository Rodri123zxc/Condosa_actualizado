$(document).ready(function () {
  $('#filtro-form').submit(function (event) {
      event.preventDefault();
      var selectedPredio = $('#filtro_predio').val();
      if (selectedPredio !== "") {
          $('#example').DataTable().column(6).search(selectedPredio).draw();
          $('#example').removeAttr('hidden');
      } else {
          $('#example').DataTable().column(6).search("").draw();
          $('#example').attr('hidden', true);
      }
  });
});

function mostrarComboBox(checkImage) {
  var trElement = $(checkImage).closest('tr');
  var estadoCelda = trElement.find('.estado-celda');
  var estadoActual = estadoCelda.text().trim();

  var selectHTML = '<select>' +
      '<option value="Habitada" ' + (estadoActual === 'Habitada' ? 'selected' : '') + '>Habitada</option>' +
      '<option value="No Habitada" ' + (estadoActual === 'No Habitada' ? 'selected' : '') + '>No Habitada</option>' +
      '<option value="Alquilada" ' + (estadoActual === 'Alquilada' ? 'selected' : '') + '>Alquilada</option>' +
      '<option value="Abandonada" ' + (estadoActual === 'Abandonada' ? 'selected' : '') + '>Abandonada</option>' +
      '</select>';

  estadoCelda.html(selectHTML);
  var selectElement = estadoCelda.find('select');

  selectElement.focus();
}

function guardarEstado(disqueteImage) {
  var trElement = $(disqueteImage).closest('tr');
  var casaId = trElement.find('td:nth-child(1)').text().trim();
  var nuevoEstado = trElement.find('.estado-celda select').val();

  trElement.find('.estado-celda').text(nuevoEstado);

  var requestData = {
      casaId: casaId,
      nuevoEstado: nuevoEstado
  };

  $.ajax({
      url: '/actualizar_estado',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(requestData),
      success: function(response) {
          alert(response.message);
      },
      error: function(error) {
          alert('Error al guardar el estado de la casa.');
      }
  });
}

$(document).on('click', '.disquete-icono img', function () {
  var disqueteImage = $(this);
  guardarEstado(disqueteImage);
});

function obtenerCasasSeleccionadas() {
  var casasSeleccionadas = [];
  $('.seleccionar-casa:checked').each(function() {
      casasSeleccionadas.push($(this).data('id'));
  });
  return casasSeleccionadas;
}

function limpiarSeleccionCasas() {
  $('.seleccionar-casa').prop('checked', false);
}

function limpiarNuevoEstado() {
  $('#nuevo-estado').val('');
}

function actualizarValoresTabla() {
  var filasTabla = $('#example').DataTable().rows().nodes();

  filasTabla.each(function(index, fila) {
      var estadoCelda = $(fila).find('.estado-celda');
      var nuevoEstado = estadoCelda.siblings('.estado-select').val();

      estadoCelda.text(nuevoEstado);
  });
}

function guardarEstadoMasivo() {
  var casasSeleccionadas = obtenerCasasSeleccionadas();
  var nuevoEstado = $('#nuevo-estado').val();

  if (casasSeleccionadas.length === 0 || nuevoEstado === '') {
    alert('Por favor, seleccione casas y elija un nuevo estado.');
    return;
  }

  var requestData = {
    casaIds: casasSeleccionadas,
    nuevoEstado: nuevoEstado
  };

  $.ajax({
    url: '/guardar_estado_masivo',
    method: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(requestData),
    success: function(response) {
        alert(response.message);
        limpiarSeleccionCasas();
        limpiarNuevoEstado();
        
        // Llamar a la función para actualizar los valores en la tabla
        actualizarValoresTabla();
    },
    error: function(xhr, status, error) {
        alert('Error al guardar los estados de las casas.');
    }
  });
}

$('#modificacion-masiva').on('click', function() {
  guardarEstadoMasivo();
});

$(document).ready(function() {
    // Inicializar la tabla
    var table = $('#example').DataTable();

    // Enumerar las filas
    table.on('order.dt search.dt', function() {
        table.column(0, { search: 'applied', order: 'applied' }).nodes().each(function(cell, i) {
            cell.innerHTML = i + 1;
        });
    }).draw();
});