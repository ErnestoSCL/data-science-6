import os

def convertir_moneda(tipo_conversion, cantidad):
    tipo_cambio = 3 
    if tipo_conversion == "soles_a_dolares":
        return cantidad / tipo_cambio
    elif tipo_conversion == "dolares_a_soles":
        return cantidad * tipo_cambio
    else:
        raise ValueError("Tipo de conversión no válido")

def main():
    while True:
        os.system('cls')
        print("================ CONVERSOR DE MONEDAS ============")
        print("========= OPCIONES ========")
        print("1. Convertir Soles a Dólares")
        print("2. Convertir Dólares a Soles")
        print("3. Salir")
        
        try:
            opcion = int(input("Ingrese la opción que desea: "))
            
            if opcion == 1:
                cantidad = float(input("Ingrese la cantidad en soles: "))
                if cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                else:
                    resultado = convertir_moneda("soles_a_dolares", cantidad)
                    print(f"{cantidad} soles son {resultado:.2f} dólares.")
            
            elif opcion == 2:
                cantidad = float(input("Ingrese la cantidad en dólares: "))
                if cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                else:
                    resultado = convertir_moneda("dolares_a_soles", cantidad)
                    print(f"{cantidad} dólares son {resultado:.2f} soles.")
            
            elif opcion == 3:
                print("¡Gracias por usar el conversor de monedas!")
                break
            
            else:
                print("Opción no válida, por favor ingrese una opción entre 1 y 3.")
        
        except Exception:
            print("Ocurrió un error inesperado. Asegúrese de ingresar solo números válidos.")
        
        if input("\n¿Desea realizar otra operación? (si/no): ").lower() != "si":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()