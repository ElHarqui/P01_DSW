//callback
/* setTimeout(function() {
    console.log("Hola Mundo")
},1000) */
const getUsuarioByID =( id, callback) => {
        const usuario = {
            id,
            nombre: "Fernando"
        }
        setTimeout(() => {
            callback(usuario)
        }, 1500)
    }
getUsuarioByID(10, (user) => {
    console.log(user.id);
    console.log(user.nombre.toUpperCase());
});

    //Los callback no es mas que funciones que se mandan como argumento a otra
    //función y se ejecutan en un lapso de tiempo.