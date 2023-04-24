import tkinter as tk
from tkinter import simpledialog, messagebox



class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = float(suma)
        self.zenklas = 1 if self.tipas == "pajamos" else -1


class Biudzetas:
    def __init__(self, suma):
        self.zurnalas = []
        self.suma = suma

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("pajamos", suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("išlaidos", suma)
        self.suma -= float(suma)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            balansas += irasas.zenklas * irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        ataskaita = ""
        for irasas in self.zurnalas:
            ataskaita += f"{irasas.tipas}: {irasas.suma}\n"
        return ataskaita





class BiudzetasGUI:
    def __init__(self, master):
        self.master = master
        master.title("Biudzetas")

        self.label = tk.Label(master, text="Pasirinkite operaciją:")
        self.label.pack(fill=tk.BOTH, expand=True)

        self.button1 = tk.Button(master, text="Įvesti pajamas", command=self.ivesti_pajamas)
        self.button1.pack(fill=tk.BOTH, expand=True)

        self.button2 = tk.Button(master, text="Įvesti išlaidas", command=self.ivesti_islaidas)
        self.button2.pack(fill=tk.BOTH, expand=True)

        self.button3 = tk.Button(master, text="Parodyti balansą", command=self.parodyti_balansa)
        self.button3.pack(fill=tk.BOTH, expand=True)

        self.button4 = tk.Button(master, text="Parodyti ataskaitą", command=self.parodyti_ataskaita)
        self.button4.pack(fill=tk.BOTH, expand=True)

        self.button5 = tk.Button(master, text="Išeiti", command=master.quit)
        self.button5.pack(fill=tk.BOTH, expand=True)



        self.biudzetas = Biudzetas(0)

    def ivesti_pajamas(self):
        pajamos = float(tk.simpledialog.askstring("Įvesti pajamas", "Įveskite pajamų sumą:"))
        self.biudzetas.prideti_pajamu_irasa(pajamos)

    def ivesti_islaidas(self):
        islaidos = float(tk.simpledialog.askstring("Įvesti išlaidas", "Įveskite išlaidų sumą:"))
        self.biudzetas.prideti_islaidu_irasa(islaidos)

    def parodyti_balansa(self):
        tk.messagebox.showinfo("Balansas", f"Balansas: {self.biudzetas.gauti_balansa()}")

    def parodyti_ataskaita(self):
        ataskaita =self.biudzetas.parodyti_ataskaita()
        tk.messagebox.showinfo("Ataskaita", f"{ataskaita}\n")





root = tk.Tk()
my_gui = BiudzetasGUI(root)
root.mainloop()
