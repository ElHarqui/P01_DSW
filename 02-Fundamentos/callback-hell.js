// el infierno de los callback o llamar uno callback dentro de otro...
// definimos un arreflo de tres elementos:
const empleados = [
        {
            id: 1,
            nombre: "Fernando"
        },
        {
            id: 2,
            nombre: "Linda"
        },
        {
            id: 3,
            nombre: "Karen"
        }
    ];
    // creamos otro arreglo de salarios de solo dos elementos.
    const salarios = [
        {
            id: 1,
            salario: 1000
        },
        {
            id: 2,
            salario: 1500
        }
     ];
    // creamos la funcion de flecha que traiga la informacion de los emplados.
    
    // incluimos el llamado a funcion callback como argumento de la funcion
    //si el empleado existe se envia null y el objeto empleado
    const getEmpleado = (id, callback) => {
        const empleado = empleados.find(e => e.id === id)
        if (empleado ){
            callback(null,empleado.nombre);
        }
        else {
            callback(`El empleado con id ${id } no existe`) ;
        }
       
    }
    // funcion  salario
    const getSalario = (id, callback) => {
        const salario = salarios.find(s => s.id === id)?.salario
        if(salario) {
            callback(null, salario);
        }
        else {
            callback(`El Salario con Id ${id} no existe`);
        }
    }
    // si existe err dara error y si es null el empleado existe.
    const id = 10;
    getEmpleado(id, (err, empleado) => {
        if (err) {
            console.log("ERROR!!");
            return console.log(err);
        }
        getSalario(id, (err, salario) => {
            if(err) {
                return console.log(err);
            }
            console.log("El Empleado: ", empleado, "Tiene salario de: ", salario);
           
        } )
    })