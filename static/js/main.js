function filtrar() {
    // Obtener el valor seleccionado del filtro
    var filtro = document.getElementById('filtro').value;

    // Hacer una petición al servidor para obtener los datos filtrados (usando AJAX o Fetch)

    // Una vez que se obtengan los datos del servidor, generar las filas de la tabla con JavaScript
    var tabla = document.getElementById('tabla').getElementsByTagName('tbody')[0];
    tabla.innerHTML = ''; // Limpiar la tabla antes de agregar las nuevas filas

    // Ejemplo de datos estáticos para llenar la tabla
    var datos = []; // Aquí debes agregar los datos obtenidos del servidor

    for (var i = 0; i < datos.length; i++) {
        var fila = tabla.insertRow();

        var numeroCasaCell = fila.insertCell();
        numeroCasaCell.textContent = datos[i].numeroCasa;

        var pisoCell = fila.insertCell();
        pisoCell.textContent = datos[i].piso;

        var areaCell = fila.insertCell();
        areaCell.textContent = datos[i].area;

        var descripcionPredioCell = fila.insertCell();
        descripcionPredioCell.textContent = datos[i].descripcionPredio;

        var tipoPredioCell = fila.insertCell();
        tipoPredioCell.textContent = datos[i].tipoPredio;

        var direccionPredioCell = fila.insertCell();
        direccionPredioCell.textContent = datos[i].direccionPredio;

        var nombrePropietarioCell = fila.insertCell();
        nombrePropietarioCell.textContent = datos[i].nombrePropietario;

        var estadoCasaCell = fila.insertCell();
        estadoCasaCell.textContent = datos[i].estadoCasa;
    }
}
