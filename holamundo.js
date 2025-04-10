const os = require('node:os');
console.log('Hola Mundo desde Node.js!');
console.log('Sistema Operativo: ' + os.platform());
console.log('Version de SO: ' + os.release());
console.log('Memoria total: ' + os.totalmem() / 1024 / 1024 + ' MB');

console.log('Versión de Node.js: ' + process.version);
console.log('Directorio de trabajo: ' + process.cwd());
console.log('ID del proceso: ' + process.pid);
