import json

from fastapi.testclient import TestClient

from ..main import app
from . import utils

client = TestClient(app)


def test_get_negative_gas():
    utils.test_get_negative("gas")


### endpoint: /pig/{id}/gas/position/{group_id}
# Basic positive tests
def test_get_gas_position_251():
    response = client.get("/pig/251/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 446499*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278202.3184792972, 28013.68036349728, 248672.55276327548]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 446499

def test_get_gas_position_271():
    response = client.get("/pig/271/gas/Position/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 513379*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[0] == [278198.07020316395, 27948.384391798045, 248697.5992484129]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 513379


def test_get_gas_position_largeID():
    response = client.get("/pig/251/gas/Position/2117968")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas position data should be a 804*3 array list
    gas_position = json.loads(response.json()["gas_position"])
    assert type(gas_position) is list
    assert gas_position[3] == [198335.0403950171, 40257.09799530143, 189707.9848941324]
    assert len(gas_position[0]) == 3
    assert len(gas_position) == 804


### endpoint: /pig/{id}/gas/electron/{group_id}
# Basic positive tests
def test_get_gas_electron_251():
    response = client.get("/pig/251/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 446499*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894253730774
    assert len(gas_electron) == 446499


def test_get_gas_electron_271():
    response = client.get("/pig/271/gas/ElectronAbundance/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas electron data should be a 513379*1 array list
    gas_electron = json.loads(response.json()["gas_electronabundance"])
    assert type(gas_electron) is list
    assert gas_electron[0] == 1.157894492149353
    assert len(gas_electron) == 513379


### endpoint: /pig/{id}/gas/H2fraction/{group_id}
# Basic positive tests
def test_get_gas_h2fraction_251():
    response = client.get("/pig/251/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 446499*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.9962370991706848
    assert len(gas_h2fraction) == 446499

def test_get_gas_h2fraction_271():
    response = client.get("/pig/271/gas/H2Fraction/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas h2fraction data should be a 513379*1 array list
    gas_h2fraction = json.loads(response.json()["gas_h2fraction"])
    assert type(gas_h2fraction) is list
    assert gas_h2fraction[0] == 0.0
    assert gas_h2fraction[100000] == 0.13368326425552368
    assert len(gas_h2fraction) == 513379


### endpoint: /pig/{id}/gas/InternalEnergy/{group_id}
# Basic positive tests
def test_get_gas_internal_energy_251():
    response = client.get("/pig/251/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas InternalEnergy data should be a 446499*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 112487.609375
    assert len(gas_internal_energy) == 446499


def test_get_gas_internal_energy_271():
    response = client.get("/pig/271/gas/InternalEnergy/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas InternalEnergy data should be a 513379*1 array list
    gas_internal_energy = json.loads(response.json()["gas_internalenergy"])
    assert type(gas_internal_energy) is list
    assert gas_internal_energy[0] == 163354.578125
    assert len(gas_internal_energy) == 513379


### endpoint: /pig/{id}/gas/Density/{group_id}
# Basic positive tests
def test_get_gas_density_251():
    response = client.get("/pig/251/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Density data should be a 446499*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.9312253957414214e-08
    assert gas_density[:4] == [2.9312253957414214e-08, 3.0495591829549085e-08, 3.838168538550235e-08, 4.375229067932196e-08]
    assert len(gas_density) == 446499


def test_get_gas_density_271():
    response = client.get("/pig/271/gas/Density/1")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Density data should be a 513379*1 array list
    gas_density = json.loads(response.json()["gas_density"])
    assert type(gas_density) is list
    assert gas_density[0] == 2.121526954113051e-08
    assert gas_density[:4] == [2.121526954113051e-08, 2.48780214207045e-08, 3.295386008517198e-08, 3.252150193588932e-08]
    assert len(gas_density) == 513379


### endpoint: /pig/{id}/gas/Entropy/{group_id}
# Basic positive tests
def test_get_gas_entropy_251():
    response = client.get("/pig/251/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Entropy data should be a 68419*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 2959285.5
    assert gas_entropy[:4] == [2959285.5, 77811.4609375, 100789.5625, 111917.515625]
    assert len(gas_entropy) == 68419


def test_get_gas_entropy_271():
    response = client.get("/pig/271/gas/Entropy/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Entropy data should be a 77457*1 array list
    gas_entropy = json.loads(response.json()["gas_entropy"])
    assert type(gas_entropy) is list
    assert gas_entropy[0] == 40433988.0
    assert gas_entropy[:4] == [40433988.0, 11036351.0, 22856564.0, 211525.53125]
    assert len(gas_entropy) == 77457


### endpoint: /pig/{id}/gas/JUV/{group_id}
# Basic positive tests
def test_get_gas_juv_251():
    response = client.get("/pig/251/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas JUV data should be a 134377*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 134377


def test_get_gas_juv_271():
    response = client.get("/pig/271/gas/JUV/10")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas JUV data should be a 145402*1 array list
    gas_juv = json.loads(response.json()["gas_juv"])
    assert type(gas_juv) is list
    assert gas_juv[0] == 9.999999682655225e-22
    assert len(gas_juv) == 145402


### endpoint: /pig/{id}/gas/NeutralHydrogenFraction/{group_id}
# Basic positive tests
def test_get_gas_nhf_251():
    response = client.get("/pig/251/gas/NeutralHydrogenFraction/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas NeutralHydrogenFraction data should be a 102446*1 array list
    gas_nhf = json.loads(response.json()["gas_neutralhydrogenfraction"])
    assert type(gas_nhf) is list
    assert gas_nhf[0] == 1.5026954542918247e-06
    assert len(gas_nhf) == 102446


def test_get_gas_nhf_271():
    response = client.get("/pig/271/gas/NeutralHydrogenFraction/20")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas NeutralHydrogenFraction data should be a 119976*1 array list
    gas_nhf = json.loads(response.json()["gas_neutralhydrogenfraction"])
    assert type(gas_nhf) is list
    assert gas_nhf[0] == 6.849857072666055e-06
    assert len(gas_nhf) == 119976


### endpoint: /pig/{id}/gas/Pressure/{group_id}
# Basic positive tests
def test_get_gas_pressure_251():
    response = client.get("/pig/251/gas/Pressure/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Pressure data should be a 83500*1 array list
    gas_pressure = json.loads(response.json()["gas_pressure"])
    assert type(gas_pressure) is list
    assert gas_pressure[0] == 1.6903873984119855e-05
    assert gas_pressure[:4] == [1.6903873984119855e-05, 1.3225580005382653e-05, 1.914056383611751e-06, 4.885966973233735e-06]
    assert len(gas_pressure) == 83500


def test_get_gas_pressure_271():
    response = client.get("/pig/271/gas/Pressure/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Pressure data should be a 102438*1 array list
    gas_pressure = json.loads(response.json()["gas_pressure"])
    assert type(gas_pressure) is list
    assert gas_pressure[0] == 6.205591773777996e-08
    assert gas_pressure[:4] == [6.205591773777996e-08, 1.3783197800876223e-06, 3.136743202958314e-07, 1.2491647112256032e-06]
    assert len(gas_pressure) == 102438


### endpoint: /pig/{id}/gas/Velocity/{group_id}
# Basic positive tests
def test_get_gas_velocity_251():
    response = client.get("/pig/251/gas/Velocity/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Velocity data should be a 83500*1 array list
    gas_velocity = json.loads(response.json()["gas_velocity"])
    assert type(gas_velocity) is list
    assert gas_velocity[0] == [-65.1724624633789, 24.529680252075195, 38.377403259277344]
    assert len(gas_velocity) == 83500


def test_get_gas_velocity_271():
    response = client.get("/pig/271/gas/Velocity/30")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Velocity data should be a 102438*1 array list
    gas_velocity = json.loads(response.json()["gas_velocity"])
    assert type(gas_velocity) is list
    assert gas_velocity[0] == [61.37261962890625, 30.83819007873535, 15.464899063110352]
    assert len(gas_velocity) == 102438


### endpoint: /pig/{id}/gas/EgyWtDensity/{group_id}
# Basic positive tests
def test_get_gas_egywtdensity_251():
    response = client.get("/pig/251/gas/EgyWtDensity/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas EgyWtDensity data should be a 75980*1 array list
    gas_egywtdensity = json.loads(response.json()["gas_egywtdensity"])
    assert type(gas_egywtdensity) is list
    assert gas_egywtdensity[0] == 1.1311906078503853e-08
    assert gas_egywtdensity[:4] == [1.1311906078503853e-08, 1.0542879458341758e-08, 4.6664844433053077e-08, 6.323491419379934e-08]
    assert len(gas_egywtdensity) == 75980


def test_get_gas_egywtdensity_271():
    response = client.get("/pig/271/gas/EgyWtDensity/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas EgyWtDensity data should be a 51832*1 array list
    gas_egywtdensity = json.loads(response.json()["gas_egywtdensity"])
    assert type(gas_egywtdensity) is list
    assert gas_egywtdensity[0] == 1.3695033374006016e-07
    assert gas_egywtdensity[:4] == [1.3695033374006016e-07, 1.5859635595916188e-06, 4.7282750159638454e-08, 3.3221699595742393e-06]
    assert len(gas_egywtdensity) == 51832


### endpoint: /pig/{id}/gas/Generation/{group_id}
# Basic positive tests
def test_get_gas_generation_251():
    response = client.get("/pig/251/gas/Generation/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Generation data should be a 75980*1 array list
    gas_generation = json.loads(response.json()["gas_generation"])
    assert type(gas_generation) is list
    assert gas_generation[10000] == 1
    assert len(gas_generation) == 75980


def test_get_gas_generation_271():
    response = client.get("/pig/271/gas/Generation/40")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Generation data should be a 51832*1 array list
    gas_generation = json.loads(response.json()["gas_generation"])
    assert type(gas_generation) is list
    assert gas_generation[15000] == 0
    assert len(gas_generation) == 51832


### endpoint: /pig/{id}/gas/Mass/{group_id}
# Basic positive tests
def test_get_gas_mass_251():
    response = client.get("/pig/251/gas/Mass/50")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Mass data should be a 76352*1 array list
    gas_mass = json.loads(response.json()["gas_mass"])
    assert type(gas_mass) is list
    assert gas_mass[0] == 0.00023622244771104306
    assert gas_mass[:4] == [0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306]
    assert len(gas_mass) == 76352


def test_get_gas_mass_271():
    response = client.get("/pig/271/gas/Mass/50")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Mass data should be a 86405*1 array list
    gas_mass = json.loads(response.json()["gas_mass"])
    assert type(gas_mass) is list
    assert gas_mass[0] == 0.00023622244771104306
    assert gas_mass[:4] == [0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306, 0.00023622244771104306]
    assert len(gas_mass) == 86405


### endpoint: /pig/{id}/gas/SmoothingLength/{group_id}
# Basic positive tests
def test_get_gas_smoothinglength_251():
    response = client.get("/pig/251/gas/SmoothingLength/60")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas SmoothingLength data should be a 68059*1 array list
    gas_smoothinglength = json.loads(response.json()["gas_smoothinglength"])
    assert type(gas_smoothinglength) is list
    assert gas_smoothinglength[0] == 57.098350524902344
    assert gas_smoothinglength[:4] == [57.098350524902344, 31.1713924407959, 32.398929595947266, 25.489093780517578]
    assert len(gas_smoothinglength) == 68059


def test_get_gas_smoothinglength_271():
    response = client.get("/pig/271/gas/SmoothingLength/60")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas SmoothingLength data should be a 96354*1 array list
    gas_smoothinglength = json.loads(response.json()["gas_smoothinglength"])
    assert type(gas_smoothinglength) is list
    assert gas_smoothinglength[0] == 84.1534652709961
    assert gas_smoothinglength[:4] == [84.1534652709961, 97.58158874511719, 94.68399810791016, 81.02495574951172]
    assert len(gas_smoothinglength) == 96354


### endpoint: /pig/{id}/gas/GroupID/{group_id}
# Basic positive tests
def test_get_gas_groupid_251():
    response = client.get("/pig/251/gas/GroupID/70")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas GroupID data should be a 84132*1 array list
    gas_groupid = json.loads(response.json()["gas_groupid"])
    assert type(gas_groupid) is list
    assert gas_groupid[100] == 70
    assert gas_groupid[500] == 70
    assert len(gas_groupid) == 84132


def test_get_gas_groupid_271():
    response = client.get("/pig/271/gas/GroupID/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas GroupID data should be a 95309*1 array list
    gas_groupid = json.loads(response.json()["gas_groupid"])
    assert type(gas_groupid) is list
    assert gas_groupid[1000] == 80
    assert gas_groupid[2000] == 80
    assert len(gas_groupid) == 95309


### endpoint: /pig/{id}/gas/Metallicity/{group_id}
# Basic positive tests
def test_get_gas_metallicity_251():
    response = client.get("/pig/251/gas/Metallicity/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Metallicity data should be a 84749*1 array list
    gas_metallicity = json.loads(response.json()["gas_metallicity"])
    assert type(gas_metallicity) is list
    assert gas_metallicity[1] == 6.301722169155255e-05
    assert gas_metallicity[7] ==  3.587197852539248e-06
    assert len(gas_metallicity) == 84749


def test_get_gas_metallicity_271():
    response = client.get("/pig/271/gas/Metallicity/80")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Metallicity data should be a 95309*1 array list
    gas_metallicity = json.loads(response.json()["gas_metallicity"])
    assert type(gas_metallicity) is list
    assert gas_metallicity[2] == 0.010519527830183506
    assert gas_metallicity[100] == 0.0
    assert len(gas_metallicity) == 95309


### endpoint: /pig/{id}/gas/Potential/{group_id}
# Basic positive tests
def test_get_gas_potential_251():
    response = client.get("/pig/251/gas/Potential/90")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Potential data should be a 93123*1 array list
    gas_potential = json.loads(response.json()["gas_potential"])
    assert type(gas_potential) is list
    assert gas_potential[0] == -332538.125
    assert gas_potential[4] == -334103.46875
    assert len(gas_potential) == 93123


def test_get_gas_potential_271():
    response = client.get("/pig/271/gas/Potential/90")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas Potential data should be a 50143*1 array list
    gas_potential = json.loads(response.json()["gas_potential"])
    assert type(gas_potential) is list
    assert gas_potential[0] == -155053.03125
    assert gas_potential[:4] == [-155053.03125, -155029.625, -155162.640625, -155010.75]
    assert len(gas_potential) == 50143


### endpoint: /pig/{id}/gas/StarFormationRate/{group_id}
# Basic positive tests
def test_get_gas_starformationrate_251():
    response = client.get("/pig/251/gas/StarFormationRate/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas StarFormationRate data should be a 68419*1 array list
    gas_starformationrate = json.loads(response.json()["gas_starformationrate"])
    assert type(gas_starformationrate) is list
    assert gas_starformationrate[1000] == 0
    assert gas_starformationrate[5000] == 0.0003683421527966857
    assert len(gas_starformationrate) == 68419


def test_get_gas_starformationrate_271():
    response = client.get("/pig/271/gas/StarFormationRate/100")
    utils.common_positive_tests(response)
    # Validate payload: Response is a well-formed JSON object and response data -- gas StarFormationRate data should be a 50143*1 array list
    gas_starformationrate = json.loads(response.json()["gas_starformationrate"])
    assert type(gas_starformationrate) is list
    assert gas_starformationrate[15000] == 0.016309794038534164
    assert gas_starformationrate[10000] == 0
    assert len(gas_starformationrate) == 77457


### advanced lengthbytype query tests: /pig/{id}/{ptype}/{feature}/
def test_get_advanced_gas_density_251():
    response = client.get("/pig/251/gas/Density/", params = {'groupid_list': [1,2,3]})
    utils.common_positive_tests(response)
    gas_density_1 = json.loads(response.json()["gas_density"]["1"])
    assert type(gas_density_1) is list
    assert gas_density_1[:4] == [2.9312253957414214e-08, 3.0495591829549085e-08, 3.838168538550235e-08, 4.375229067932196e-08]
    assert len(gas_density_1) == 446499
    gas_density_2 = json.loads(response.json()["gas_density"]["2"])
    assert type(gas_density_2) is list
    assert gas_density_2[:4] == [6.8903700523037514e-09, 6.851533118634734e-09, 8.200615297937475e-09, 7.598972118216807e-09]
    assert len(gas_density_2) == 700225
    gas_density_3 = json.loads(response.json()["gas_density"]["3"])
    assert type(gas_density_3) is list
    assert gas_density_3[:4] == [2.12554578382651e-08, 2.075496752240724e-08, 2.7879844211042837e-08, 2.678831378943869e-08]
    assert len(gas_density_3) == 239021


def test_get_advanced_gas_entropy_251():
    response = client.get("/pig/251/gas/Entropy/", params = {'groupid_list': [4,5,6]})
    utils.common_positive_tests(response)
    gas_entropy_4 = json.loads(response.json()["gas_entropy"]["4"])
    assert type(gas_entropy_4) is list
    assert gas_entropy_4[:4] == [9321008.0, 53421.7734375, 63790.05859375, 53965.58984375]
    assert len(gas_entropy_4) == 125966
    gas_entropy_5 = json.loads(response.json()["gas_entropy"]["5"])
    assert type(gas_entropy_5) is list
    assert gas_entropy_5[:4] == [411603.28125, 146572.4375, 255028.5625, 110186.3046875]
    assert len(gas_entropy_5) == 172170
    gas_entropy_6 = json.loads(response.json()["gas_entropy"]["6"])
    assert type(gas_entropy_6) is list
    assert gas_entropy_6[:4] == [81743.9140625, 132288.1875, 73330.1796875, 104180.6171875]
    assert len(gas_entropy_6) == 154147


def test_get_advanced_gas_h2fraction_251():
    response = client.get("/pig/251/gas/H2Fraction/", params = {'groupid_list': [7,8,9]})
    utils.common_positive_tests(response)
    gas_h2fraction_7 = json.loads(response.json()["gas_h2fraction"]["7"])
    assert type(gas_h2fraction_7) is list
    assert gas_h2fraction_7[10000:10004] == [0.009490085765719414, 0, 0, 0]
    assert len(gas_h2fraction_7) == 177623
    gas_h2fraction_8 = json.loads(response.json()["gas_h2fraction"]["8"])
    assert type(gas_h2fraction_8) is list
    assert gas_h2fraction_8[20000:20004] == [0, 0, 0, 0.04939519986510277]
    assert len(gas_h2fraction_8) == 142821
    gas_h2fraction_9 = json.loads(response.json()["gas_h2fraction"]["9"])
    assert type(gas_h2fraction_9) is list
    assert gas_h2fraction_9[15000:15004] == [0.15932804346084595, 0, 0.0031604496762156487, 0]
    assert len(gas_h2fraction_9) == 140981


def test_get_advanced_gas_juv_251():
    response = client.get("/pig/251/gas/JUV/", params = {'groupid_list': [10,11,12]})
    utils.common_positive_tests(response)
    gas_juv_10 = json.loads(response.json()["gas_juv"]["10"])
    assert type(gas_juv_10) is list
    assert gas_juv_10[10000:10004] == [9.999999682655225e-22, 9.999999682655225e-22, 9.999999682655225e-22, 9.999999682655225e-22]
    assert len(gas_juv_10) == 134377
    gas_juv_11 = json.loads(response.json()["gas_juv"]["11"])
    assert type(gas_juv_11) is list
    assert gas_juv_11[20000] == 9.999999682655225e-22
    assert len(gas_juv_11) == 102244
    gas_juv_12 = json.loads(response.json()["gas_juv"]["12"])
    assert type(gas_juv_12) is list
    assert gas_juv_12[15000] == 9.999999682655225e-22
    assert len(gas_juv_12) == 91408


def test_get_advanced_gas_nhf_251():
    response = client.get("/pig/251/gas/NeutralHydrogenFraction/", params = {'groupid_list': [13,14,15]})
    utils.common_positive_tests(response)
    gas_nhf_13 = json.loads(response.json()["gas_neutralhydrogenfraction"]["13"])
    assert type(gas_nhf_13) is list
    assert gas_nhf_13[:4] == [0.00016779893485363573, 0.001974311890080571, 0.0013231453485786915, 0.004058866761624813]
    assert len(gas_nhf_13) == 109887
    gas_nhf_14 = json.loads(response.json()["gas_neutralhydrogenfraction"]["14"])
    assert type(gas_nhf_14) is list
    assert gas_nhf_14[:4] == [1.6623314422758995e-06, 3.881593784171855e-06, 1.4636433661507908e-05, 0.021240321919322014]
    assert len(gas_nhf_14) == 101137
    gas_nhf_15 = json.loads(response.json()["gas_neutralhydrogenfraction"]["15"])
    assert type(gas_nhf_15) is list
    assert gas_nhf_15[:4] == [0.006793433800339699, 0.005498229991644621, 0.009771108627319336, 0.007732793223112822]
    assert len(gas_nhf_15) == 99544


def test_get_advanced_gas_pressure_251():
    response = client.get("/pig/251/gas/Pressure/", params = {'groupid_list': [16,17,18]})
    utils.common_positive_tests(response)
    gas_pressure_16 = json.loads(response.json()["gas_pressure"]["16"])
    assert type(gas_pressure_16) is list
    assert gas_pressure_16[:4] == [3.65005826097331e-06, 7.030094479887339e-07, 8.947169476414274e-07, 1.1282971854598145e-06]
    assert len(gas_pressure_16) == 119751
    gas_pressure_17 = json.loads(response.json()["gas_pressure"]["17"])
    assert type(gas_pressure_17) is list
    assert gas_pressure_17[:4] == [1.4249569630919723e-06, 1.5151192656048806e-06, 8.5890900436425e-07, 5.033523393649375e-07]
    assert len(gas_pressure_17) == 123411
    gas_pressure_18 = json.loads(response.json()["gas_pressure"]["18"])
    assert type(gas_pressure_18) is list
    assert gas_pressure_18[:4] == [1.0433600436954293e-06, 1.858478412941622e-06, 2.476672761986265e-06, 4.140899363846984e-06]
    assert len(gas_pressure_18) == 119046


def test_get_advanced_gas_velocity_251():
    response = client.get("/pig/251/gas/Velocity/", params = {'groupid_list': [19,20,21]})
    utils.common_positive_tests(response)
    gas_velocity_19 = json.loads(response.json()["gas_velocity"]["19"])
    assert type(gas_velocity_19) is list
    assert gas_velocity_19[0] == [-10.421012878417969, -11.563729286193848, -8.927306175231934]
    assert len(gas_velocity_19) == 87054
    gas_velocity_20 = json.loads(response.json()["gas_velocity"]["20"])
    assert type(gas_velocity_20) is list
    assert gas_velocity_20[0] == [55.109683990478516, 4.177705764770508, -14.314995765686035]
    assert len(gas_velocity_20) == 102446
    gas_velocity_21 = json.loads(response.json()["gas_velocity"]["21"])
    assert type(gas_velocity_21) is list
    assert gas_velocity_21[0] == [-34.447486877441406, -1.5274184942245483, 37.998382568359375]
    assert len(gas_velocity_21) == 70998