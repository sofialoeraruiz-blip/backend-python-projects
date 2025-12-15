teams = []
players = []

def team_registration():
    print("REGISTRO DE EQUIPOS")
    while True:
        teamname = input("Ingrese el nombre del equipo (A o B): ").strip().capitalize()
        if teamname not in ("A", "B"):
            print("Solo se permiten los equipos 'A' o 'B'. Intente de nuevo.")
            continue
        if any(team["nombre"] == teamname for team in teams):
            print(f"El equipo {teamname} ya está registrado. Elija el otro.")
            continue
        break

    while True:
        try:
            participants = int(input("Ingrese el número de participantes (2 por equipo): "))
        except ValueError:
            print("El número de participantes debe ser un número entero.")
            continue
        if participants == 2:
            break
        else:
            print("Cada equipo debe tener exactamente 2 participantes.")

    teams.append({
        "nombre": teamname,
        "puntos": 0,
        "jugadores": []
    })
    print(f"Equipo '{teamname}' registrado exitosamente.")

def user_registration():
    if len(teams) < 2:
        print("Primero debes registrar los 2 equipos antes de agregar jugadores.")
        return

    print("REGISTRO DE JUGADOR")
    while True:
        username = input("Ingrese su nombre: ").strip().title()
        if not username:
            print("El nombre no puede estar vacío.")
            continue
        if any(player["nombre"] == username for player in players):
            print("Ese jugador ya está registrado. Ingresa otro nombre.")
            continue
        break

    while True:
        try:
            userAge = int(input("Ingrese su edad: "))
        except ValueError:
            print("La edad debe ser un número entero.")
            continue
        if userAge > 14:
            break
        else:
            print("No tienes la edad suficiente para participar.")
            return

    while True:
        teamname = input("Ingrese el equipo al que pertenece (A o B): ").strip().capitalize()
        if teamname in ("A", "B") and any(team["nombre"] == teamname for team in teams):
            break
        print("Equipo inválido o no registrado. Intente de nuevo.")

    players.append({
        "nombre": username,
        "edad": userAge,
        "equipo": teamname
    })

    for team in teams:
        if team["nombre"] == teamname:
            team["jugadores"].append(username)

    print(f"Jugador '{username}' registrado exitosamente en el equipo '{teamname}'.")

def enter_scores():
    if len(teams) < 2:
        print("Se necesitan los 2 equipos registrados para ingresar puntuaciones.")
        return

    print("INGRESO DE PUNTUACIONES")
    while True:
        team_name = input("Ingrese el nombre del equipo: ").strip().capitalize()
        if any(team["nombre"] == team_name for team in teams):
            break
        print("Equipo inválido. Intente de nuevo.")

    while True:
        try:
            round1 = int(input("Puntos de la ronda 1: "))
            round2 = int(input("Puntos de la ronda 2: "))
            round3 = int(input("Puntos de la ronda 3: "))
            break
        except ValueError:
            print("Los puntos deben ser números enteros. Intente de nuevo.")

    total = round1 + round2 + round3
    for team in teams:
        if team["nombre"] == team_name:
            team["puntos"] += total

    print(f"Equipo: {team_name}")
    print(f"Ronda 1: {round1} puntos")
    print(f"Ronda 2: {round2} puntos")
    print(f"Ronda 3: {round3} puntos")
    print(f"Total sumado al equipo: {total} puntos")

def show_results():
    if len(teams) < 2:
        print("Se necesitan los 2 equipos registrados para mostrar la tabla de posiciones.")
        return

    print("TABLA DE POSICIONES")
    sorted_teams = sorted(teams, key=lambda x: x["puntos"], reverse=True)
    for team in sorted_teams:
        jugadores = ", ".join(team['jugadores']) if team['jugadores'] else "Sin jugadores"
        print(f"Equipo {team['nombre']}, {team['puntos']} puntos, Jugadores: {jugadores}")

def eliminar_equipo():
    global teams, players
    if not teams:
        print("No hay equipos registrados.")
        return
    
    teamname = input("Ingrese el equipo a eliminar: ").strip().capitalize()
    if not any(team["nombre"] == teamname for team in teams):
        print("El equipo no existe o no está registrado.")
        return

    teams = [team for team in teams if team["nombre"] != teamname]
    players = [player for player in players if player["equipo"] != teamname]

    print(f"El equipo '{teamname}' y todos sus jugadores han sido eliminados.")

def menu():
    print("Bienvenido al torneo de juegos 2025!")
    while True:
        print("MENÚ DEL TORNEO")
        print("1. Registrar equipo")
        print("2. Registrar jugador")
        print("3. Actualizar puntos")
        print("4. Ver tabla de posiciones")
        print("5. Eliminar equipo")
        print("6. Salir")

        opcion = input("Elegir una opción (Ej: 1 ): ")

        if opcion == "1":
            team_registration()
        elif opcion == "2":
            user_registration()
        elif opcion == "3":
            enter_scores()
        elif opcion == "4":
            show_results()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()







                