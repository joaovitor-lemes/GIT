function ehPrimo(n: number): boolean {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function primeirosPrimos(quantidade: number): number[] {
    const primos: number[] = [];
    let num = 2;

    while (primos.length < quantidade) {
        if (ehPrimo(num)) {
            primos.push(num);
        }
        num++;
    }

    return primos;
}

// Exemplo de uso:
const primos = primeirosPrimos(25);
console.log("Os 25 primeiros números primos são:");
console.log(primos);
