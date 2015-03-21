import random 
from numpy.random import choice
from decimal import *

getcontext().prec = 64

def rationalize(weight_list):
	weight_sum = 0
	weight_ratio_list = []
	for x in weight_list:
		weight_sum += Decimal(x)
	for x in weight_list:
		x = Decimal(x)
		weight_ratio_list.append(Decimal(Decimal(x)/weight_sum))
	return weight_ratio_list

def random_material(material_type):
	material_rarity = []
	for x in range(34):
		material_rarity.append(Decimal(34**(1/1.5)) - Decimal(x**(1/1.5)))
	material_rarity = rationalize(material_rarity)
	material_dict = materials['dict']
	possible_material_dict = material_dict[material_type]
	possible_material_list = materials[material_type]
	material = choice(possible_material_list, p=material_rarity)	
	material_stat = possible_material_dict[material]
	material_attributes = [material, material_stat]
	return material_attributes

def weapon_class_chooser():
	classes = ['ranged','long bladed','shield','magic', 'blunt', 'concealed', 'gadget', 'book']
	weapon_class = random.choice(classes)
	return weapon_class

if True:
	ranged_weapons_file = open('ranged_weapons.txt')
	ranged_weapons_data = ranged_weapons_file.read().splitlines()
	ranged_weapons_split = []
	ranged_weapons = []
	for x in ranged_weapons_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			ranged_weapons_split.append(x)
	ranged_material = []
	ranged_rarity_linear = []
	for x in ranged_weapons_split:
		if (ranged_weapons_split.index(x) + 1) % 3 == 1:
			ranged_material.append(x)
		elif (ranged_weapons_split.index(x) + 1) % 3 == 2:
			ranged_rarity_linear.append(x)
		else:
			ranged_weapons.append(x)
	ranged_rarity = []
	for x in ranged_rarity_linear:
		x = int(x)
		ranged_rarity.append(Decimal(x**(1/1.5)))
	ranged_rarity = rationalize(ranged_rarity)	
	long_bladed_weapons_file = open('long_bladed_weapons.txt')
	long_bladed_weapons_data = long_bladed_weapons_file.read().splitlines()
	long_bladed_weapons_split = []
	long_bladed_weapons = []
	for x in long_bladed_weapons_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			long_bladed_weapons_split.append(x)
	long_bladed_material = []
	long_bladed_rarity_linear = []
	for x in long_bladed_weapons_split:
		if (long_bladed_weapons_split.index(x) + 1) % 3 == 1:
			long_bladed_material.append(x)
		elif (long_bladed_weapons_split.index(x) + 1) % 3 == 2:
			long_bladed_rarity_linear.append(x)
		else:
			long_bladed_weapons.append(x)
	long_bladed_rarity = []
	for x in long_bladed_rarity_linear:
		x = int(x)
		long_bladed_rarity.append(Decimal(x**(1/1.5)))
	long_bladed_rarity = rationalize(long_bladed_rarity)
	shields_file = open('shields.txt')
	shields_data = shields_file.read().splitlines()
	shields_split = []
	shields = []
	for x in shields_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			shields_split.append(x)
	shield_material = []
	shield_rarity_linear = []
	for x in shields_split:
		if (shields_split.index(x) + 1) % 3 == 1:
			shield_material.append(x)
		elif (shields_split.index(x) + 1) % 3 == 2:
			shield_rarity_linear.append(x)
		else:
			shields.append(x)
	shield_rarity = []
	for x in shield_rarity_linear:
		x = int(x)
		shield_rarity.append(Decimal(x**(1/1.5)))
	shield_rarity = rationalize(shield_rarity)
	magic_weapons_file = open('magic_weapons.txt')
	magic_weapons_data = magic_weapons_file.read().splitlines()
	magic_weapons_split = []
	magic_weapons = []
	for x in magic_weapons_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			magic_weapons_split.append(x)
	magic_material = []
	magic_rarity_linear = []
	for x in magic_weapons_split:
		if (magic_weapons_split.index(x) + 1) % 3 == 1:
			magic_material.append(x)
		elif (magic_weapons_split.index(x) + 1) % 3 == 2:
			magic_rarity_linear.append(x)
		else:
			magic_weapons.append(x)
	magic_rarity = []
	for x in magic_rarity_linear:
		x = int(x)
		magic_rarity.append(Decimal(x**(1/1.5)))
	magic_rarity = rationalize(magic_rarity)
	blunt_weapons_file = open('blunt_weapons.txt')
	blunt_weapons_data = blunt_weapons_file.read().splitlines()
	blunt_weapons_split = []
	blunt_weapons = []
	for x in blunt_weapons_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			blunt_weapons_split.append(x)
	blunt_material = []
	blunt_rarity_linear = []
	for x in blunt_weapons_split:
		if (blunt_weapons_split.index(x) + 1) % 3 == 1:
			blunt_material.append(x)
		elif (blunt_weapons_split.index(x) + 1) % 3 == 2:
			blunt_rarity_linear.append(x)
		else:
			blunt_weapons.append(x)
	blunt_rarity = []
	for x in blunt_rarity_linear:
		x = int(x)
		blunt_rarity.append(Decimal(x**(1/1.5)))
	blunt_rarity = rationalize(blunt_rarity)
	concealed_weapons_file = open('concealed_weapons.txt')
	concealed_weapons_data = concealed_weapons_file.read().splitlines()
	concealed_weapons_split = []
	concealed_weapons = []
	for x in concealed_weapons_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			concealed_weapons_split.append(x)
	concealed_material = []
	concealed_rarity_linear = []
	for x in concealed_weapons_split:
		if (concealed_weapons_split.index(x) + 1) % 3 == 1:
			concealed_material.append(x)
		elif (concealed_weapons_split.index(x) + 1) % 3 == 2:
			concealed_rarity_linear.append(x)
		else:
			concealed_weapons.append(x)
	concealed_rarity = []
	for x in concealed_rarity_linear:
		x = int(x)
		concealed_rarity.append(Decimal(x**(1/1.5)))
	concealed_rarity = rationalize(concealed_rarity)
	gadgets_file = open('gadgets.txt')
	gadgets_data = gadgets_file.read().splitlines()
	gadgets_split = []
	gadgets = []
	for x in gadgets_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			gadgets_split.append(x)
	gadget_material = []
	gadget_rarity_linear = []
	for x in gadgets_split:
		if (gadgets_split.index(x) + 1) % 3 == 1:
			gadget_material.append(x)
		elif (gadgets_split.index(x) + 1) % 3 == 2:
			gadget_rarity_linear.append(x)
		else:
			gadgets.append(x)
	gadget_rarity = []
	for x in gadget_rarity_linear:
		x = int(x)
		gadget_rarity.append(Decimal(x**(1/1.5)))
	gadget_rarity = rationalize(gadget_rarity)
	books_file = open('books.txt')
	books_data = books_file.read().splitlines()
	books_split = []
	books = []
	for x in books_data:
		x = x.split('/')
		weapon_data = x
		for x in weapon_data:
			books_split.append(x)
	book_material = []
	book_rarity_linear = []
	for x in books_split:
		if (books_split.index(x) + 1) % 3 == 1:
			book_material.append(x)
		elif (books_split.index(x) + 1) % 3 == 2:
			book_rarity_linear.append(x)
		else:
			books.append(x)
	book_rarity = []
	for x in book_rarity_linear:
		x = int(x)
		book_rarity.append(Decimal(x**(1/1.5)))
	book_rarity = rationalize(book_rarity)

def isnumeric(n):
        try:
                i = float(n)
        except (ValueError, TypeError):
            return False
        return True

def random_weapon(weapon_type='rand', maxlevel=100):

	def weapon_chooser(weapon_class):		
		if weapon_class == 'ranged':
			random_weapon = choice(ranged_weapons, p=ranged_rarity)
			if ranged_material[ranged_weapons.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special ranged' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'ranged'
				weapon_attributes['skill'] = 'ranged weapon'
				weapon_index = ranged_weapons.index(random_weapon)
				weapon_rarity = int(ranged_rarity_linear[weapon_index])
				weapon_level = round((10-int(ranged_rarity_linear[ranged_weapons.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if ranged_material[ranged_weapons.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'ranged' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'ranged'
				weapon_attributes['skill'] = 'ranged weapon'
				weapon_index = ranged_weapons.index(random_weapon)
				weapon_rarity = int(ranged_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'long bladed':
			random_weapon = choice(long_bladed_weapons, p=long_bladed_rarity)
			if long_bladed_material[long_bladed_weapons.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special long bladed' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'long bladed'
				weapon_attributes['skill'] = 'long bladed weapon'
				weapon_index = long_bladed_weapons.index(random_weapon)
				weapon_rarity = int(long_bladed_rarity_linear[weapon_index])
				weapon_level = round((10-int(long_bladed_rarity_linear[long_bladed_weapons.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if long_bladed_material[long_bladed_weapons.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'long bladed' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'long bladed'
				weapon_attributes['skill'] = 'long bladed weapon'
				weapon_index = long_bladed_weapons.index(random_weapon)
				weapon_rarity = int(long_bladed_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'shield':
			random_weapon = choice(shields, p=shield_rarity)
			if shield_material[shields.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special shield' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'shield'
				weapon_attributes['skill'] = 'shield'
				weapon_index = shields.index(random_weapon)
				weapon_rarity = int(shield_rarity_linear[weapon_index])
				weapon_level = round((10-int(shield_rarity_linear[shields.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if shield_material[shields.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'shield' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'shield'
				weapon_attributes['skill'] = 'shield'
				weapon_index = shields.index(random_weapon)
				weapon_rarity = int(shield_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'magic':
			random_weapon = choice(magic_weapons, p=magic_rarity)
			if magic_material[magic_weapons.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special magic' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'magic'
				weapon_attributes['skill'] = 'magic weapon'
				weapon_index = magic_weapons.index(random_weapon)
				weapon_rarity = int(magic_rarity_linear[weapon_index])
				weapon_level = round((10-int(magic_rarity_linear[magic_weapons.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if magic_material[magic_weapons.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'magic' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'magic'
				weapon_attributes['skill'] = 'magic weapon'
				weapon_index = magic_weapons.index(random_weapon)
				weapon_rarity = int(magic_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'blunt':
			random_weapon = choice(blunt_weapons, p=blunt_rarity)
			if blunt_material[blunt_weapons.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special blunt' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'blunt'
				weapon_attributes['skill'] = 'blunt weapon'
				weapon_index = blunt_weapons.index(random_weapon)
				weapon_rarity = int(blunt_rarity_linear[weapon_index])
				weapon_level = round((10-int(blunt_rarity_linear[blunt_weapons.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if blunt_material[blunt_weapons.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'blunt' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'blunt'
				weapon_attributes['skill'] = 'blunt weapon'
				weapon_index = blunt_weapons.index(random_weapon)
				weapon_rarity = int(blunt_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'concealed':
			random_weapon = choice(concealed_weapons, p=concealed_rarity)
			if concealed_material[concealed_weapons.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special concealed' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'concealed'
				weapon_attributes['skill'] = 'concealed weapon'
				weapon_index = concealed_weapons.index(random_weapon)
				weapon_rarity = int(concealed_rarity_linear[weapon_index])
				weapon_level = round((10-int(concealed_rarity_linear[concealed_weapons.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if concealed_material[concealed_weapons.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'concealed' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'concealed'
				weapon_attributes['skill'] = 'concealed weapon'
				weapon_index = concealed_weapons.index(random_weapon)
				weapon_rarity = int(concealed_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'gadget':
			random_weapon = choice(gadgets, p=gadget_rarity)
			if gadget_material[gadgets.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special gadget' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'gadget'
				weapon_attributes['skill'] = 'gadget'
				weapon_index = gadgets.index(random_weapon)
				weapon_rarity = int(gadget_rarity_linear[weapon_index])
				weapon_level = round((10-int(gadget_rarity_linear[gadgets.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if gadget_material[gadgets.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'gadget' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'gadget'
				weapon_attributes['skill'] = 'gadget'
				weapon_index = gadgets.index(random_weapon)
				weapon_rarity = int(gadget_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'book':
			random_weapon = choice(books, p=book_rarity)
			if book_material[books.index(random_weapon)] == 's':
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special book' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'book'
				weapon_attributes['skill'] = 'book'
				weapon_index = books.index(random_weapon)
				weapon_rarity = int(book_rarity_linear[weapon_index])
				weapon_level = round((10-int(book_rarity_linear[books.index(random_weapon)]))**2.09590327429)
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				if book_material[books.index(random_weapon)] == 'm':
					material = random_material('metal')
				else:
					material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'book' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'book'
				weapon_attributes['skill'] = 'book'
				weapon_index = books.index(random_weapon)
				weapon_rarity = int(book_rarity_linear[weapon_index])
				weapon_level = round((int((10-weapon_rarity)*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					return weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_skill = weapon_attributes['skill']
				weapon_skill = ' '.join(word[0].upper() + word[1:] for word in weapon_skill.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' ' + weapon_skill + ' Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes



	if weapon_type == 'rand':
		return weapon_chooser(weapon_class_chooser())
	else:	
		return weapon_chooser(weapon_type)

def weapon_generator(weapons_limit):
	counter = 0
	weapon_list = []
	while counter <= weapons_limit - 1:
		random_weapon_attributes = random_weapon('rand')
		weapon_list.append(random_weapon_attributes['name'])
		counter += 1
	return weapon_list

def user_process(user_input):
	end_process = False
	while end_process != True:
		if user_input != 'end' and isnumeric(user_input) == True:
			weapon_generator_list = weapon_generator(int(user_input))
			print('')
			for x in range(len(weapon_generator_list)):
				print(weapon_generator_list[x] + '\n')
			return user_process(input('How many more weapons to generate? (Type "end" to close program.) '))
		elif user_input == 'end':
			return 'Closing...'
			sleep(100)
			break
		else:
			return user_process(input('How many more weapons to generate? (Must be a number.) '))

def material_lister():
	metallic_material_file = open('metallic_materials.txt')
	metallic_materials = metallic_material_file.read().splitlines()
	metallic_material_stats = {}
	wooden_material_file = open('wooden_materials.txt')
	wooden_materials = wooden_material_file.read().splitlines()
	wooden_material_stats = {}
	for x in range(len(metallic_materials)):
		metallic_material_stats[metallic_materials[x]] = round((x+1)**1.6)
	for x in range(len(wooden_materials)):
		wooden_material_stats[wooden_materials[x]] = round((x+1)**1.6)
	material_dict = {'metal' : metallic_material_stats, 'wood' : wooden_material_stats}
	dict_list = {'metal' : metallic_materials, 'wood' : wooden_materials, 'dict' : material_dict}
	return dict_list	

materials = material_lister()

print(user_process(input('How many weapons to generate? (Type "end" to close program.) '))
)
