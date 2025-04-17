console.log("Inicio del Programa"); // 1
setTimeout( () => {
    console.log("Primer timeOut"); // 5
}, 3000);
setTimeout( () => {
    console.log("Segundo timeOut"); // 2

}, 3000);
setTimeout( () => {
    console.log("Tercer timeOut"); // 3
}, 3000);
console.log("Fin del Programa"); // 4