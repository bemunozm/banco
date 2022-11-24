from client_class import Client

def main():
    #variables
    client_1 = 0
    name = ""
    last_name = ""
    run = ""
    mail = ""
    bank = ""
    account_type = ""
    amount = 0

    #entrada de datos
    name = input("Ingrese el nombre del cliente: ")
    last_name = input("Ingrese el apellido del cliente: ")
    run = input("Ingrese el RUT del cliente: ")
    mail = input("Ingese el correo electronico del cliente: ")
    bank = input("Ingrese el banco donde desea crear su cuenta: ")
    account_type = input("Ingrese el tipo de cuenta a crear: ")

    #crear objetos
    client_1 = Client(1,name,last_name,run,mail,bank,account_type)
    print("\n----NUEVO CLIENTE CREADO----")
    client_1.show_info()

    #cambiar monto
    opcion = int(input("\nDesea realizar alguan operacion bancaria?(1.SI; 2.NO): "))
    if(opcion==1):
        client_1.withdraw()
    else:
        print("FIN")

if __name__ == "__main__":
    main()