from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Role, Audition

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create a role
role = Role(character_name="Hamlet")
session.add(role)
session.commit()

# Create auditions
audition1 = Audition(actor="Alice", location="New York", phone=1234567890, role_id=role.id)
audition2 = Audition(actor="Bob", location="London", phone=9876543210, role_id=role.id)
session.add_all([audition1, audition2])
session.commit()

# Test call_back
audition1.call_back()
session.commit()

# Test relationships and methods
print(role.auditions)  # [<Audition id=1 ...>, <Audition id=2 ...>]
print(role.actors())  # ['Alice', 'Bob']
print(role.locations())  # ['New York', 'London']
print(role.lead())  # <Audition id=1 ...>
print(role.understudy())  # 'no actor has been hired for understudy for this role'

# Test Audition.role
print(audition1.role)  # <Role id=1 character_name=Hamlet>

# Clean up
session.query(Audition).delete()
session.query(Role).delete()
session.commit()