import adsk.core, adsk.fusion, traceback

def ask_user(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface      
        
        (material, cancelled) = ui.inputBox("Please define a material: You may choose Oil, Water, Air, Mercury")        
        
        ui.messageBox(material, "Material") 
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
