from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class anl(Page):
	def is_displayed(self):
		return self.round_number==1
class Intro(Page):
	form_model=models.Player
	form_fields=["guess","che","inv","abcd"]

	def che_error_message(self,value):
		if not (value==1):
			return 'Bitte geben Sie noch Ihre Einschätzung zu 1.) ab und klicken Sie auf "Einschätzung abgeben".'

	def inv_error_message(self,value):
		value="".join(value.split("."))
		value=value.split(",")[0]
		value=value.strip('euro')
		value=value.strip('€')
		value=value.strip('Euro')
		value=value.strip(' ')
		value1=value.strip('EUR')
		try: 
			str(type(int(value1)))=="<class 'int'>"
		except ValueError:
			return 'Bitte verwenden Sie ausschließlich Zahlen bei Ihrer Eingabe.'
		

	def before_next_page(self):
		self.player.strinv()
	def is_displayed(self):
		return self.round_number==1
	

class dceques(Page):
	form_model=models.Player
	form_fields=["submitted_answer1","submitted_answer2","submitted_answer3"]

	def vars_for_template(self):
		return self.player.vars_for_template()

class koinv(Page):
	def is_displayed(self):
		return self.round_number==6

class add(Page):
	form_model=models.Player
	form_fields=["add1","add2","add3","add4","add5","add6"]

	def vars_for_template(self):
		return self.player.vars_for_template()
	def is_displayed(self):
		return self.round_number==6
	
		

page_sequence = [
	anl,
	Intro,
	dceques,
	koinv,
	add
]
