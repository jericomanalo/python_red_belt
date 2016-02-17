from system.core.controller import *
# import flash in order to flash messages
from flask import flash

class itemsControllers(Controller):
  def __init__(self, action):
    super(itemsControllers, self).__init__(action)
  	# // LOAD OUR MODEL // 
    self.load_model('itemsModel')

  # // DISPLAYING OUR PRODUCTS PAGE //
  # def products(self):
  #	allProducts = self.models['pModel'].get_all_products()
  #	print allProducts, "ALL PRODUCTS HERE"
  #	return self.load_view('products.html', allProducts = allProducts)

  # // DISPLAY A FORM TO ADD A NEW ITEM
  def new_item(self):
    return self.load_view('new.html')

  # // HANDLE ADD PRODUCT POST DATA TO BE SENT TO THE MODEL // 
  def create_item(self):
    item_info = {
    "name": request.form['name'],
      "user_id": request.form['user_id']
  	}
    newItem_status = self.models['itemsModel'].create_newItem(item_info)
    if newItem_status['status'] == True:
      return redirect('/dashboard')
    else:
      for message in newItem_status['errors']:
        flash(message, 'add_errors')
        return redirect('/items/add')

  # // DISPLAY THE PAGE BY ID
  def show(self, id):
  	item = self.models['itemsModel'].get_item_by_id(id)
  	return self.load_view('show.html', item = item)

  # // ADD ITEM TO WISHLIST
  def add_to_wishlist(self, id):
    wishlist_data = {
      "user_id": request.form['user_id'],
      "item_id": id
    }
    self.models['itemsModel'].add_to_wishlist_by_id(wishlist_data)
    return redirect('/dashboard')

  # // DISPLAY THE EDIT PAGE BY ID
  def edit(self, id):
  	product = self.models['pModel'].get_product_by_id(id)
  	return self.load_view('edit.html', product = product)

  # // HANDLE THE DESTROY PRODUCT POST DATA TO BE SENT TO THE MODEL
  def destroy(self, id):
  	destroy_data = {
  		'item_id': id,
      'user_id': request.form['user_id']
  	}
  	print request.form
  	self.models['itemsModel'].remove_item(destroy_data)
  	return redirect('/dashboard')

  def remove_favorite(self, id):
    removeFavorite_data = {
      'user_id': request.form['user_id'],
      'item_id': id
    }
    self.models['itemsModel'].remove_favorite(removeFavorite_data)
    return redirect('/dashboard')











