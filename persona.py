class persona:
    tipoDoc=""
    documento=0
    nombre=""
    apellido=""
    peso=0
    estatura=0
    edad=0
    sexo=""
    
    def pedirDatos(self):
    tipoDoc = input("Ingrese su tipo de documento: ")
    documento = int(input("Ingrese su documento: "))
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    peso = int(input("Ingrese su peso: "))
    estatura = int(input("Ingrese su estatura: "))
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo: ")
    
    def mostrarPersona(self,tipoDoc,documento,nombre,apellido,peso,estatura,edad,sexo):
        print("el tipo del documento del usuario es{tipoDoc},su nombre es{nombre},su apellido es{apellido},su peso es{peso},su altura es de{altura},su edad es{edad},su sexo es{sexo}")
    
    
    def calcularmc(self,peso,estatura):
    peso = int(input("Ingrese su peso: "))
    estatura = int(input("Ingrese su estatura: "))
    peso_actual = peso / (estatura ** 2)
    print("El peso actual es:", peso_actual)
    return peso_actual
    def mayorEdad(self):
        if(edad>=18):
            print("eres mayor de edad")
        else:
            print("eres menor de edad")


  
        
        
    

    
   
    
      
        
        
    
    
    