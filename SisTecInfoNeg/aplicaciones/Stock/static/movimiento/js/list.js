$(function () {
  midatatable2 = $('#data').DataTable({
    "lengthMenu": [
      [5, 25, 50, -1],
      [5, 25, 50, "Todos"]
    ],
    dom: '',
    columnDefs: [
      { 'sortable': true, 'searchable': false, 'visible': false, 'type': 'num', 'targets': [0] }
    ],
    order: [
      [0, "desc"]
    ],
    language: {
      sProcessing: "Procesando...",
      sLengthMenu: "Mostrar _MENU_ registros",
      sZeroRecords: "No se encontraron resultados",
      sEmptyTable: "Ningún dato disponible en esta tabla",
      sInfo: "Mostrando _START_ al _END_ de un total de _TOTAL_ registros",
      sInfoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
      sInfoFiltered: "(filtrado de un total de _MAX_ registros)",
      sInfoPostFix: "",
      sSearch: "Buscar:",
      sUrl: "",
      sInfoThousands: ",",
      sLoadingRecords: "Cargando...",
      oPaginate: {
        sFirst: "Primero",
        sLast: "Último",
        sNext: "Siguiente",
        sPrevious: "Anterior"
      },
      oAria: {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
      },
      buttons: {
        "copy": "Copiar",
        "colvis": "Visibilidad"
      }
    },
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        'action': 'searchdata'
      },
      dataSrc: ""
    },
    columns: [
      //{"data": "id"},
      { "data": "tipoMovimiento" },  //atributos del modelo
      { "data": "tipoComprobante" },
      { "data": "numeroComprobante" },
      { "data": "lugar" },
      { "data": "fechaMovimiento" },
      { "data": "observaciones" },
      { "data": "articulo" },
      { "data": "total" },
      
    ],
    initComplete: function (settings, json) {

    }
  });
});