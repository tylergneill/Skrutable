from skrutable.scansion import Scanner
from skrutable.meter_identification import MeterIdentifier
from skrutable.meter_identification import VerseTester
import inspect

def test_test_as_anuzwuB():
	S = Scanner()
	input_string = """yadA yadA hi Darmasya
glAnirBavati BArata
aByutTAnamaDarmasya
tadAtmAnaM sfjAmyaham"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.test_as_anuzwuB(V)
	output = V.meter_label
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "anuṣṭubh (ab: pathyā, cd: pathyā)"
	assert output == expected_output

def test_identify_anuzwuB_split():
	MI = MeterIdentifier()
	input_string = """yadA yadA hi Darmasya
glAnirBavati BArata
aByutTAnamaDarmasya
tadAtmAnaM sfjAmyaham"""
	object_result = MI.identify_meter(input_string, from_scheme='SLP', resplit_option='resplit_hard')
	output = object_result.meter_label
	output = output[:8]
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "anuṣṭubh"
	assert output == expected_output

def test_count_pAdasamatva():
	S = Scanner()
	input_string = """sampūrṇakumbho na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.count_pAdasamatva(V)
	output = VT.pAdasamatva_count # int
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 4
	assert output == expected_output

def test_test_as_upajAti():
	S = Scanner()
	input_string = """kolAhale kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	output = VT.test_as_upajAti(V)
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "upajāti"
	assert output[:7] == expected_output

def test_identify_meter_upajAti():
	MI = MeterIdentifier()
	input_string = """kolAhale kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	object_result = MI.identify_meter(input_string, from_scheme='SLP', resplit_option='resplit_hard')
	output = object_result.summarize()
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "upajāti"

def test_identify_meter_Darmakzetre():
	MI = MeterIdentifier()
	input_string = """dharmakṣetre kurukṣetre samavetā yuyutsavaḥ /
māmakāḥ pāṇḍavāś caiva kim akurvata sañjaya //"""
	object_result = MI.identify_meter(input_string, from_scheme='IAST', resplit_option='resplit_hard')
	output = object_result.summarize()
	truncated_output = object_result.meter_label[:8]
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "anuṣṭubh"
	assert truncated_output == expected_output

def test_evaluate_samavftta_sampUrRakumBo():
	S = Scanner()
	input_string = """sampūrṇakumbho na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.count_pAdasamatva(V)
	VT.evaluate_samavftta(V)
	output = V.meter_label[:10]
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = "indravajrā"
	assert output == expected_output

def test_evaluate_samavftta_sampUrRakumBo_3():
	S = Scanner()
	# note "kumbha" instead of "kumbho"
	input_string = """sampūrṇakumbha na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.count_pAdasamatva(V)
	VT.evaluate_samavftta(V)
	output = V.identification_score
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 7
	assert output == expected_output

def test_evaluate_upajAti_kolAhale():
	S = Scanner()
	input_string = """kolAhale kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.evaluate_upajAti(V)
	output = V.identification_score
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 8
	assert output == expected_output

def test_evaluate_upajAti_kolAhala():
	S = Scanner()
	# note "kolAhala" is still triṣṭubh, just not the expected one
	input_string = """kolAhala kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.count_pAdasamatva(V)
	VT.evaluate_upajAti(V)
	output = V.identification_score
	other_output = V.meter_label
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(other_output) + '\n\n')
	expected_output = 8
	assert output == expected_output

def test_evaluate_upajAti_kolAha():
	S = Scanner()
	# note hypometrical "kolAha" instead of "kolAhale"
	input_string = """kolAha kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.count_pAdasamatva(V)
	VT.evaluate_upajAti(V)
	output = V.identification_score
	other_output = V.meter_label
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 6
	assert output == expected_output

def test_test_as_samavftta_etc_kolAhale():
	S = Scanner()
	input_string = """kolAhale kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.test_as_samavftta_etc(V)
	output = V.identification_score
	# curr_func = inspect.stack()[0][3]
	# print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 8
	assert output == expected_output

def test_test_as_samavftta_etc_sampUrRakumBo_3():
	S = Scanner()
	# note "kumbha" instead of "kumbho"
	input_string = """sampūrṇakumbha na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.test_as_samavftta_etc(V)
	output = V.identification_score
	curr_func = inspect.stack()[0][3]
	print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 8 # because within triṣṭubh
	assert output == expected_output

def test_test_as_samavftta_etc_kudeSam_3():
	S = Scanner()
	# note "AsAdyā" instead of "AsAdya"
	input_string = """kudeSamAsAdyā kuto 'rTasaYcayaH
kuputramAsAdya kuto jalAYjaliH
kugehinIM prApya kuto gfhe suKam
kuSizyamaDyApayataH kuto yaSaH"""
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	VT.test_as_samavftta_etc(V)
	output = V.identification_score
	curr_func = inspect.stack()[0][3]
	print("\n\n%s OUTPUT:\n" % curr_func + str(output) + '\n\n')
	expected_output = 7 # because not within triṣṭubh
	assert output == expected_output

def test_combine_results_kolAhale():
	S = Scanner()
	input_string = """kolAhale kAkakulasya jAte
virAjate kokilakUjitaM kim
parasparaM saMvadatAM KalAnAM
mOnaM viDeyaM satataM suDIBiH""" # id_score == 8
	V = S.scan(input_string, from_scheme='SLP')
	VT = VerseTester()
	# VT.count_pAdasamatva(V)
	VT.evaluate_upajAti(V)
	VT.combine_results(V, new_label='something better', new_score=9)
	output = V.identification_score
	other_output = V.meter_label
	curr_func = inspect.stack()[0][3]
	print("\n\n%s OUTPUT:\n" % curr_func + str(other_output) + '\n\n')
	expected_output = 9
	assert output == expected_output
