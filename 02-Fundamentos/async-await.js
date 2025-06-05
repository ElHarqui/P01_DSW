//promesas
const empleados = [
    {
        id: 1,
        nombre: 'Fernando'
    },
    {
        id: 2,
        nombre: 'Linda'
    },
    {
        id: 3,
        nombre: 'Karen'
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
//getEmpleado transformado en promesa, ya no es necesario el callback.
// se define la promesa con dosr argumentos resolve si no hay error, reject si hay error
//se busca el empleado retorna el nombre si existe llamo al empleado, caso contrario el error
const getEmpleado = (id) => {
    return new Promise((resolve, reject) => {
        const empleado = empleados.find(e => e.id === id)?.nombre;
        (empleado)
            ? resolve(empleado)
            :reject (`No existe Empleado con Id ${id}`);
        
    });
        
}
// funcion getSalario
const getSalario = (id) => {
    return new  Promise((resolve, reject) => {
        const salario= salarios.find(s => s.id === id)?.salario;
        (salario)
           ? resolve(salario)
           :reject (`No existe Salario Id ${id}`);
        
    });
        
}

//const id=1;


//funcion asincroma
const getInfoUsuario = async(id) => {
    try {
        const empleado = await getEmpleado(id);
        const salario = await getSalario(id );
        return `El salario del emplado: ${empleado} es de ${salario}`;
        
    } catch (error) {
        return error; 
    }
    
}

const id=3;
getInfoUsuario(id )
    .then(msg => console.log(msg))
    .catch( err => console.log(err));
