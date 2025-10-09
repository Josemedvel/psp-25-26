import subprocess


texto = ""

with open("texto_prueba.txt", "r") as file:
    texto = file.read()

# print(texto)

p = subprocess.run(args=["grep", "rit"], input=texto, capture_output=True, text=True)

print(p.stdout)