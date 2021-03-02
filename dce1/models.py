from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import csv
import pandas as pd
import re

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'dce1'
	num_rounds = 6
	players_per_group = None
	

#		df1 = pd.read_csv('dce1/alt1lte1.csv', delimiter=',')
#		sets1 = [list(x) for x in df1.values]
#		df2 = pd.read_csv('dce1/alt2lte1.csv', delimiter=',')
#		sets2 = [list(x) for x in df2.values]
#	else:
#		df1 = pd.read_csv('dce1/alt3lte1.csv', delimiter=',')
#		sets1 = [list(x) for x in df1.values]
#		df2 = pd.read_csv('dce1/alt4lte1.csv', delimiter=',')
#		sets2 = [list(x) for x in df2.values]
#
#	dfl1 = pd.read_csv('dce1/alt1large.csv', delimiter=',')
#	setsl1 = [list(x) for x in dfl1.values]
#	dfl2 = pd.read_csv('dce1/alt2large.csv', delimiter=',')
#	setsl2 = [list(x) for x in dfl2.values]


	


class Subsession(BaseSubsession):
	def creating_session(self):
		for p in self.get_players():
					
			if self.round_number==1:
				p.treat=random.choice([0,1])
				p.participant.vars["treat"]=p.treat

				li=[1,2,3,4,5,6]
				random.shuffle(li)
				p.participant.vars['one']=li.pop(0)
				p.one=p.participant.vars['one']
				p.participant.vars['two']=li.pop(0)
				p.two=p.participant.vars['two']
				p.participant.vars['three']=li.pop(0)
				p.three=p.participant.vars['three']
				p.participant.vars['four']=li.pop(0)
				p.four=p.participant.vars['four']
				p.participant.vars['five']=li.pop(0)
				p.five=p.participant.vars['five']
				p.participant.vars['six']=li.pop(0)
				p.six=p.participant.vars['six']


				li2=[1,3,4,5]
				random.shuffle(li2)
				li2.append(2)
				p.participant.vars['row1']=li2.pop(0)
				p.row1=p.participant.vars['row1']
				p.participant.vars['row2']=li2.pop(0)
				p.row2=p.participant.vars['row2']
				p.participant.vars['row3']=li2.pop(0)
				p.row3=p.participant.vars['row3']
				p.participant.vars['row4']=li2.pop(0)
				p.row4=p.participant.vars['row4']
				p.participant.vars['row5']=li2.pop(0)
				p.row5=p.participant.vars['row5']

				li3=[1,2,3]
				random.shuffle(li3)
				p.participant.vars['column1']=li3.pop(0)
				p.column1=p.participant.vars['column1']
				p.participant.vars['column2']=li3.pop(0)
				p.column2=p.participant.vars['column2']
				p.participant.vars['column3']=li3.pop(0)
				p.column3=p.participant.vars['column3']


			p.one=p.participant.vars['one']
			p.two=p.participant.vars['two']
			p.three=p.participant.vars['three']
			p.four=p.participant.vars['four']
			p.five=p.participant.vars['five']
			p.six=p.participant.vars['six']

			p.row1=p.participant.vars['row1']
			p.row2=p.participant.vars['row2']
			p.row3=p.participant.vars['row3']
			p.row4=p.participant.vars['row4']
			p.row5=p.participant.vars['row5']

			p.column1=p.participant.vars['column1']
			p.column2=p.participant.vars['column2']
			p.column3=p.participant.vars['column3']
			p.treat=p.participant.vars['treat']


		df = pd.read_csv('dce1/choiceset.csv', delimiter=',')
		df1 = df[df['block'] == 1]
		df2 = df[df['block'] == 2]
		df3 = df[df['block'] == 3]
		df1 = df1.drop(['choice_set','alt','block'], 1)
		df2 = df2.drop(['choice_set','alt','block'], 1)
		df3 = df3.drop(['choice_set','alt','block'], 1)
		for p in self.get_players():
			if self.round_number==1:
				r=random.choice([1,2,3])
				p.block=r
				p.participant.vars["block"]=p.block
			p.block=p.in_round(1).block
			p.participant.vars["block"]=p.block
			r=p.block
			if r==1:
			    sets1 = [list(x) for x in df1.values]
			elif r==2:
			    sets1 = [list(x) for x in df2.values]
			else:
			    sets1 = [list(x) for x in df3.values]

			set1a1=[]
			set1a2=[]
			set1a3=[]
			for i in range(int(len(sets1)/3)):
			    set1a1.append(sets1.pop(0))
			    set1a2.append(sets1.pop(0))
			    set1a3.append(sets1.pop(0))

			self.session.vars['questions1']=set1a1
			self.session.vars['questions2']=set1a2
			self.session.vars['questions3']=set1a3

		
			set_data1 = p.current_set1()
			p.set_attr11 = "Keine Angabe" if set_data1[0]==0 else "ökologischer Beitrag" if set_data1[0]==1 else "ökologischer Beitrag"
			p.set_attr111 = "" if set_data1[0]==0 else "(ohne messb. Nachweis)" if set_data1[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr12 = str(set_data1[1])
			p.set_attr13 = "1 Jahr" if set_data1[2]==1 else "2 Jahren" if set_data1[2]==3 else "3 Jahren"
			p.set_attr14 = str(set_data1[3])
			p.set_attr15 = "inkrementelle Innovation" if set_data1[4]==0 else "Durchbruchsinnovation" 

			set_data2 = p.current_set2()
			p.set_attr21 = "Keine Angabe" if set_data2[0]==0 else "ökologischer Beitrag" if set_data2[0]==1 else "ökologischer Beitrag"
			p.set_attr211 = "" if set_data2[0]==0 else "(ohne messb. Nachweis)" if set_data2[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr22 = str(set_data2[1])
			p.set_attr23 = "1 Jahr" if set_data2[2]==1 else "2 Jahren" if set_data2[2]==3 else "3 Jahren"
			p.set_attr24 = str(set_data2[3])
			p.set_attr25 = "inkrementelle Innovation" if set_data2[4]==0 else "Durchbruchsinnovation" 

			set_data3 = p.current_set3()
			p.set_attr31 = "Keine Angabe" if set_data3[0]==0 else "ökologischer Beitrag" if set_data3[0]==1 else "ökologischer Beitrag"
			p.set_attr311 = "" if set_data3[0]==0 else "(ohne messb. Nachweis)" if set_data3[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr32 = str(set_data3[1])
			p.set_attr33 =  "1 Jahr" if set_data3[2]==1 else "2 Jahren" if set_data3[2]==3 else "3 Jahren"
			p.set_attr34 = str(set_data3[3])
			p.set_attr35 = "inkrementelle Innovation" if set_data3[4]==0 else "Durchbruchsinnovation" 

			set_data4 = p.add_set1()
			p.set_attr41 = "Keine Angabe" if set_data4[0]==0 else "ökologischer Beitrag" if set_data4[0]==1 else "ökologischer Beitrag"
			p.set_attr411 = "" if set_data4[0]==0 else "(ohne messb. Nachweis)" if set_data4[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr42 = str(set_data4[1])
			p.set_attr43 =  "1 Jahr" if set_data4[2]==1 else "2 Jahren" if set_data4[2]==3 else "3 Jahren"
			p.set_attr44 = str(set_data4[3])
			p.set_attr45 = "inkrementelle Innovation" if set_data4[4]==0 else "Durchbruchsinnovation"

			set_data5 = p.add_set2()
			p.set_attr51 = "Keine Angabe" if set_data5[0]==0 else "ökologischer Beitrag" if set_data5[0]==1 else "ökologischer Beitrag"
			p.set_attr511 = "" if set_data5[0]==0 else "(ohne messb. Nachweis)" if set_data5[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr52 = str(set_data5[1])
			p.set_attr53 = "1 Jahr" if set_data5[2]==1 else "2 Jahren" if set_data5[2]==3 else "3 Jahren"
			p.set_attr54 = str(set_data5[3])
			p.set_attr55 = "inkrementelle Innovation" if set_data5[4]==0 else "Durchbruchsinnovation"

			set_data6 = p.add_set3()
			p.set_attr61 = "Keine Angabe" if set_data6[0]==0 else "ökologischer Beitrag" if set_data6[0]==1 else "ökologischer Beitrag"
			p.set_attr611 = "" if set_data6[0]==0 else "(ohne messb. Nachweis)" if set_data6[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr62 = str(set_data6[1])
			p.set_attr63 =  "1 Jahr" if set_data6[2]==1 else "2 Jahren" if set_data6[2]==3 else "3 Jahren"
			p.set_attr64 = str(set_data6[3])
			p.set_attr65 = "inkrementelle Innovation" if set_data6[4]==0 else "Durchbruchsinnovation"

			set_data7 = p.add_set4()
			p.set_attr71 = "Keine Angabe" if set_data7[0]==0 else "ökologischer Beitrag" if set_data7[0]==1 else "ökologischer Beitrag"
			p.set_attr711 = "" if set_data7[0]==0 else "(ohne messb. Nachweis)" if set_data7[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr72 = str(set_data7[1])
			p.set_attr73 =  "1 Jahr" if set_data7[2]==1 else "2 Jahren" if set_data7[2]==3 else "3 Jahren"
			p.set_attr74 = str(set_data7[3])
			p.set_attr75 = "inkrementelle Innovation" if set_data7[4]==0 else "Durchbruchsinnovation"

			set_data8 = p.add_set5()
			p.set_attr81 = "Keine Angabe" if set_data8[0]==0 else "ökologischer Beitrag" if set_data8[0]==1 else "ökologischer Beitrag"
			p.set_attr811 = "" if set_data8[0]==0 else "(ohne messb. Nachweis)" if set_data8[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr82 = str(set_data8[1])
			p.set_attr83 =  "1 Jahr" if set_data8[2]==1 else "2 Jahren" if set_data8[2]==3 else "3 Jahren"
			p.set_attr84 = str(set_data8[3])
			p.set_attr85 = "inkrementelle Innovation" if set_data8[4]==0 else "Durchbruchsinnovation"

			set_data9 = p.add_set6()
			p.set_attr91 = "Keine Angabe" if set_data9[0]==0 else "ökologischer Beitrag" if set_data9[0]==1 else "ökologischer Beitrag"
			p.set_attr911 = "" if set_data9[0]==0 else "(ohne messb. Nachweis)" if set_data9[0]==1 else "(mit messbaren Nachweis)"
			p.set_attr92 = str(set_data9[1])
			p.set_attr93 =  "1 Jahr" if set_data9[2]==1 else "2 Jahren" if set_data9[2]==3 else "3 Jahren"
			p.set_attr94 = str(set_data9[3])
			p.set_attr95 = "inkrementelle Innovation" if set_data9[4]==0 else "Durchbruchsinnovation"








		




class Group(BaseGroup):
	pass


class Player(BasePlayer):
	block=models.IntegerField()
	set_id1 = models.PositiveIntegerField()
	set_attr11 = models.StringField()
	set_attr111 = models.StringField()
	set_attr12 = models.StringField()
	set_attr13 = models.StringField()
	set_attr14 = models.StringField()
	set_attr15 = models.StringField()

	set_id2 = models.PositiveIntegerField()
	set_attr21 = models.StringField()
	set_attr211 = models.StringField()
	set_attr22 = models.StringField()
	set_attr23 = models.StringField()
	set_attr24 = models.StringField()
	set_attr25 = models.StringField()

	set_id3 = models.PositiveIntegerField()
	set_attr31 = models.StringField()
	set_attr311 = models.StringField()
	set_attr32 = models.StringField()
	set_attr33 = models.StringField()
	set_attr34 = models.StringField()
	set_attr35 = models.StringField()

	set_id4 = models.PositiveIntegerField()
	set_attr41 = models.StringField()
	set_attr411 = models.StringField()
	set_attr42 = models.StringField()
	set_attr43 = models.StringField()
	set_attr44 = models.StringField()
	set_attr45 = models.StringField()

	set_id5 = models.PositiveIntegerField()
	set_attr51 = models.StringField()
	set_attr511 = models.StringField()
	set_attr52 = models.StringField()
	set_attr53 = models.StringField()
	set_attr54 = models.StringField()
	set_attr55 = models.StringField()

	set_id6 = models.PositiveIntegerField()
	set_attr61 = models.StringField()
	set_attr611 = models.StringField()
	set_attr62 = models.StringField()
	set_attr63 = models.StringField()
	set_attr64 = models.StringField()
	set_attr65 = models.StringField()

	set_id7 = models.PositiveIntegerField()
	set_attr71 = models.StringField()
	set_attr711 = models.StringField()
	set_attr72 = models.StringField()
	set_attr73 = models.StringField()
	set_attr74 = models.StringField()
	set_attr75 = models.StringField()

	set_id8 = models.PositiveIntegerField()
	set_attr81 = models.StringField()
	set_attr811 = models.StringField()
	set_attr82 = models.StringField()
	set_attr83 = models.StringField()
	set_attr84 = models.StringField()
	set_attr85 = models.StringField()

	set_id9 = models.PositiveIntegerField()
	set_attr91 = models.StringField()
	set_attr911 = models.StringField()
	set_attr92 = models.StringField()
	set_attr93 = models.StringField()
	set_attr94 = models.StringField()
	set_attr95 = models.StringField()


	guess = models.FloatField()
	che = models.IntegerField()
	sec = models.IntegerField()
	inv = models.StringField(widget=widgets.TextInput(
                           attrs={'class': "inp"}))
	inv1 = models.IntegerField(initial=0)
	treat = models.IntegerField()
	abcd = models.IntegerField(initial=0)

	submitted_answer1 = models.IntegerField()
	submitted_answer2 = models.IntegerField()
	submitted_answer3 = models.IntegerField()

	add1 = models.IntegerField()
	add2 = models.IntegerField()
	add3 = models.IntegerField()
	add4 = models.IntegerField()
	add5 = models.IntegerField()
	add6 = models.IntegerField()

	one = models.IntegerField()
	two = models.IntegerField()
	three = models.IntegerField()
	four = models.IntegerField()
	five = models.IntegerField()
	six = models.IntegerField()

	row1 = models.IntegerField()
	row2 = models.IntegerField()
	row3 = models.IntegerField()
	row4 = models.IntegerField()
	row5 = models.IntegerField()

	column1 = models.IntegerField()
	column2 = models.IntegerField()
	column3 = models.IntegerField()


 #   correct_answers=models.IntegerField(
  #  	default=0
   # 	)

	def current_set1(self):
		if self.round_number==1:
			return self.session.vars['questions1'][(self.participant.vars["one"]-1)]
		elif self.round_number==2:
			return self.session.vars['questions1'][(self.participant.vars["two"]-1)]
		elif self.round_number==3:
			return self.session.vars['questions1'][(self.participant.vars["three"]-1)]
		elif self.round_number==4:
			return self.session.vars['questions1'][(self.participant.vars["four"]-1)]
		elif self.round_number==5:
			return self.session.vars['questions1'][(self.participant.vars["five"]-1)]
		elif self.round_number==6:
			return self.session.vars['questions1'][(self.participant.vars["six"]-1)]


	def current_set2(self):
		if self.round_number==1:
			return self.session.vars['questions2'][(self.participant.vars["one"]-1)]
		elif self.round_number==2:
			return self.session.vars['questions2'][(self.participant.vars["two"]-1)]
		elif self.round_number==3:
			return self.session.vars['questions2'][(self.participant.vars["three"]-1)]
		elif self.round_number==4:
			return self.session.vars['questions2'][(self.participant.vars["four"]-1)]
		elif self.round_number==5:
			return self.session.vars['questions2'][(self.participant.vars["five"]-1)]
		elif self.round_number==6:
			return self.session.vars['questions2'][(self.participant.vars["six"]-1)]

	def current_set3(self):
		if self.round_number==1:
			return self.session.vars['questions3'][(self.participant.vars["one"]-1)]
		elif self.round_number==2:
			return self.session.vars['questions3'][(self.participant.vars["two"]-1)]
		elif self.round_number==3:
			return self.session.vars['questions3'][(self.participant.vars["three"]-1)]
		elif self.round_number==4:
			return self.session.vars['questions3'][(self.participant.vars["four"]-1)]
		elif self.round_number==5:
			return self.session.vars['questions3'][(self.participant.vars["five"]-1)]
		elif self.round_number==6:
			return self.session.vars['questions3'][(self.participant.vars["six"]-1)]

	def add_set1(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions1'][1]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions1'][1]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions1'][5]

	def add_set2(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions2'][1]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions2'][1]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions2'][5]

	def add_set3(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions3'][1]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions3'][1]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions3'][5]

	def add_set4(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions1'][3]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions1'][4]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions1'][0]

	def add_set5(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions2'][3]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions2'][4]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions2'][0]

	def add_set6(self):
		if self.participant.vars["block"]==1:
			return self.session.vars['questions3'][3]
		elif self.participant.vars["block"]==2:
			return self.session.vars['questions3'][4]
		elif self.participant.vars["block"]==3:
			return self.session.vars['questions3'][0]



	def strinv(self):
		self.inv="".join(self.inv.split("."))
		self.inv=self.inv.split(",")[0]
		self.inv=self.inv.strip('euro')
		self.inv=self.inv.strip('€')
		self.inv=self.inv.strip('Euro')
		self.inv=self.inv.strip(' ')
		self.inv1=int(self.inv.strip('EUR'))
		






	def vars_for_template(self):
		return {
		'attr11': self.set_attr11,
		'attr111': self.set_attr111,
		'attr12': self.set_attr12,
		'attr13': self.set_attr13,
		'attr14': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr14)/100)*self.in_round(1).inv1,-3)))),
		'attr15': self.set_attr15,
		'attr21': self.set_attr21,
		'attr211': self.set_attr211,
		'attr22': self.set_attr22,
		'attr23': self.set_attr23,
		'attr24': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr24)/100)*self.in_round(1).inv1,-3)))),
		'attr25': self.set_attr25,
		'attr31': self.set_attr31,
		'attr311': self.set_attr311,
		'attr32': self.set_attr32,
		'attr33': self.set_attr33,
		'attr34': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr34)/100)*self.in_round(1).inv1,-3)))),
		'attr35': self.set_attr35,
		'attr41': self.set_attr41,
		'attr411': self.set_attr411,
		'attr42': self.set_attr42,
		'attr43': self.set_attr43,
		'attr44': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr44)/100)*self.in_round(1).inv1,-3)))),
		'attr441': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr44)/100)*self.in_round(1).inv1/2,-3)))),
		'attr45': self.set_attr45,
		'attr51': self.set_attr51,
		'attr511': self.set_attr511,
		'attr52': self.set_attr52,
		'attr53': self.set_attr53,
		'attr54': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr54)/100)*self.in_round(1).inv1,-3)))),
		'attr541': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr54)/100)*self.in_round(1).inv1/2,-3)))),
		'attr55': self.set_attr55,
		'attr61': self.set_attr61,
		'attr611': self.set_attr611,
		'attr62': self.set_attr62,
		'attr63': self.set_attr63,
		'attr64': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr64)/100)*self.in_round(1).inv1,-3)))),
		'attr641': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr64)/100)*self.in_round(1).inv1/2,-3)))),
		'attr65': self.set_attr65,
		'attr71': self.set_attr71,
		'attr711': self.set_attr711,
		'attr72': self.set_attr72,
		'attr73': self.set_attr73,
		'attr74': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr74)/100)*self.in_round(1).inv1,-3)))),
		'attr741': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr74)/100)*self.in_round(1).inv1/2,-3)))),
		'attr75': self.set_attr75,
		'attr81': self.set_attr81,
		'attr811': self.set_attr811,
		'attr82': self.set_attr82,
		'attr83': self.set_attr83,
		'attr84': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr84)/100)*self.in_round(1).inv1,-3)))),
		'attr841': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr84)/100)*self.in_round(1).inv1/2,-3)))),
		'attr85': self.set_attr85,
		'attr91': self.set_attr91,
		'attr911': self.set_attr911,
		'attr92': self.set_attr92,
		'attr93': self.set_attr93,
		'attr94': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr94)/100)*self.in_round(1).inv1,-3)))),
		'attr941': re.sub(r'(?<!^)(?=(\d{3})+$)', r'.', str(round(round((int(self.set_attr94)/100)*self.in_round(1).inv1/2,-3)))),
		'attr95': self.set_attr95,
		}



#    def count(self):
 #   	if self.submitted_answer == self.solution:
  #  		self.correct_answers=self.correct_answers.in_previous_rounds() + 1


