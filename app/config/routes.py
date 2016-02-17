from system.core.router import routes


# // DEFAULT // 
routes['default_controller'] = 'usersControllers'

# // ADD USER VIA POST DATA //
routes['POST']['/register'] = 'usersControllers#register'

# // REDIRECT TO THE SUCCESS.HTML AFTER '/register' ADDS A USER TO THE DATABASE //
routes['GET']['/dashboard'] = 'usersControllers#dashboard'

# // LOG OUT //
routes['GET']['/logout'] = 'usersControllers#logout'

# // LOG IN AS A PREVIOUS USER //
routes['POST']['/login'] = 'usersControllers#login'

# // GO TO THE NEW.HTML PAGE //
routes['GET']['/items/add'] = 'itemsControllers#new_item'

# // ADD PRODUCT VIA POST DATA //
routes['POST']['/items'] = 'itemsControllers#create_item'

# // SHOW ITEM BY ID //
routes['GET']['/items/<int:id>'] = 'itemsControllers#show'

# // ADD ITEM TO MY WISHLIST //
routes['POST']['/wishlists/<int:id>'] = 'itemsControllers#add_to_wishlist'

# // DESTROY THE ITEM VIA POST DATA
routes['POST']['/items/<int:id>'] = 'itemsControllers#destroy'

routes['POST']['/wishlists/<int:id>/remove'] = 'itemsControllers#remove_favorite'
