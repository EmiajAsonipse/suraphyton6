#Los diccionarios son variables especiales 
# que me permiten almacenar multiples datos 
# de diferente tipo en una sola variable  #son atributos

empleado={
    'nombre':"Juan",
    'Cedula':"1001727063",
    'Cargo':"Analista de datos",
    'Salario':8000000,
    'Horas trabajadas':40,
    'aplicasubsidiodetrasnporte':False,
    'deudas':[1500000,800000]
}
#print(empleado)
#print(empleado['deudas'][1])


#recorriendo un diccionario:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)