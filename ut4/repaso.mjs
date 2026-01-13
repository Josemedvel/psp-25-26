import os from "os"
import path from "path"
import {readFileSync, readFile} from "fs"

console.log(os.hostname())

let variable = 45
const constante = "hola"

console.log(constante)


// + - * / ** 
console.log(3/2)

// if, else if, else

let arr = [1,2,3,4,5,6,7,8,9]
/*
for(let i = 0; i < arr.length; i++){
    console.log(arr[i])
}
*/

function imprimir(elemento){
    console.log(elemento)
}

//arr.forEach(imprimir)
//arr.forEach(e => console.log(e))


const datos = {
    "nombre": "Julian",
    "edad" : 40,
    "telefono" : "645378924" 
}
console.error("Ha habido un error")
//console.log(datos)
console.table(datos)


const f = (e) => {
    console.log("hola")
    console.log("adios")
}

f()

//map

const arr2 = arr.map(e => e + 2)
console.log(arr2)
console.log(arr)

const suma = arr.reduce((p,e) => e + p, 0)
console.log(suma)

const pares = arr.filter(e => e % 2 == 0)
console.log(pares)


pares.push(10)
console.log(pares)
pares.splice(2, 1)//, "hola")
console.log(pares)

const rutaActual = path.resolve(".")
const rutaFichero = path.join(rutaActual, "log_errors.txt")
const rutaFichero2 = path.join(rutaActual, "repaso.mjs")
const contenido = readFileSync(rutaFichero, "utf8")
console.log(contenido)

readFile(rutaFichero2, "utf8", (data, err) => {
    if(data){
        console.log(data)
    }
    if(err){
        console.error(err)
    }
})