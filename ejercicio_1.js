//instalar: npm install prompt-sync
while (true) {
    const prompt = require('prompt-sync')({sigint:true})
    const numero = parseInt(prompt('Digite un numero: '))
    if(numero == 4) break
    if(numero == 0) console.log('El numero digitado es 0️⃣')
        else if(numero < '0') console.log('El numero digitado es Negativo ➖')
    else console.log('El numero digitado es Positivo ➕ ')
}


console.log(4 == '4')
console.log(4 === '4')
console.log(4 > 4)
