class Pet:
    def __init__(self, name, species, family_type, owner):
        self.__petName = name
        self.__petSpecies = species
        self.__petFamilyType = family_type
        self.__petOwnerName = owner
        
    def set_Name(self, name):
        self.__petName = name
        
    def set_Species(self, species):
        self.__petSpecies = species
        
    def set_Family_Type(self, family_type):
        self.__petFamilyType = family_type
        
    def set_Owner(self, owner):
        self.__petOwnerName = owner
        
    def get_Name(self):
        return self.__petName
        
    def get_Species(self):
        return self.__petSpecies
        
    def get_Family_Type(self):
        return self.__petFamilyType
        
    def get_Owner(self):
        return self.__petOwnerName
        
    def __str__(self):
        return f"Pet name: {self.get_Name()}, species: {self.get_Species()}, family type: {self.get_Family_Type()}, owner: {self.get_Owner()}"