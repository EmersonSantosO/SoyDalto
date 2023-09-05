class Personage:
    def __init__(self, name, power, *args) -> None:
        self.name = name
        self.power = power
        self.skills = list(args)

    def __str__(self) -> str:

        return f"name = {self.name}, Power = {self.power}, Skills = {self.skills}"

    def __add__(self, other):
        newName = self.name + other.name
        newPower = self.power + other.power
        newSkills = self.skills + other.skills
        return Personage(newName, newPower, newSkills)

    def addAbility(self, ability):
        self.skills.append(ability)


goku = Personage("goku", 10000, "jamejame haaa", "tp", "mondongo")
jiren = Personage("jiren", 10000000, "se pelao", "marcianito", "bailar cumbia")
goku.addAbility("XD")
newPersonage = goku+jiren

print(newPersonage)
