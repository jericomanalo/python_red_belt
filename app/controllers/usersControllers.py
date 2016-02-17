from system.core.controller import *
# import flash in order to flash messages
from flask import flash

class usersControllers(Controller):
  def __init__(self, action):
    super(usersControllers, self).__init__(action)
    # // LOAD OUR MODELS // 
    self.load_model('usersModel')
    self.load_model('itemsModel')

  # // CONTROLLER FOR DISPLAYING OUR FIRST INDEX PAGE THAT HOLDS OUR REGISTRATION AND LOGIN FORMS // 
  def index(self):
    return self.load_view('index.html')

  # // CONTROLLER FOR HANDLING REGISTER POST DATA TO BE SENT TO THE MODEL // 
  def register(self):
    # gather the data that was posted to our register method and format it to pass it to the model
    user_info = {
      "name": request.form['name'],
      "username": request.form['username'],
      "password": request.form['password'],
      "confirm_password": request.form["confirm_password"],
      "date_hired": request.form["date_hired"]
    }
    # call the register_user method from model and write some logic based on the returned value
    # notice how we passed the user_info to our model method
    print user_info
    create_status = self.models['usersModel'].register_user(user_info)
    if create_status['status'] == True:
      # the user should have been created in the model
      # we can set the newly-created users id and name to session
      session['id'] = create_status['user']['id']
      session['username'] = create_status['user']['username']
      # we can redirect to the users profile ('/success') page here
      return redirect('/dashboard')
    else:
      # set flashed error messages here
      for message in create_status['errors']:
        flash(message, 'registration_errors')
      # redirect back home which renders the registration form
      return redirect('/')

  # // CONTROLLER FOR HANDLING THE REDIRECTION OF A SUCCESSFUL REGISTER ATTEMPT // 
  def dashboard(self):
    get_all_items = self.models['itemsModel'].get_all_items()
    wishlist = self.models['itemsModel'].get_wishlist_by_id(session['id'])
    return self.load_view('dashboard.html', name = session['username'], id = session['id'], allItems = get_all_items, wishlist = wishlist)
  
  # // CONTROLLER FOR LOGGING OUT A LOGGED IN USER // 
  def logout(self):
    session.clear()
    return redirect('/')

  # // CONTROLLER FOR LOGGING IN AS A PREVIOUS USER //
  def login(self):
    user_info = {
      'username': request.form['login_username'],
      'password': request.form['login_password']
      }
    login_status = self.models['usersModel'].login_user(user_info)
    if login_status['status'] == True:
      # the user should have been found in the database
      # set the user id and name to session
      session['id'] = login_status['user']['id']
      session['username'] = login_status['user']['username']
      # we can now redirect to the users profile ('/dashboard') page here
      return redirect('/dashboard')
    else:
      # set flashed error messages here
      flash('Email and/or password are not valid. Try again.')
      # redirect back home which renders the registration and login forms
      return redirect('/')














