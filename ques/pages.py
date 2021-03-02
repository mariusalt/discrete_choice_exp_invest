from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random






class Questionnaire(Page):
	form_model=models.Player
	form_fields=['indust1','indust2','indust3','indust4','indust5','indust6','indust7','indust8','indust9','indust10','indust11','indust12','andereind','sd1','sd2','sd3','sd4','sd5','sd6','sd7','sd8','sd9','sd10','wg','member0','member1','member2','resp','beitrag','flach','res','emi','demand','grepro','guess3','guess4','rank1','rank2','rank3','exit','many','when','branch','patent','fisup','phase1','phase2','phase3',"r1","r2","r3","r4","r5","tp1","tp2","tp3","tp4","tp5",'invest1','altru2','Env1','Env2','Env3','Env4','Env5','Env6','Env7','Env8','Env9','risk', 'gender','age','influ1','influ2']#,'recall1','recall2','volun', 'uni','exhaust1']

class Thanks(Page):
	form_model=models.Player
	form_fields=['mail']
class Thanks1(Page):
	pass

page_sequence = [
	Questionnaire,
	Thanks,
	Thanks1
]

