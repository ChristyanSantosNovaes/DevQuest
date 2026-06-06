#Exemplo de Tratamento de Erros:

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida!")
        return None
    except TypeError:
        print("Erro: Certifique-se de que ambos os argumentos são numeros.")
    else:
        print("Divisão realizada com sucesso!")
        return resultado
    finally:
        print("Execução da função dividir finalizada.")


print(f"Resultado 1: {dividir(10,2)}")
print(f"Resultado 2: {dividir(10,0)}")
print(f"Resultado 3: {dividir(10,"a")}")
print(f"Resultado 4: {dividir(20,4)}")

print("---------------------------------------------------------------------------------------------------------")

# Levantando exceções (raise)

def verificar_idade(idade):
    if not isinstance(idade, (int, float)):
        raise TypeError("A idade deve ser um numero.")
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    print(f"Idade valida: {idade}")


try:
    verificar_idade(30)
except (ValueError, TypeError) as e:
    print(f"Erro ao verificar idade: {e}")
try:
    verificar_idade("vinte")
except (ValueError, TypeError) as e:
    print(f"Erro ao verificar idade: {e}")
try:
    verificar_idade(30)
except (ValueError, TypeError) as e:
    print(f"Erro ao verificar idade: {e}")