from system.core.model import Model
## IMPORT FLASH FROM FLASK AND REGULAR EXPRESSION
from flask import flash
import re

class usersModel(Model):

  def __init__(self):
    super(usersModel, self).__init__()

  # // Create a function that adds a user with validations via querying into the database //
  def register_user(self, info):
    # We write our validations in model functions
    # They look similar to those we wrote in Flask
    # EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
    PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')
    errors = []
    # Validations
    if not info['name']:
      errors.append('Name cannot be blank')
    elif len(info['name']) < 3:
      errors.append('Name must be at least 3 characters long')
    if not info['username']:
      errors.append('Username cannot be blank')
    elif len(info['username']) < 3:
      errors.append('Username must be at least 3 characters long')
    if not info['password']:
      errors.append('Password must not be blank')
    elif len(info['password']) < 8:
      errors.append('Password must be at least 8 characters long')
    elif not PASS_REGEX.match(info['password']):
      errors.append('Password must contain at least one number, upper and lower case letter')
    if info['password'] != info['confirm_password']:
      errors.append('Password and confirmation must match')
    if not info['date_hired']:
      errors.append('Date hired cannot be blank and format must be valid: xx/xx/xx')

    # If we have errors, return them, else return True
    if errors: 
      return {"status": False, "errors": errors}
    else:
      # Code to insert user into database
      password = info['password']
      hashed_password = self.bcrypt.generate_password_hash(password)
      query = "INSERT INTO users (name, username, password, date_hired, created_at, updated_at) VALUES (%s, %s, %s, %s, NOW(), NOW())"
      data = [
        info['name'],
        info['username'],
        hashed_password,
        info['date_hired']
      ]
      self.db.query_db(query, data)
      # Then retrieve last inserted user
      get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
      user =  self.db.query_db(get_user_query)
      return { "status": True, "user": user[0] }

  # // Create a function that checks to see if we have a matching user and password by querying to the database
  def login_user(self, info):
    # Explicitly instantiate variables so that it is easier to track the information that is going to be passed into the self.db.query() function
    password = info['password']
    query = 'SELECT * FROM users where username = %s LIMIT 1'
    data = [info['username']]
    user = self.db.query_db(query, data)

    # If the array gets returned back empty, that means there is no match in the database so we return False
    if user == []:
      return { "status": False }
    else:
      # This tests to see if the password that was previously input matches the same bcrypted value that was already stored in the database
      if self.bcrypt.check_password_hash(user[0]['password'], password):
        return { "status": True, "user": user[0]}
      else:
        return {"status": False}











