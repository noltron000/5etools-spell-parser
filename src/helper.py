# All spacial units are converted to points.
# Note, 72 points is an inch.
# Id rather use inches but fractions of inches are utilized.
# To keep all data as integers, points are used for data.
convert_space = {
	'point': 1,
	'inch': 72,
	'foot': 864,
	'yard': 2592,
	'mile': 4561920,
	'points': 1,
	'inches': 72,
	'feet': 864,
	'yards': 2592,
	'miles': 4561920,
}

# All temporal units are converted to seconds.
# Note, month and year have approximate values.
convert_time = {
	'second': 1,
	'round': 10,
	'minute': 60,
	'hour': 3600,
	'day': 86400,
	'week': 604800,
	'month': 2592000, # 30 days
	'year': 31104000, # 360 days
	'decade': 311040000,
	'century': 3110400000,
	'millennium': 31104000000,
	'seconds': 1,
	'rounds': 10,
	'minutes': 60,
	'hours': 3600,
	'days': 86400,
	'weeks': 604800,
	'months': 2592000, # 30 days
	'years': 31104000, # 360 days
	'decades': 311040000,
	'centuries': 3110400000,
	'millennia': 31104000000,
}

# We will be converting to & from strings often.
# Dictionaries like these help figure out plural words.
pluralize_space = {
	'point': 'points',
	'inch': 'inches',
	'foot': 'feet',
	'yard': 'yards',
	'mile': 'miles',
}
singularize_space = {
	'points': 'point',
	'inches': 'inch',
	'feet': 'foot',
	'yards': 'yard',
	'miles': 'mile',
}
pluralize_time = {
	'second': 'seconds',
	'round': 'rounds',
	'minute': 'minutes',
	'hour': 'hours',
	'day': 'days',
	'week': 'weeks',
	'month': 'months',
	'year': 'years',
	'decade': 'decades',
	'century': 'centuries',
	'millennium': 'millennia',
}
singularize_time = {
	'seconds': 'second',
	'rounds': 'round',
	'minutes': 'minute',
	'hours': 'hour',
	'days': 'day',
	'weeks': 'week',
	'months': 'month',
	'years': 'year',
	'decades': 'decade',
	'centuries': 'century',
	'millennia': 'millennium',
}

def assure_time_unit():
	pass

def time2num(amount, unit):
	return convert_time[unit] * amount

def time2str(amount, delimiter=' '):
	re.split(r'[\s-]+', string)
	pass

def space2num(amount, unit):
	return convert_space[unit] * amount

shape_parameters = {
	'aura': {
		'radius',
	},
	'sphere': {
		'radius',
	},
	'cone': {
		'radius',
	},
	'cylinder': {
		'radius',
		'height',
	},
	'cube': {
		'length',
	},
	'line': {
		'length',
		'width',
	},
	'wall': {
		'length',
		'width',
		'height',
	},
}