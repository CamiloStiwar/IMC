#paso1: Pedirle a los usuarios el peso
pesoUsuarios = int(input("Por favor ponga su peso en kilogramos: "))
#paso2: pedirle a los usuarios la estatura
estaturaUsuarios = float(input("Por favor ponga su estatura en m: "))
#paso3: aplicar la formula para aplicar el IMC
formulaIMC = pesoUsuarios / (estaturaUsuarios**2)
#paso4: mostrar el imc dependiendo del caso
if formulaIMC < 18.5:
    print(f"Tienes bajo peso, tu IMC es de {formulaIMC} kg/m^2")

elif 18.5 < formulaIMC < 24.9:
    print(f"Tienes un peso normal, tu IMC es de {formulaIMC} kg/m^2")

elif 25 < formulaIMC < 29.9:
    print(f"Tienes sobrepeso, tu IMC es de {formulaIMC} kg/m^2")

elif formulaIMC > 30:
    print(f"Tienes obesidad, tu IMC es de {formulaIMC} kg/m^2")
 