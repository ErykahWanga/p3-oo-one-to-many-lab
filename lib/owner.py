from pet import Pet

class Owner:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def pets(self):
        """Return a list of all pets belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner after validating it is a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of this owner's pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)