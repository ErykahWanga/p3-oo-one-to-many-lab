import pytest
from lib.owner import Owner
from lib.pet import Pet

def test_owner_init():
    """Test that Owner initializes with a valid name."""
    owner = Owner("John")
    assert owner.name == "John"
    with pytest.raises(Exception):
        Owner("")  # Should raise Exception for empty name
    with pytest.raises(Exception):
        Owner(123)  # Should raise Exception for non-string

def test_pet_init():
    """Test that Pet initializes with valid name, pet_type, and optional owner."""
    owner = Owner("John")
    pet = Pet("Fluffy", "cat", owner)
    assert pet.name == "Fluffy"
    assert pet.pet_type == "cat"
    assert pet.owner == owner
    with pytest.raises(Exception):
        Pet("Fluffy", "fish")  # Invalid pet_type
    with pytest.raises(Exception):
        Pet("", "cat")  # Empty name
    with pytest.raises(Exception):
        Pet("Fluffy", "cat", "not_an_owner")  # Invalid owner

def test_pet_all():
    """Test that all Pet instances are stored in Pet.all."""
    Pet.all.clear()  # Clear to ensure a clean test
    pet1 = Pet("Fluffy", "cat")
    pet2 = Pet("Rex", "dog")
    assert len(Pet.all) == 2
    assert pet1 in Pet.all
    assert pet2 in Pet.all

def test_owner_pets():
    """Test that Owner.pets() returns the correct list of pets."""
    owner = Owner("John")
    pet1 = Pet("Fluffy", "cat", owner)
    pet2 = Pet("Rex", "dog")
    assert owner.pets() == [pet1]
    pet2.owner = owner
    assert sorted(owner.pets(), key=lambda x: x.name) == [pet1, pet2]

def test_owner_add_pet():
    """Test that Owner.add_pet() adds a pet and sets the owner."""
    owner = Owner("John")
    pet = Pet("Fluffy", "cat")
    owner.add_pet(pet)
    assert pet.owner == owner
    assert pet in owner.pets()
    with pytest.raises(Exception):
        owner.add_pet("not_a_pet")  # Should raise Exception

def test_owner_get_sorted_pets():
    """Test that Owner.get_sorted_pets() returns a sorted list by name."""
    owner = Owner("John")
    pet1 = Pet("Zorro", "cat", owner)
    pet2 = Pet("Alpha", "dog", owner)
    sorted_pets = owner.get_sorted_pets()
    assert sorted_pets == [pet2, pet1]