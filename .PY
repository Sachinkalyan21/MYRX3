from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from copy import deepcopy

@dataclass(frozen=True)
class Address:
    city: str
    state: str

@dataclass(frozen=True)
class ImmutableEmployee:
    name: str
    id: str
    date_of_joining: datetime
    addresses: List[Address] = field(default_factory=list)
    
    def __post_init__(self):
        # Validate the fields to ensure immutability
        if not self.name or not self.id or not self.date_of_joining:
            raise ValueError("Name, ID, and date_of_joining cannot be null")
        
        # Deepcopy the mutable fields to ensure immutability
        object.__setattr__(self, "addresses", deepcopy(self.addresses))

    def get_date_of_joining(self):
        # Return a copy of the date to ensure immutability
        return self.date_of_joining.replace()

    def get_addresses(self):
        # Return a deepcopy of the addresses list to ensure immutability
        return deepcopy(self.addresses)

# Example usage
if __name__ == "__main__":
    address1 = Address(city="New York", state="NY")
    address2 = Address(city="San Francisco", state="CA")
    addresses = [address1, address2]

    employee = ImmutableEmployee(
        name="John Doe",
        id="EMP123",
        date_of_joining=datetime(2020, 5, 20),
        addresses=addresses
    )

    print(employee)

    # Attempt to modify the list (immutable, deepcopy protects it)
    try:
        employee.get_addresses().append(Address(city="Los Angeles", state="CA"))
    except Exception as e:
        print("Modification not allowed:", e)

    # Output the object again
    print(employee)
