from system.core.model import Model
## IMPORT FLASH FROM FLASK AND REGULAR EXPRESSION
from flask import flash
import re

class itemsModel(Model):

	def __init__(self):
		super(itemsModel, self).__init__()

	def create_newItem(self, info):
		errors = []
		if not info['name']:
			errors.append('Name cannot be blank')
		elif len(info['name']) < 3:
			errors.append('Name must be at least 3 characters long')
		# If we have errors, return them, else return True
		if errors: 
			return {"status": False, "errors": errors}
		else:
			query = "INSERT INTO items (name, created_at, updated_at, user_id) VALUES (%s, NOW(), NOW(), %s)"
			data = [
			info['name'],
			info['user_id']
		]
		self.db.query_db(query, data)
		get_user_query = "SELECT * FROM items ORDER BY id DESC LIMIT 1"
		item =  self.db.query_db(get_user_query)
		return { "status": True, "item": item[0] }

	def get_all_items(self):
		query = 'SELECT * FROM items'
		return self.db.query_db(query)

	def get_item_by_id(self, id):
		query = 'SELECT * FROM items WHERE id = %s'
		data = [id]
		return self.db.query_db(query, data)

	def add_to_wishlist_by_id(self, wishlist_data):
		query = "INSERT INTO wishlists (user_id, item_id) VALUES (%s, %s)"
		data = [
			wishlist_data['user_id'],
			wishlist_data['item_id']
		]
		return self.db.query_db(query, data)
	# def get_all_wishlists(self, id):
	#   query = "SELECT name, item_id, user_id FROM users LEFT JOIN wishlists ON users.id = wishlists.id LEFT JOIN items ON wishlists.id = items.id WHERE users.id = %s"
	#   data = [id]
	#   self.db.query_db(query, data)

	def get_wishlist_by_id(self, id):
	  query = 'SELECT * FROM wishlists LEFT JOIN items ON items.id = wishlists.item_id WHERE wishlists.user_id = %s'
	  data = [id]
	  return self.db.query_db(query, data)

	def remove_item(self, info):
		query = "DELETE FROM items WHERE id = %s and user_id = %s"
		data = [
			info['id'],
			info['user_id']]
		return self.db.query_db(query, data)

	def remove_favorite(self, info):
		query = "DELETE FROM wishlists WHERE user_id = %s and item_id = %s"
		data = [
			info['user_id'],
			info['item_id']
		]
		return self.db.query_db(query, data)








