function listadoServicios(){
    $.ajax({
        url:"/Servicios/listar_servicio/",
        type:"get",
        dataType:"json",
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    listadoServicios();
});