

class Pet:
    all = []

    def __init__(self, name, species, owner=None):
        self.name = name
        self.species = species
        self._owner = None
        if owner:
            self.owner = owner  # uses setter
        Pet.all.append(self)

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
