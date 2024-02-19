def inverter_string(s):
    string_invertida = ''

    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]

    return string_invertida

string_original = 'Estou feliz por participar do programa de estágio!'
string_invertida = inverter_string(string_original)

print("String Original:", string_original)
print("String Invertida:", string_invertida)
