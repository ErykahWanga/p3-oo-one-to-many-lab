

# lib/pet.py

class Pet:
    all = []

    def __init__(self, name, pet_type, owner=None):  # rename parameter
        self.name = name
        self.pet_type = pet_type  # store as pet_type to match test
        self._owner = None
        if owner:
            self.owner = owner
        Pet.all.append(self)
    ...


    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        from lib.owner import Owner  # Delayed import to prevent circular import
        if isinstance(owner, Owner):
            self._owner = owner
            owner.add_pet(self)  # ensure pet is added to owner's pet list
        else:
            raise TypeError("owner must be an instance of Owner")

    def __repr__(self):
        return f"<Pet name={self.name} species={self.species}>"
