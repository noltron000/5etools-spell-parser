import os
import re

class Library:
	'''
	A library contains many books in an orderly fashion.
	'''
	def __init__(self):
		self.books = {}

	def add(self, Book):
		self.books[Book.acronym] = Book

	def write_to_file(self, level = 0):
		# grab all the books
		for book_title in self.books:
			Book = self.books[book_title]
			# make a folder
			if not os.path.exists(f'./spells/{Book.acronym}/'):
				os.makedirs(f'./spells/{Book.acronym}/')
			# grab all the spells
			for spell_name in Book.spells:
				Spell = Book.spells[spell_name]
				filepath = f'./spells/{Spell.slug}.md'
				if level == None or level == Spell.level:
					with open(filepath, 'w+') as file:
						file.write(Spell.markdown)
