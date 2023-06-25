print('''Menu Morelba
    1. Hamburguesa de pollo
    2.Pasta con huevo
    3.Pescado frito
    4.Pasta con atun
    5.Carne asada
    6.Arroz con pollo
    7.Pasta con albondigas
    8.Arepas con queso''')
opcion= int (input('Por favor selecciona una opcion (entre el 1 y el 8) '))
if opcion<1:
    print("Por favor introducir una opcion valida]")
elif opcion==1:
    print('Descripcion: ri0taza y variedad de verduras. Precio $10 Peso: 200 g Codigo: APEX')
elif opcion==2:
    print('Descripcion: Deliciosa pasta con alto valor nutricional que contiene 4 huevos revueltos y abundante queso rallado. Precio $5 Peso: 150 g Codigo: AB1506')
elif opcion==3:
    print('Suculento filete de pescado frito con verduras como lechuga, pimenton y tomate. Precio $15 Peso: 250 g Codigo: 0804')
elif opcion==4:
    print('Exquisita pasta larga tipo vermicelli con abundante atun y mayonesa. Precio $10 Peso: 100 g Codigo: 15062')
elif opcion==5:
    print('Jugosa carne a la parrilla con tomate y cebolla. Precio $15 Peso: 300 g Codigo: 2405')
elif opcion==6:
    print('La receta exclusiva de la casa, un delicioso arroz con pollo acompanado de cilantro y cebolla larga con trocitos de pollo. Precio $8 Peso: 300 g Codigo: 0702')
elif opcion==7: 
    print('Una sabrosa pasta aompanada con albondigas hechas a base de carne molida, con cuaddritos de zanahoria y abundanto salsa de tomate. Precio 9$ Peso: 230 g Codigo: 0258')
elif opcion==8:
    print('La receta tradicional venezolana! Arepas rellenas con queso de mano y margarina. Precio $2.5 C/U Peso: 50 g Codigo: 1987')
elif opcion>8:
    print('Por favor ingresar una opcion valida')

