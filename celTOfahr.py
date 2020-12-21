import sys
# programmed by @ysr075
def program():
    formCel = 1.8
    formFahr = 0.55555555555
    allDivider = 32
    nRestart = ["1", "restart", "r"]
    nQuit = ["2", "Quit", "q"]
    choose = float(input("\n1.Celsius to Fahrenheit.\n2.Fahrenheit to Celcius\n: "))
    if choose == 1:
        Celsius = float(input("\nCelsius: "))
        print("\n", (Celsius * formCel) + allDivider, "Fahrenheit.")
        restart = input("\nrestart of quit program: ").lower()
        if restart in nRestart:
            program()
        if restart in nQuit:
            sys.exit()
    if choose == 2:
        Fahrenheit = float(input("\nFahrenheit: "))
        print("\n", (Fahrenheit - allDivider) * formFahr, "Celsius.")
        restart = input("\nrestart or quit program: ")
        if restart in nRestart:
            program()
        if restart in nQuit:
            sys.exit()
    else:
        sys.exit()
program()
