from skrutable import phonemes
from skrutable import scheme_maps
from skrutable import scheme_detection
from skrutable import virAma_avoidance
import json
import re

# load config variables
config_data = open('config.json','r').read()
config = json.loads(config_data)
default_scheme_out = config["default_scheme_out"] # e.g. "IAST"
avoid_virAma_indic_scripts = config["avoid_virAma_indic_scripts"] # e.g. True
avoid_virAma_all_scripts = config["avoid_virAma_all_scripts"] # e.g. False

class Transliterator():

	def __init__(self, from_scheme=None, to_scheme=None):
		"""
		User-facing constructor.

		Manual specification of input and output schemes is optional here;
		a second chance is also provided when calling self.transliterate().
		"""

		self.contents = None
		self.scheme_in = from_scheme
		self.scheme_out = to_scheme


	def set_detected_scheme(self):
		"""Internal method."""
		self.scheme_in = scheme_detection.detect_scheme(self.contents)

	def map_replace(self, from_scheme, to_scheme):
		"""
		Internal method.

		Performs simple series of global regex replacements for transliteration.

		Result returned via updated self.contents.
		"""
		map = scheme_maps.by_name[from_scheme + '_' + to_scheme]
		for (char_in, char_out) in map:
			self.contents = self.contents.replace(char_in, char_out)


	def avoid_virAmas(self):
		"""
		Internal method.

		Performs simple series of global regex replacements for avoiding virāma.

		Result returned via updated self.contents.
		"""
		for pattern in virAma_avoidance.replacements:
			self.contents = re.sub(pattern, r'\1\2', self.contents)

	def linear_preprocessing(self, from_scheme, to_scheme):
		"""
		Internal method.

		Manages inherent short 'a' vowel and virāma for Indic schemes <<>> SLP,
		paying special attention to positions immediately after consonants.

		Also manages distinction between initial and mātrā vowel forms.

		Indic-SLP hybrid result returned via updated self.contents,
		to be further processed by simple map replacement.
		"""

		if from_scheme in scheme_maps.indic_schemes and to_scheme == 'SLP':
			char_to_ignore = scheme_maps.virAmas[from_scheme]
			char_to_add = 'a'
		elif from_scheme == 'SLP' and to_scheme in scheme_maps.indic_schemes:
			char_to_ignore = 'a'
			char_to_add = scheme_maps.virAmas[to_scheme]
		else: return

		content_in = self.contents

		content_out = '' # buffer to build as hybrid mix
		prev_char = ''
		for curr_char in content_in:

			if prev_char in phonemes.SLP_and_indic_consonants:
				# only need special action after consonants

				if curr_char == char_to_ignore:
					# from DEV: virāma
					# from SLP: 'a'
					pass

				elif curr_char not in phonemes.vowels_that_preempt_virAma:
					# from Indic: not vowel mātrā, therefore need 'a'
					# from SLP: not vowel, therefore need virāma
					# could also be other things (e.g. vowel, whitesp., punct.)
					content_out += char_to_add + curr_char

				elif curr_char in phonemes.SLP_vowels_with_mAtrAs:
					# from SLP: any vowel except 'a', therefore need mātrā
					content_out += phonemes.vowel_mAtrA_lookup[to_scheme][curr_char]

				elif curr_char in phonemes.vowels_that_preempt_virAma:
					# from Indic: vowel mātrā (only possibility left)
					content_out += curr_char

			else:
				# whenever preceding is non-consonant (e.g. vowel, whitesp., punct.)
				content_out += curr_char

			prev_char = curr_char

		if curr_char in phonemes.SLP_consonants:
			# from SLP: final virāma if needed
			content_out += scheme_maps.virAmas[to_scheme]

		self.contents = content_out # hybrid


	def transliterate(self, cntnts, from_scheme=None, to_scheme=None):
		"""
		User-facing method.

		Manual specification of input and output schemes is optional here,
		as it was when calling the constructor,
		but this is the last chance to do so,
		otherwise input scheme is auto-detected
		and fixed output scheme is chosen by default (see config.json).

		Executes transliteration via SLP,
		including linear preprocessing in case of DEV.

		Result returned via updated self.contents
		and also directly as string.
		"""

		self.contents = cntnts

		if from_scheme != None:
			self.scheme_in = from_scheme
		if self.scheme_in == None:
			self.set_detected_scheme() # default is automatic detection

		if to_scheme != None:
			self.scheme_out = to_scheme
		if self.scheme_out == None:
			self.scheme_out = default_scheme_out

		# transliterate first to hub scheme SLP
		self.linear_preprocessing(self.scheme_in, 'SLP')
		self.map_replace(self.scheme_in, 'SLP')

		# avoid undesirable virāmas specified in virāma_avoidance.py
		if 	(self.scheme_out in scheme_maps.indic_schemes
			and avoid_virAma_indic_scripts == True
			or avoid_virAma_all_scripts == True):
			self.avoid_virAmas()

		# then transliterate to desired scheme
		self.linear_preprocessing('SLP', self.scheme_out)
		self.map_replace('SLP', self.scheme_out)

		return self.contents
