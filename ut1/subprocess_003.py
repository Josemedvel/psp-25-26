import subprocess

fichero = input("Ingrese nombre de fichero:\t")
aguja = input("Ingrese cadena a buscar:\t")
p_cat = subprocess.run(args=["cat", fichero], capture_output=True, text=True)
p_grep = subprocess.run(args=["grep", aguja], capture_output=True, text=True, input=p_cat.stdout)

print(p_grep.stdout)