from abuela import Abuela
from mesa import Mesa
from nieto import Nieto


mesa = Mesa(100)
abuela = Abuela("Andrea", mesa, 1, 10)
nietos = [Nieto(f"Nieto-{i}", mesa, 1/3, 10, 3) for i in range(3)]
