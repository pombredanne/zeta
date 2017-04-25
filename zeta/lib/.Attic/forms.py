"""Helper functions for forms

Creates the Form objects.
"""
from   pytz                               import all_timezones

#---------------------------- Form Classes -----------------------------------

class Form(object) :
    pass

class Column(object) :
    pass

class Fieldset(object) :
    pass

class Input(object) :
    pass


#--------------------- Helper functions to frame form objects ----------------

# formfill = [ width, [ fieldsets ] ]    for each column
# fieldset = [ legend_style, text, [ inputs ] ]
# input    = [ type, class, id, valign, name, value, label, param, attr, text, help ]
# attr     = String containing the following characters, each representing a
#            boolean attribute
#               d - Disable the <input>
#               r - Make <input> readonly

# Pending inputs, 'button', 'image',

# if type in ['text', 'password', 'file' ]
#   param = maxlen
# if type in [ 'checkbox', 'radio' ],
#   param is not used
# if type in ['textarea'],
#   param = rows,cols
# if type in ['captcha'],
#   param = imgsrc
# if type in ['hidden'],
#   param is not used
# if type in ['list'],
#   param = (size, [_optgroup]
#   _optgroup = (disabled, label, [ _options ])
#   _option   = (disabled, selected, value, text)


def form_input( type, cls, id, valign, name, value, label, param=None, attr="",
                text=None, help=None ) :
    """Generate the input field object."""
    inp          = Input()
    inp.type     = type
    inp.cls      = cls 
    inp.id       = id  
    inp.valign   = valign
    inp.name     = name
    inp.value    = value
    inp.label    = label
    inp.help     = help
    inp.text     = text
    inp.readonly = False
    inp.disabled = False
    inp.multiple = False
    if inp.type in [ 'text', 'password', 'file'] :
        inp.maxlen   = param
    elif inp.type in [ 'checkbox', 'radio' ] :
        pass
    elif inp.type in [ 'textarea' ] :
        inp.x, inp.y = param.split(',')
    elif inp.type in [ 'captcha' ] :
        inp.imgsrc   = param
    elif inp.type in [ 'hidden' ] :
        pass
    elif inp.type in [ 'list' ] :
        inp.select   = param
    if attr :
        if 'r' in attr :
            inp.readonly = True
        if 'd' in attr :
            inp.disabled = True
        if 'm' in attr :
            inp.multiple = True
    return inp


def form_fieldset( legend_style, text, inputs=None ) :
    """Generate the fieldset object to be attached to the form."""
    fs              = Fieldset()
    fs.legend_style = legend_style
    fs.text         = text
    fs.inputs       = []
    if inputs :
        for input in inputs :
            if input :
                fs.inputs.append( form_input(*input) )
            else :
                fs.inputs.append( None )
    return fs


def form_column( width, fieldsets=None ) :
    """Generate the column object to be attached to the column."""
    col           = Column()
    col.width     = width
    col.fieldsets = []
    if fieldsets :
        for fieldset in fieldsets :
            col.fieldsets.append( form_fieldset(*fieldset) )
    return col


def form_form( formfill ) :
    """Generate the form object with form content filled."""
    cols = []
    for width, fieldsets in formfill :
        cols.append( form_column( width, fieldsets ))

    return cols
