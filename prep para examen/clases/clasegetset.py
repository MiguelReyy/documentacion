class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    # Getter para obtener el titular de la cuenta
    def get_titular(self):
        return self._titular

    # Setter para modificar el titular de la cuenta
    def set_titular(self, nuevo_titular):
        self._titular = nuevo_titular

    # Getter para obtener el saldo de la cuenta
    def get_saldo(self):
        return self._saldo

    # Setter para modificar el saldo de la cuenta
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("El saldo no puede ser negativo.")
        else:

            self._saldo = self._saldo + nuevo_saldo

            print(f"{self._saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Saldo actual: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

   

# Ejemplo de uso
cuenta = CuentaBancaria("Juan", 1000)
print(f"Titular de la cuenta: {cuenta.get_titular()}")
print(f"Saldo de la cuenta: {cuenta.get_saldo()}")

cuenta.set_titular("María")
print(f"Nuevo titular de la cuenta: {cuenta.get_titular()}")

cuenta.depositar(500)

cuenta.set_saldo(500)
