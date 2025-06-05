const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, 'tokens.env') });

const { leerInput, inquirerMenu, pausa, listarLugares } = require("./helpers/inquirer");
const Busquedas = require("./models/busquedas");
console.log(process.env);
//console.clear();
const main = async() => {
    const busquedas = new Busquedas();
    let opt = 0;
    do {
        // llamada a la funcion que pinta el menu
        opt = await inquirerMenu();
        switch(opt) {
            case 1:
                //mostrar mensaje
                const lugar = await leerInput('Ciudad: ');
                //buscar los lugares
                const lugares = await busquedas.ciudad(lugar);
                //seleccionar el lugar
                const id = await listarLugares(lugares);
                if(id === '0') continue; // cancela
                const lugarSel = lugares.find(l => l.id === id);
                //guardar en arraglo
                busquedas.agregarHistorial(lugarSel.nombre);
                //clima
                const clima = await busquedas.climaLugar(lugarSel.lat, lugarSel.lng);

                if (!clima) {
                    console.log('No se pudo obtener el clima para este lugar.');
                    break;
                }

                //mostrar los resultados
                console.clear();
                console.log('\nInformacion de la Ciudad\n'.green);
                console.log('Ciudad: ', lugarSel.nombre.green);
                console.log('Lat: ', lugarSel.lat);
                console.log('Lng: ', lugarSel.lng);
                console.log('Temperatura: ', clima.temp);
                console.log('Maxima: ', clima.max);
                console.log('Minima: ', clima.min);
                console.log('Estado del clima: ', clima.desc.green);
                break;
            case 2:
                // aqui en vez de busqueda.historial poner busqueda.historialCapitalizado
                busquedas.historialCapitalizado.forEach((lugar,i) => {
                    const idx = `${i+1}`.green;
                    console.log(`${idx} ${lugar}`);

                })
                break;


            case 0:
                break;

        }
        await pausa();

    } while(opt !== 0);

   
}
main();
