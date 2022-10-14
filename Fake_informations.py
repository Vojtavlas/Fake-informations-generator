#By Github:VojtaVlas
from faker import Faker
fake = Faker()
print("all fake informations for you")
print("")
print("")
print(fake.name( ) + ": name")
print(fake.job( ) + ": job")
print(fake.company( ) + ": company")
print(fake.email( ) + ": email")
print(fake.address( ) + ": address")

