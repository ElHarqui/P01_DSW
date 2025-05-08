const argv = require('yargs')
     .option('b', {
      alias: 'base',
      type: 'number',
      demandOption: true,
      describe: 'Es la base de la tabla de multiplicar'

      }) 
      .check((argv, options ) => {
      if(isNaN(argv.b)){
        throw 'La base debe ser un Numero'
        }
          return true;
      }) 
      .option('l', {
         alias: 'listar',
         type: 'boolean',
         default: false,
         describe: 'Muestra la tabla en consola'

        })
      .option('h', {
         alias: 'hasta',
         type: 'number',
         default: 10,
         describe: 'Hasta que numero se multiplicara'
        })
      .check((argv, options ) => {
         if(isNaN(argv.h)){
           throw 'El valor de hasta debe ser un Numero'
          }
            return true;
        })         
    .argv;
module.exports = argv;
