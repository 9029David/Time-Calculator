# Crear diccionario
def diccionario(cadena):
    horario = {}
    cadena_formato = cadena.split()
    cadena_hora = cadena_formato[0].split(':')
    horario['horas'] = cadena_hora[0]
    horario['minutos'] = cadena_hora[1]
    if len(cadena_formato) > 1:
        horario['formato'] = cadena_formato[1]
        horario['dia_semana'] = ''
    else:
        horario['formato'] = ''
    return horario

# Suma de cadenas
def suma(dic1, dic2):
    dic1 = diccionario(dic1)
    dic2 = diccionario(dic2)
    suma_horas = int(dic1['horas']) + int(dic2['horas'])
    suma_minutos = int(dic1['minutos']) + int(dic2['minutos'])
    formato = dic1['formato']

    if suma_minutos >= 60:
        suma_horas += suma_minutos // 60
        suma_minutos %= 60
    
    dic1['horas'] = str(suma_horas)
    dic1['minutos'] = str(suma_minutos).zfill(2)  
    dic1['formato'] = formato
    
    return dic1
# Formato AM - PM
def formato_hora(diccionario, dia):
    horas = diccionario['horas']
    horas_int = int(horas)
    formato = diccionario['formato']
    
    cont_dias = horas_int // 24
    horas_int %= 24

    if horas_int >= 12:
        if formato == 'AM':
            formato = 'PM'
        else:
            formato = 'AM'
            cont_dias += 1

    if horas_int == 0:
        horas_int = 12
    elif horas_int > 12:
        horas_int -= 12

    diccionario['horas'] = str(horas_int)
    diccionario['formato'] = formato
    diccionario['dias'] = cont_dias
    diccionario['dia_semana'] = dia

    return diccionario

# Dia de la semana
def dia_de_la_semana (diccionario):
    dias_pasados = diccionario['dias']
    dia = diccionario['dia_semana']
    if dia:
        dia = dia.lower()
        dias = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if dia in dias:
            index = dias.index(dia)
            resultado = dias[(index + dias_pasados) % len(dias)]
            return resultado.capitalize()
    return '' 
        
# Mensaje personalizado 
def mensaje(diccionario):
    dias_pasados = diccionario['dias']
    horas = diccionario['horas']
    minutos = diccionario['minutos']
    formato = diccionario['formato']
    resultado = dia_de_la_semana(diccionario)
    
    if diccionario['dia_semana'] == '':
        mensaje_cero = f'{horas}:{minutos} {formato}'
        mensaje_uno = f'{horas}:{minutos} {formato} (next day)'
        mensaje_dos = f'{horas}:{minutos} {formato} ({dias_pasados} days later)'
        
    else:
        mensaje_cero = f'{horas}:{minutos} {formato}, {resultado}'
        mensaje_uno = f'{horas}:{minutos} {formato}, {resultado} (next day)'
        mensaje_dos = f'{horas}:{minutos} {formato}, {resultado} ({dias_pasados} days later)'
    
    if dias_pasados == 0:
        return mensaje_cero 
    elif dias_pasados == 1:
        return mensaje_uno
    else:
        return mensaje_dos
    
        
def add_time(start, distance, dia=''):
    suma_de_horas = suma(start, distance)
    formato = formato_hora(suma_de_horas, dia)
    my_time = mensaje(formato)
    return my_time


resultado = add_time('2:59 AM', '24:00', 'saturDay')
print(resultado)