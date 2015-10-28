'''
Created July 2015

@author: TEASER 4 Development Team


This Scripts loads the VDI 6007 Room from the old format of TEASER 3, 
manipulates the data thus it fits with the specification of VDI 6007 and 
computes the parameters. The parameters are then compared with the ones from
Rouvel

'''

from teaser.Project import Project
import teaser.Logic.Utilis as utilis


def parameter_room1():
    
    '''
    load project of VDI 6007 room from TEASER file
    '''
    prj = Project(False)
    
    prj.load_project(utilis.get_full_path("Examples\\ExampleInputFiles\\VDI6007_Room1.teaserXML"))
    
    '''
    execute VDI calculation for single zone
    '''
    
    prj.list_of_buildings[0].calc_building_parameter('vdi')
    
    return prj
    

prj = parameter_room1()

'''
parameters inner wall Typraum S
'''
print("Parameters for inner wall")
print("r1_iw:", prj.list_of_buildings[0].thermal_zones[0].r1_iw, "K/W ---", "Rouvel: 0.000595515 K/W")
print("c1_iw: ", prj.list_of_buildings[0].thermal_zones[0].c1_iw / 1000, "kJ/K ---", "Rouvel: 14836.2 kJ/K")
print("area_iw: ", prj.list_of_buildings[0].thermal_zones[0].area_iw, "qm ---", "Rouvel: 75.5 qm")
print("alpha_weight_conv_iw: ", prj.list_of_buildings[0].thermal_zones[0].alpha_conv_iw, "W/(qm*K) ---", "Rouvel: 2.236423594 W/(qm*K)")

'''
parameters outer wall Typraum S
'''
print("\nParameters for outer wall")
print("r_rest_ow", prj.list_of_buildings[0].thermal_zones[0].r_rest_ow, "K/W ---", "Rouvel: 0.042768721 K/W")
print("r1_ow:", prj.list_of_buildings[0].thermal_zones[0].r1_ow, "K/W ---", "Rouvel: 0.004367913 K/W")
print("c1_ow: ", prj.list_of_buildings[0].thermal_zones[0].c1_ow / 1000, "kJ/K ---", "Rouvel: 1600.8 kJ/K")
print("area_ow: ", prj.list_of_buildings[0].thermal_zones[0].area_ow + prj.list_of_buildings[0].thermal_zones[0].area_win, "qm ---", "Rouvel: 10.5 qm")
print("alpha_conv_inner_ow: ", prj.list_of_buildings[0].thermal_zones[0].alpha_conv_inner_ow, "W/(qm*K) ---", "Rouvel: 2.7 W/(qm*K)")
print("alpha_comb_outer_ow: ", prj.list_of_buildings[0].thermal_zones[0].alpha_comb_outer_ow, "W/(qm*K) ---", "Rouvel: 25.0 W/(qm*K)")
