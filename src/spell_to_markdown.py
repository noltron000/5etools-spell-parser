from helper import *
from bad_string_parser import *

class SpellToMarkdown:
	def __init__(self, Spell):
		self.spell = Spell
		self.markdown = None
		self.main()

	def main(self):
		Spell = self.spell

		result = ''
		# Basic spell name as header
		result += f'# {Spell.name}'
		# Homebrew indicator
		result += '\n\n- [ ] Homebrew'
		# Adding spell level and school
		result += (
			f'\n\n***{nth_number(Spell.level)}'
			f'-level {Spell.school}***'
		)
		# Casting time is right up there
		result += (
			f'\n\n**Casting Time:** {time2str(Spell.cast_time)}'
		)
		# Duration is easy to grab
		if Spell.duration['quality']:
			duration = Spell.duration['quality']
		else:
			duration = time2str(Spell.duration)
		result += f'\n\n**Duration:** {duration}'
		# The range is just a number or string.
		if Spell.range['distance']:
			measurement = Spell.range['distance']
			measurement = space2str(measurement)
			result += f'\n\n**Range:** {measurement}'
		else:
			result += f'\n\n**Range:** {Spell.range["quality"]}'
		# The shape can be deconstructed with a for loop.
		shape = Spell.area['shape']
		if shape:
			result += f'\n\n**Shape:** {shape}'
			for dimension in shape_parameters[shape]:
				measurement = Spell.area[dimension]
				measurement = space2str(measurement)
				dimension = dimension.capitalize()
				result += f'\n\n{dimension}: {measurement}'
		# Instances isn't a good name but its what we got
		if Spell.instances != 1:
			result += f'\n\n**Effect Instances:** {Spell.instances}'
		# Spell tags
		for tag in Spell.tags:
			if Spell.tags[tag]:
				tag_list = self.distill_tags(Spell.tags).lower()
				result += f'\n\n**Tags:** {tag_list}'
				break
		# Spell components
		for component in Spell.components:
			if Spell.components[component]:
				result += (
					f'\n\n**{component.capitalize()} Components:** '
					f'{Spell.components[component]}'
				)
		# Spell description
		result += '\n\n---\n\n'
		result += Spell.description
		result += '\n\n---'
		# Spell class access
		classes = Spell.access['classes']
		if classes != []:
			classes = self.distill_access(classes).lower()
			result += f'\n\n**Classes:** {classes}'
		subclasses = Spell.access['subclasses']
		if subclasses != []:
			subclasses = self.distill_access(subclasses).lower()
			result += f'\n\n**Subclasses:** {subclasses}'
		races = Spell.access['races']
		if races != []:
			races = self.distill_access(races).lower()
			result += f'\n\n**Races:** {races}'
		subraces = Spell.access['subraces']
		if subraces != []:
			subraces = self.distill_access(subraces).lower()
			result += f'\n\n**Subraces:** {subraces}'
		# Finally, add the citation.
		book = book_transition_temp[Spell.citation['book']].upper()
		page = Spell.citation['page']
		cite = self.distill_citation(book, page)
		result += f'\n\n**Source:** {cite}'
		# Don't forget to set the markdown...
		result += '\n'
		result = cleanse_markdown(result)
		self.markdown = result

	def distill_tags(self, tags):
		tag_list = []
		for tag in tags:
			if tags[tag]:
				tag_list.append(tag)
		return ', '.join(tag_list)

	def distill_access(self, classes):
		result = ''
		result_array = []
		for player_class in classes:
			result_array.append(player_class)
		if result_array == []:
			return None
		result = ', '.join(result_array)
		return result

	def distill_citation(self, book, page):
		result = ''
		result += str(book)
		if page:
			result += ', page '
			result += str(page)
		return result
