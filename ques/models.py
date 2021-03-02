from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
from django import forms

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'ques'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	tp1 = models.IntegerField(blank=True)
	tp2 = models.IntegerField(blank=True)
	tp3 = models.IntegerField(blank=True)
	tp4 = models.IntegerField(blank=True)
	tp5 = models.IntegerField(blank=True)
	r1 = models.IntegerField(blank=True)
	r2 = models.IntegerField(blank=True)
	r3 = models.IntegerField(blank=True)
	r4 = models.IntegerField(blank=True)
	r5 = models.IntegerField(blank=True)

	exit = models.PositiveIntegerField(
		choices=[
			[1, "1 Jahr"], 
			[2, "2 Jahre"],
			[3, "3 Jahre"],
			[4, "4 Jahre"],
			[5, "5 Jahre"],
			[6, "6 Jahre"],
			[7, "7 Jahre"],
			[8, "8 Jahre"],
			[9, "9 Jahre"],
			[10, "10 Jahre"],
			[11, "11 Jahre"],
			[12, "12 Jahre"],
			[13, "13 Jahre"],
			[14, "14 Jahre"],
			[15, "15 Jahre"],
			[16, ">15 Jahre"],
		 ],blank=True)


	many = models.IntegerField(
		choices=[
			[0, "0"],
			[1, "1"], 
			[2, "2"],
			[3, "3"],
			[4, "4"],
			[5, "5"],
			[6, "6"],
			[7, "7"],
			[8, "8"],
			[9, "9"],
			[10, "10"],
			[11, "<10"],
			],blank=True)
	many2 = models.StringField(blank=True)


	when = models.IntegerField(
		choices=[
			[2, "vor weniger als 3 Monaten"], 
			[3, "vor weniger als 6 Monaten"], 
			[4, "vor weniger als 1 Jahr"], 
			[5, "vor weniger als 2 Jahren"],
			[6, "vor weniger als 3 Jahren"],
			[7, "vor weniger als 4 Jahren"],
			[8, "vor weniger als 5 Jahren"],
			[9, ">5 Jahren"],

		 ],blank=True)

	branch = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	patent = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	fisup = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	phase1 = models.IntegerField(initial=0,blank=True)
	phase2 = models.IntegerField(initial=0,blank=True)
	phase3 = models.IntegerField(initial=0,blank=True)

	influ1 = models.IntegerField(blank=True)
	influ2 = models.IntegerField(blank=True)

	invest1 = models.PositiveIntegerField(
		choices=[
			[1, "alleine"], 
			[2, "mit anderen Investoren"],
		 ],
		 widget=widgets.RadioSelect,blank=True)

	rank1 = models.StringField(blank=True)
	rank2 = models.StringField(blank=True)
	rank3 = models.StringField(blank=True)

	guess3 = models.IntegerField(blank=True)
	guess4 = models.IntegerField(blank=True)
	beitrag = models.IntegerField(blank=True)
	flach = models.IntegerField(blank=True)
	res = models.IntegerField(blank=True)
	emi = models.IntegerField(blank=True)
	demand = models.IntegerField(blank=True)
	grepro = models.IntegerField(blank=True)
	resp= models.IntegerField(blank=True)

	indust1 = models.IntegerField(blank=True, initial=0)
	indust2 = models.IntegerField(blank=True, initial=0)
	indust3 = models.IntegerField(blank=True, initial=0)
	indust4 = models.IntegerField(blank=True, initial=0)
	indust5 = models.IntegerField(blank=True, initial=0)
	indust6 = models.IntegerField(blank=True, initial=0)
	indust7 = models.IntegerField(blank=True, initial=0)
	indust8 = models.IntegerField(blank=True, initial=0)
	indust9 = models.IntegerField(blank=True, initial=0)
	indust10 = models.IntegerField(blank=True, initial=0)
	indust11 = models.IntegerField(blank=True, initial=0)
	indust12 = models.IntegerField(blank=True, initial=0)
	andereind = models.StringField(blank=True,label="")
	altru2 = models.StringField(blank=True)

	# Deserving1 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)


	# Deserving2 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)

	# volun = models.IntegerField(
	# 	choices=[
	# 		[1, '0 gar nicht risikobereit'], 
	# 		[2, '1'],
	# 		[3, '2'],
	# 		[4, "3"],
	# 		[5, "4"],
	# 		[6, "5"],
	# 		[7, "6"],
	# 		[8, "7"],
	# 		[9, "8"],
	# 		[10, "9"],
	# 		[11, "10 sehr risikobereit"]
	# 	 ],
	# 	 blank=True,
	# 	 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
	# 	 widget=widgets.RadioSelectHorizontal)

	recall1 = models.PositiveIntegerField(
		blank=True,
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"]
		 ],
		 widget=widgets.RadioSelect)

	recall2 = models.PositiveIntegerField(
		blank=True,
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"]
		 ],
		 widget=widgets.RadioSelect)

	Realization = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env3 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env4 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env5 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env6 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env7 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env8 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	Env9 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect,blank=True)

	sd1 = models.IntegerField(blank=True)
	sd2 = models.IntegerField(blank=True)
	sd3 = models.IntegerField(blank=True)
	sd4 = models.IntegerField(blank=True)
	sd5 = models.IntegerField(blank=True)
	sd6 = models.IntegerField(blank=True)
	sd7 = models.IntegerField(blank=True)
	sd8 = models.IntegerField(blank=True)
	sd9 = models.IntegerField(blank=True)
	sd10 = models.IntegerField(blank=True)


	wg = models.IntegerField(blank=True)
	
	member0=models.IntegerField(blank=True, initial=0)
	member1=models.IntegerField(blank=True, initial=0)
	member2=models.IntegerField(blank=True, initial=0)

	# Deontologist1 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)

	# Deontologist2 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)

	# Deontologist3 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)

	# Deontologist4 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, "Stimme überhaupt nicht zu"], 
	# 		[2, "Stimme eher nicht zu"],
	# 		[3, "Bin unentschieden"],
	# 		[4, "Stimme eher zu"],
	# 		[5, "Stimme voll und ganz zu"],
	# 		[6, "Keine Angabe"]
	# 	 ],
	# 	 widget=widgets.RadioSelect,blank=True)


	risk = models.IntegerField(
		choices=[
			[1, '0 gar nicht risikobereit'], 
			[2, '1'],
			[3, '2'],
			[4, "3"],
			[5, "4"],
			[6, "5"],
			[7, "6"],
			[8, "7"],
			[9, "8"],
			[10, "9"],
			[11, "10 sehr risikobereit"]
		 ],
		 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
		 widget=widgets.RadioSelectHorizontal,blank=True)


	# exhaust1 = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, 'Sehr anstrengend'], 
	# 		[2, 'Eher anstrengend'],
	# 		[3, 'Wenig anstrengend'],
	# 		[4, "Überhaupt nicht anstrengend"],
	# 		[5, "Keine Angabe"]         
	# 	 ],
	# 	 label="Wie anstrengend empfanden Sie die Dekodierungsaufgabe in Teil 1?",
	# 	 widget=widgets.RadioSelect,blank=True)

	# tippen = models.StringField(
	# 	choices=['Sehr vertraut', 'Vertraut', 'Eher nicht vertraut', 'Gar nicht vertraut','Keine Angabe'],
	# 	label="Wie schnell können Sie einen Text per Tastatur eingeben?",
	# 	widget=widgets.RadioSelect,blank=True)

	tenf = models.StringField(
		choices=['Ja', 'Nein', 'keine Angabe'],
		label="Beherrschen Sie das Zehnfinger-Schreibsystem?",
		widget=widgets.RadioSelect,blank=True)

	gender = models.CharField(
		choices=[' weiblich', ' männlich', ' divers', ' keine Angabe'],
		label="Bitte geben Sie ihr Geschlecht an.",
		widget=widgets.RadioSelectHorizontal,blank=True)

	age = models.PositiveIntegerField(label="Wie alt sind Sie?",blank=True)

	# nationality = models.CharField(label="Was ist Ihre Staatsangehörigkeit?",blank=True)

	# uni = models.CharField(label="Welche Muttersprache(n) sprechen Sie?",blank=True)

	# party = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, 'CDU/CSU'], 
	# 		[2, 'SPD'],
	# 		[3, 'AfD'],
	# 		[4, "FDP"],
	# 		[5, "Bündnis 90/Die Grünen"],
	# 		[6, "Die Linke"],
	# 		[7, "andere"],
	# 		[8, "Keine Angabe"]
	# 	 ],
	# 	 label="Welche Partei würden Sie wählen, wenn am nächsten Sonntag Bundestagswahl wäre?",
	# 	 widget=widgets.RadioSelect,blank=True)

	# education = models.PositiveIntegerField(
	# 	choices=[
	# 		[1, 'Keinen Schulabschluss'], 
	# 		[2, 'Hauptschulabschluss'],
	# 		[3, 'Mittlere Reife'],
	# 		[4, "Abitur"],
	# 		[5, "Abgeschlossene Ausbildung"],
	# 		[6, "Univeritäts- / Fachhochschulabschluss"],
	# 		[7, "Keine Angabe"]
	# 	 ],
	# 	 label="Was ist Ihr höchster Bildungsabschluss?",
	# 	 widget=widgets.RadioSelect,blank=True)

	# income = models.IntegerField(blank=True)


	# co1 = models.IntegerField(blank=True)
	# co2 = models.IntegerField(blank=True)
	# co31 = models.IntegerField(blank=True, initial=1)
	# co32 = models.IntegerField(blank=True, initial=1)
	# co33 = models.IntegerField(blank=True, initial=1)
	# co41 = models.IntegerField(blank=True, initial=1)
	# co42 = models.IntegerField(blank=True, initial=1)
	# co43 = models.IntegerField(blank=True, initial=1)
	# co5 = models.IntegerField(blank=True)
	# co61 = models.IntegerField(blank=True, initial=1)
	# co62 = models.IntegerField(blank=True, initial=1)
	# co63 = models.IntegerField(blank=True, initial=1)
	# co64 = models.IntegerField(blank=True, initial=1)

	mail = models.StringField(blank=True)