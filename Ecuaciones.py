class Ecuaciones_cua:
    def Ecuaciones(self):
        opcion="sinERROR"
        while opcion=="sinERROR":
            try:
                print('Ingrese su ecuacion como se le vaya pidiendo: ')
                a=float(input('Ingrese su termino "A": '))
                b=float(input('Ingrese su termino "B": '))
                c=float(input('Ingrese su termino "C": '))
                opcion="ELEMENTOS VALIDOS"
            except ValueError:
                print('\nELEMENTOS INVALIDOS')
                opcion="sinERROR"
        print("\n  ",opcion)
        obj=Ecuaciones_cua()
        obj.operaciones(a,b,c)


        
    def operaciones (self,a,b,c):
        import math as mt
        b_uno=b*-1
        b_dos=b**2
        ac=4*a*c
        a_uno=a*2
        raiz=b_dos-ac
        if raiz>=0:
            raiz=mt.sqrt(raiz)   
        else:
            print('\nTu ecuacion no tiene solucion en los numero reales')
            obj=Ecuaciones_cua()
            obj.final()
        # Resultado x_uno
        x_uno = b_uno + raiz
        x_uno = x_uno / a_uno
        # Resultado x_dos
        x_dos = b_uno - raiz
        x_dos = x_dos / a_uno
        print('\nEl resultado es: ')
        print('x=',x_uno)
        print('x=',x_dos)
        obj=Ecuaciones_cua()
        obj.final()
            
    def final(self):
        # sys para terminar un programa 
        import sys 
        print('\n\nGracias por usar el programa')
        sys.exit()
        
    
                
        
