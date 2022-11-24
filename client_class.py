class Client:
    def __init__(self,id,name,last_name,run,mail,bank,account_type="Vista",amount=0):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.run = run
        self.mail = mail
        self.bank = bank
        self.account_type = account_type
        self.amount = amount

    def withdraw(self):
        print("--------MENU BANCARIO--------")
        print("1.- INGRESAR DINERO")
        print("2.- RETIRAR DINERO")
        print("SALDO ACTUAL: ",self.amount)
        print("----------------")
        opcion = int(input("Ingrese la operacion que desea realizar: "))

        if(opcion==1):
            amount = int(input("Ingrese el monto a depositar: "))
            if(amount>0):
                self.amount += amount
        elif(opcion==2):
            amount = int(input("Ingrese el monto a retirar: "))
            if(amount<=self.amount):
                self.amount -= amount
            elif(amount>self.amount):
                print("Usted no posee el dinero suficiente para realizar este retiro")
        else:
            print("Ingrese una opcion valida!")

        print("Saldo actual: ",self.amount)

    def show_info(self):
        print("Nombre cliente: ",self.name,self.last_name)
        print("RUT: ",self.run)
        print("Correo: ",self.mail)
        print("Banco: ",self.bank," Cuenta: ",self.account_type)
        print("Saldo actual: ",self.amount)
