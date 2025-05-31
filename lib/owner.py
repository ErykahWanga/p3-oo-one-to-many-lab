
# lib/owner.py

class Owner:
    def __init__(self, name):
        if not name:
            raise Exception("Owner name cannot be empty")
        self.name = name
        self._pets = []
    ...


    def add_pet(self, pet):
        from lib.pet import Pet  # Delayed import to prevent circular import
        if isinstance(pet, Pet):
            if pet not in self._pets:
                self._pets.append(pet)
            if pet.owner != self:
                pet._owner = self  # avoid recursive loop by directly setting
        else:
            raise TypeError("pet must be an instance of Pet")

    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"
