 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='civilian_initial_count', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.civilian_initial_count = IntText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='civilian_speed', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.civilian_speed = FloatText(
          value=.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='civilian_birth_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.civilian_birth_rate = FloatText(
          value=.0007,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='civilian_death_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.civilian_death_rate = FloatText(
          value=.000007,
          step=1e-06,
          style=style, layout=widget_layout)

        param_name6 = Button(description='civilian_strength', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.civilian_strength = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name7 = Button(description='thanos_speed', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.thanos_speed = FloatText(
          value=1.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='thanos_strength', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.thanos_strength = FloatText(
          value=1000,
          step=100,
          style=style, layout=widget_layout)

        param_name9 = Button(description='thanos_motility_bias', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.thanos_motility_bias = FloatText(
          value=.85,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='avenger_initial_count', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.avenger_initial_count = IntText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='avenger_speed', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.avenger_speed = FloatText(
          value=4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='avenger_strength', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.avenger_strength = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='avenger_motility_bias', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.avenger_motility_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='avenger_motility_bias_with_stone', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.avenger_motility_bias_with_stone = FloatText(
          value=0.2,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='initial number of civilians', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='civilian migration speed', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='civilian birth rate', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='civilian death rate', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='civilian battle strength', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='Thanos migration speed', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='Thanos battle strength', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Thanos migration bias (0 = Brownian)', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='number of Avengers', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Avengers migration speed', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Avengers battle stregth', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Avengers migration bias (0 = Brownian)', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Avengers migration bias when hiding Infinity Stone', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.civilian_initial_count, units_button2, desc_button2] 
        row3 = [param_name3, self.civilian_speed, units_button3, desc_button3] 
        row4 = [param_name4, self.civilian_birth_rate, units_button4, desc_button4] 
        row5 = [param_name5, self.civilian_death_rate, units_button5, desc_button5] 
        row6 = [param_name6, self.civilian_strength, units_button6, desc_button6] 
        row7 = [param_name7, self.thanos_speed, units_button7, desc_button7] 
        row8 = [param_name8, self.thanos_strength, units_button8, desc_button8] 
        row9 = [param_name9, self.thanos_motility_bias, units_button9, desc_button9] 
        row10 = [param_name10, self.avenger_initial_count, units_button10, desc_button10] 
        row11 = [param_name11, self.avenger_speed, units_button11, desc_button11] 
        row12 = [param_name12, self.avenger_strength, units_button12, desc_button12] 
        row13 = [param_name13, self.avenger_motility_bias, units_button13, desc_button13] 
        row14 = [param_name14, self.avenger_motility_bias_with_stone, units_button14, desc_button14] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.civilian_initial_count.value = int(uep.find('.//civilian_initial_count').text)
        self.civilian_speed.value = float(uep.find('.//civilian_speed').text)
        self.civilian_birth_rate.value = float(uep.find('.//civilian_birth_rate').text)
        self.civilian_death_rate.value = float(uep.find('.//civilian_death_rate').text)
        self.civilian_strength.value = float(uep.find('.//civilian_strength').text)
        self.thanos_speed.value = float(uep.find('.//thanos_speed').text)
        self.thanos_strength.value = float(uep.find('.//thanos_strength').text)
        self.thanos_motility_bias.value = float(uep.find('.//thanos_motility_bias').text)
        self.avenger_initial_count.value = int(uep.find('.//avenger_initial_count').text)
        self.avenger_speed.value = float(uep.find('.//avenger_speed').text)
        self.avenger_strength.value = float(uep.find('.//avenger_strength').text)
        self.avenger_motility_bias.value = float(uep.find('.//avenger_motility_bias').text)
        self.avenger_motility_bias_with_stone.value = float(uep.find('.//avenger_motility_bias_with_stone').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//civilian_initial_count').text = str(self.civilian_initial_count.value)
        uep.find('.//civilian_speed').text = str(self.civilian_speed.value)
        uep.find('.//civilian_birth_rate').text = str(self.civilian_birth_rate.value)
        uep.find('.//civilian_death_rate').text = str(self.civilian_death_rate.value)
        uep.find('.//civilian_strength').text = str(self.civilian_strength.value)
        uep.find('.//thanos_speed').text = str(self.thanos_speed.value)
        uep.find('.//thanos_strength').text = str(self.thanos_strength.value)
        uep.find('.//thanos_motility_bias').text = str(self.thanos_motility_bias.value)
        uep.find('.//avenger_initial_count').text = str(self.avenger_initial_count.value)
        uep.find('.//avenger_speed').text = str(self.avenger_speed.value)
        uep.find('.//avenger_strength').text = str(self.avenger_strength.value)
        uep.find('.//avenger_motility_bias').text = str(self.avenger_motility_bias.value)
        uep.find('.//avenger_motility_bias_with_stone').text = str(self.avenger_motility_bias_with_stone.value)
