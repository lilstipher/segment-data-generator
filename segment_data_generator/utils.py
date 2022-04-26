import logging
from typing import Tuple
from faker import Faker
import faker_commerce
import base64

from random import randrange ,choice
 
_logger = logging.getLogger(__name__)
fake = Faker ()
fake.add_provider(faker_commerce.Provider)
Faker.seed(1)


def generate_identify_data() -> Tuple[str,dict]:
    """Generate identify data

    Returns:
        Tuple[str,dict]: (user_id,traits)
    """    
    fake.seed_instance(randrange(0,10))

    name = fake.name()
    user_id = base64.b16encode(str.encode(name)).decode().lower()
    traits = {
      'email': f"{name.lower().replace(' ','')}@example.org",
      'name': name,
      'state': fake.state(),
      'friends': randrange(0,1000)
    }
    _logger.info(f"Generated identify data with id {user_id}")
    _logger.debug(f"user_id = {user_id},traits = {traits}")
    return (user_id,traits)


def generate_track_data() -> Tuple[str,dict]:
    """Generate tracking data

    Returns:
        Tuple[str,dict]: (user_id,event_name,event)
    """   
    fake.seed_instance(randrange(0,10))
    name = fake.name()
    user_id = base64.b16encode(str.encode(name)).decode().lower()
    event_name = choice( [ "Signed Up" ,"Article Bookmarked" , "Purchased"])
    event = ""
    if event_name == "Signed Up" :
        event = {'plan': choice(["Pro","Free", "Business", "Enterprise"]) }
    else :
        event =  {
      'Title': fake.ecommerce_name(),
      'author': fake.name(),
      'price':randrange(0,1000) #choice ([f"{randrange(0,1000)} $",randrange(0,1000)])
    }
    _logger.info(f"Generated track data with id {user_id}")
    _logger.debug(f"user_id = {user_id},event_name = {event_name},event = {event}")
    return (user_id,event_name,event)
