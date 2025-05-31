class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"pet_type must be one of {self.PET_TYPES}")
        # Defer owner validation to setter to avoid circular import
        self._name = name
        self._pet_type = pet_type
        self._owner = None  # Set owner later
        if owner is not None:
            self.owner = owner  # Use setter for validation
        Pet.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def pet_type(self):
        return self._pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        from owner import Owner  # Moved import inside setter
        if value is not None and not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner")
        self._owner = value