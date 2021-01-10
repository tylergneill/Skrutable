from skrutable.scansion import Scanner
from skrutable.meter_identification import MeterIdentifier
from skrutable.meter_identification import VerseTester

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
	# print("\n\n test_test_as_anuzwuB OUTPUT: " + output + '\n\n')
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
	# print("\n\n test_identify_anuzwuB_split OUTPUT: " + output + '\n\n')
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
	# print("\n\n test_count_pAdasamatva OUTPUT: " + str(output) + '\n\n')
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
	# print("\n\n test_test_as_upajAti OUTPUT: " + output + '\n\n')
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
	# print("\n\n test_identify_meter_upajAti OUTPUT: " + output + '\n\n')
	expected_output = "upajāti"

def test_identify_meter_Darmakzetre():
	MI = MeterIdentifier()
	input_string = """dharmakṣetre kurukṣetre samavetā yuyutsavaḥ /
māmakāḥ pāṇḍavāś caiva kim akurvata sañjaya //"""
	object_result = MI.identify_meter(input_string, from_scheme='IAST', resplit_option='resplit_hard')
	output = object_result.summarize()
	# print("\n\ntest_identify_meter_Darmakzetre OUTPUT:\n" + output + '\n\n')
	expected_output = "upajāti"

def test_as_samavftta_and_or_upajAti_sampUrRakumBo():
	S = Scanner()
	input_string = """sampūrṇakumbho na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.test_as_samavftta_and_or_upajAti(V)
	output = V.meter_score # int
	print("\n\ntest_as_samavftta_and_or_upajAti_sampUrRakumBo OUTPUT:\n" + str(output) + '\n\n')
	print(VT.samavftta_result)
	expected_output = 9
	assert output == expected_output

def test_as_samavftta_and_or_upajAti_sampUrRakumBo_3():
	S = Scanner()
	input_string = """sampūrṇakumbha na karoti śabdam
ardho ghaṭo ghoṣamupaiti nūnam
vidvānkulīno na karoti garvaṃ
jalpanti mūḍhāstu guṇairvihīnāḥ"""
	V = S.scan(input_string, from_scheme='IAST')
	VT = VerseTester()
	VT.test_as_samavftta_and_or_upajAti(V)
	output = V.meter_score # int
	print("\n\ntest_as_samavftta_and_or_upajAti_sampUrRakumBo OUTPUT:\n" + str(output) + '\n\n')
	print(VT.samavftta_result)
	expected_output = 7
	assert output == expected_output
