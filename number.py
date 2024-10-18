def divide_numbers():
    try:
        num1 = float(input("Ievadiet pirmo skaitļi:"))
        num2 = float(input("Ievadiet otro skaitli:"))
        result = num1/num2
        print(f"Rezultāts: {result}")

    except ZeroDivisionError:
        print("Kļuda: Dalīšana ar nulli nav atļauta.")

    except ValueError:
        print("Kļuda:Lūdzu, ievadiet derīgus kaitļus.")

    except Exception:
        print(f"Radās neparedzēta kļūda: {e}")

    finally:
        print("Darbība pabeigta.")

class Kalkulators:
    def __init__(self, skaitlis1, skaitlis2):
        self.skaitlis1 = skaitlis1
        self.skaitlis2 = skaitlis2
        
    def saskaitisana(self):
        return self.skaitlis1 + self.skaitlis2
    def atnemsana(self):
        return self.skaitlis1 - self.skaitlis2
    def reizinajums(self):
        return self.skaitlis1 * self.skaitlis2
    def dalisana(self):
        try:
            return self.skaitlis1 / self.skaitlis2
        except ZeroDivisionError:
            return "Kļūda: mēģinājums dalīt ar nulli!"
    def iegut_skaitli(teksts):
        while True:
        try:
            return float(input(teksts))
        except ValueError:
            print("Kļūda: lūdzu, ievadiet derīgu skaitli.")
    if __name__ == "__main__":
        skaitlis1 = iegut_skaitli("Ievadiet pirmo skaitli: ")
        skaitlis2 = iegut_skaitli("Ievadiet otro skaitli: ")
        kalkulators = Kalkulators(skaitlis1, skaitlis2)
        print(f"Saskaitīšana: {kalkulators.saskaitisana()}")
        print(f"Atņemšana: {kalkulators.atnemsana()}")
        print(f"Reizinājums: {kalkulators.reizinajums()}")
        print(f"Dališana: {kalkulators.dalisana()}")