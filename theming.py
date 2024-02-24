 #['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond', 'Blue', 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue', 'Cornsilk', 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen', 'Darkkhaki', 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen', 'Darkslateblue', 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue', 'Dimgray', 'Dimgrey', 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite', 'Gold', 'Goldenrod', 'Gray', 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'Lavenderblush', 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan', 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey', 'Lightpink', 'Lightsalmon', 'Lightseagreen', 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime', 'Limegreen', 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen', 'Mediumslateblue', 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream', 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace', 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid', 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru', 'Pink', 'Plum', 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell', 'Sienna', 'Silver', 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'Whitesmoke', 'Yellow', 'Yellowgreen']
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ListProperty

KV = '''
<CustomCard>:
    orientation: "vertical"
    size_hint_y: None
    height: "60dp"  # Adjust the height of the CustomCard
    padding: "8dp"

    MDBoxLayout:
        id: card
        adaptive_height: True
        size_hint_y: None
        height: "40dp"  # Adjust the height of the MDBoxLayout inside CustomCard
        md_bg_color: root.bg_color

        MDLabel:
            id: label
            text: "Custom Card"
            halign: "center"
            theme_text_color: "Primary"

MDScreen:
    md_bg_color: app.theme_cls.backgroundColor
    MDBoxLayout:
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'top': 1}
        MDIconButton:
            on_release: app.open_menu(self)
            pos_hint: {"top": .98}
            x: "12dp"
            icon: "menu"
        MDLabel:
            id: label_color
            text: "Selected Color"
            halign: "center"
            
            theme_text_color: "Custom"
            text_color: app.theme_cls.primaryColor
       
    ScrollView:
        size_hint_y: 0.9
        
        MDGridLayout:
            cols:3
            id: card_list
            size_hint_y: None
            height: self.minimum_height
            spacing: "16dp"
            padding: "16dp"
'''


class CustomCard(MDBoxLayout):
    bg_color = ListProperty([1, 1, 1, 1])  

    def __init__(self, scheme_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = scheme_name
        self.scheme_name = scheme_name
        Clock.schedule_once(lambda dt: setattr(self.ids.card, "md_bg_color", self.bg_color))

class Example(MDApp):
    scheme_names = [
    'primaryColor', 'onPrimaryColor', 'primaryContainerColor', 'onPrimaryContainerColor',
    'secondaryColor', 'onSecondaryColor', 'secondaryContainerColor', 'onSecondaryContainerColor',
    'tertiaryColor', 'onTertiaryColor', 'tertiaryContainerColor', 'onTertiaryContainerColor',
    'errorColor', 'onErrorColor', 'errorContainerColor', 'onErrorContainerColor',
    'backgroundColor', 'onBackgroundColor', 'surfaceColor', 'onSurfaceColor',
    'surfaceVariantColor', 'onSurfaceVariantColor', 'outlineColor', 'outlineVariantColor',
    'shadowColor', 'scrimColor', 'inverseSurfaceColor', 'inverseOnSurfaceColor', 'inversePrimaryColor'
]

    def build(self):
        self.theme_cls.primary_palette = "Red" 
        self.theme_cls.theme_style = "Light"  
        root_widget = Builder.load_string(KV)
        self.create_cards(root_widget)
        return root_widget

    def open_menu(self, menu_button):
        menu_items = [
            {"text": "Set Palette", "on_release": lambda x="Set palette": self.open_palette_menu(x, menu_button)},
            {"text": "Switch Theme Style", "on_release": lambda: self.switch_theme_style()},
        ]
        menu = MDDropdownMenu(caller=menu_button, items=menu_items)
        menu.open()

    def open_palette_menu(self, item_name, menu_button):
        menu_items = [
            {"text": palette_name, "on_release": lambda x=palette_name: self.switch_palette(x)}
            for palette_name in ['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond', 'Blue', 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue', 'Cornsilk', 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen', 'Darkkhaki', 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen', 'Darkslateblue', 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue', 'Dimgray', 'Dimgrey', 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite', 'Gold', 'Goldenrod', 'Gray', 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'Lavenderblush', 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan', 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey', 'Lightpink', 'Lightsalmon', 'Lightseagreen', 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime', 'Limegreen', 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen', 'Mediumslateblue', 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream', 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace', 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid', 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru', 'Pink', 'Plum', 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell', 'Sienna', 'Silver', 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'Whitesmoke', 'Yellow', 'Yellowgreen']  
        ]
        menu = MDDropdownMenu(caller=menu_button, items=menu_items)
        menu.open()

    def switch_palette(self, selected_palette):
        self.theme_cls.primary_palette = selected_palette
        self.root.ids.label_color.text = selected_palette
        self.update_scheme_colors()

    def switch_theme_style(self):
        self.theme_cls.theme_style = 'Light' if self.theme_cls.theme_style == 'Dark' else 'Dark'
        self.update_scheme_colors()

    def update_scheme_colors(self):
        palette_name = self.theme_cls.primary_palette
        theme_style = self.theme_cls.theme_style

        palette_colors = {
            'Light': {
        'primaryColor': 'primaryColor',
        'onPrimaryColor': 'onPrimaryColor',
        'primaryContainerColor': 'primaryContainerColor',
        'onPrimaryContainerColor': 'onPrimaryContainerColor',
        'secondaryColor': 'secondaryColor',
        'onSecondaryColor': 'onSecondaryColor',
        'secondaryContainerColor': 'secondaryContainerColor',
        'onSecondaryContainerColor': 'onSecondaryContainerColor',
        'tertiaryColor': 'tertiaryColor',
        'onTertiaryColor': 'onTertiaryColor',
        'tertiaryContainerColor': 'tertiaryContainerColor',
        'onTertiaryContainerColor': 'onTertiaryContainerColor',
        'errorColor': 'errorColor',
        'onErrorColor': 'onErrorColor',
        'errorContainerColor': 'errorContainerColor',
        'onErrorContainerColor': 'onErrorContainerColor',
        'backgroundColor': 'backgroundColor',
        'onBackgroundColor': 'onBackgroundColor',
        'surfaceColor': 'surfaceColor',
        'onSurfaceColor': 'onSurfaceColor',
        'surfaceVariantColor': 'surfaceVariantColor',
        'onSurfaceVariantColor': 'onSurfaceVariantColor',
        'outlineColor': 'outlineColor',
        'outlineVariantColor': 'outlineVariantColor',
        'shadowColor': 'shadowColor',
        'scrimColor': 'scrimColor',
        'inverseSurfaceColor': 'inverseSurfaceColor',
        'inverseOnSurfaceColor': 'inverseOnSurfaceColor',
        'inversePrimaryColor': 'inversePrimaryColor'
    },
            'Dark': {
        'primaryColor': 'primaryColor',
        'onPrimaryColor': 'onPrimaryColor',
        'primaryContainerColor': 'primaryContainerColor',
        'onPrimaryContainerColor': 'onPrimaryContainerColor',
        'secondaryColor': 'secondaryColor',
        'onSecondaryColor': 'onSecondaryColor',
        'secondaryContainerColor': 'secondaryContainerColor',
        'onSecondaryContainerColor': 'onSecondaryContainerColor',
        'tertiaryColor': 'tertiaryColor',
        'onTertiaryColor': 'onTertiaryColor',
        'tertiaryContainerColor': 'tertiaryContainerColor',
        'onTertiaryContainerColor': 'onTertiaryContainerColor',
        'errorColor': 'errorColor',
        'onErrorColor': 'onErrorColor',
        'errorContainerColor': 'errorContainerColor',
        'onErrorContainerColor': 'onErrorContainerColor',
        'backgroundColor': 'backgroundColor',
        'onBackgroundColor': 'onBackgroundColor',
        'surfaceColor': 'surfaceColor',
        'onSurfaceColor': 'onSurfaceColor',
        'surfaceVariantColor': 'surfaceVariantColor',
        'onSurfaceVariantColor': 'onSurfaceVariantColor',
        'outlineColor': 'outlineColor',
        'outlineVariantColor': 'outlineVariantColor',
        'shadowColor': 'shadowColor',
        'scrimColor': 'scrimColor',
        'inverseSurfaceColor': 'inverseSurfaceColor',
        'inverseOnSurfaceColor': 'inverseOnSurfaceColor',
        'inversePrimaryColor': 'inversePrimaryColor'
    }
        }

        for card in self.root.ids.card_list.children:
            scheme_name = card.ids.label.text
            corrected_scheme_name = palette_colors[theme_style].get(scheme_name)
            if corrected_scheme_name:
                card.ids.card.md_bg_color = getattr(self.theme_cls, corrected_scheme_name)

    def create_cards(self, root_widget):
        for scheme_name in self.scheme_names:
            bg_color = getattr(self.theme_cls, scheme_name)
            card = CustomCard(scheme_name=scheme_name)
            card.bg_color = bg_color 
            root_widget.ids.card_list.add_widget(card)


Example().run()


