#!/usr/bin/env
favorites = {}
favorites['book'] = 'Fourth Wing'
favorites['song'] = "Can't Hold Us"
favorites['tree'] = 'Cedar'
favorites['organism'] = 'Xenopus'
favorites['organism'] = 'c.elegans'

print(favorites['book'])
print(favorites['tree'])

for favorite in favorites:
   print(favorite, favorites[favorite])
print(favorites['song'])

for favorite in favorites: 
 print(favorite)


