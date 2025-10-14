import subprocess

proceso_1 = subprocess.run(args=["ls", "-l"], capture_output=True, text=True)
#print(proceso_1.stdout)
print(proceso_1.returncode)
proceso_2 = subprocess.run(args=["grep", "process"], input=proceso_1.stdout, capture_output=True, text=True)
print(proceso_2.stdout)