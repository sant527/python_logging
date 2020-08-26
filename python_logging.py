import logging
import traceback

#######################
#CREATE CUSTOM LOGGING FORMATTER
#######################
exposed_request=None
class VerFormatter(logging.Formatter):
    def format(self, record):
        ## We want to show some code lines while logging. So that its eays to know 
        #create a list of all the linenumber: lines 
        lines=[]
        with open(record.pathname) as src:
            for index, line in enumerate(src.readlines(), start=1):
                if index == record.lineno:
                    lines.append('{:4d}***: {}'.format(index, line))
                else:
                    lines.append('{:7d}: {}'.format(index, line))
        # select +/-3 lines from the current line
        start=(record.lineno -1) - 5
        end=(record.lineno -1) + 5
        if record.lineno == len(lines):
            end = record.lineno-1
        if end > len(lines)-1:
            end = len(lines)-1
        if record.lineno -1 == 0:
            start = 0
        if start < 0:
            start = 0
        code = ''.join(lines[start:end+1]) #lines[start:length]

        # colorize the code
        import pygments
        from pygments.lexers.python import Python3Lexer
        from pygments.formatters import TerminalTrueColorFormatter
        code = pygments.highlight(
            code,
            Python3Lexer(),
            #TerminalTrueColorFormatter(style='monokai') #use for terminal
            TerminalTrueColorFormatter() #use for jupyter notebook
        )

        #add new attributes to record which will be used later
        # we also want to have the url requested and its method
        if exposed_request is not None:
            record.absolute_path = exposed_request.build_absolute_uri()
            record.method = exposed_request.method
        else:
            record.absolute_path = "NONE_NO_REQUEST_ABS_PATH        "
            record.method = "NONE_NO_REQUEST_METHOD"
        record.codelines = code
        record.topline = "--------------------------------------------------------------------------------------------------------------"
        record.botline = "--------------------------------------------------------------------------------------------------------------"
        return super(VerFormatter, self).format(record)


formatter = VerFormatter('%(topline)s\n%(asctime)s\nXXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(absolute_path)s\n%(method)s\n%(topline)s\n\n%(codelines)s\n\n%(message)s\n\n%(codelines)s')

#######################
#CREATE AND HANDLER AND SET THE LEVEL AND FORMATTER
#######################
handler =  logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)


#######################
#FUNCTIONS
######################
def anything(var,trace):
    trace_hightligh = pp_traceback(trace)
    str3 = '\n\n'.join([str(var), trace_hightligh])
    return str3

# The below function converts any byte string keys into string
#we found that if key is byte string then json.dumps will throw error So we have to convert the dict
# recursive key as string conversion for byte keys
#https://stackoverflow.com/a/57014404/2897115
def keys_string(d):
    rval = {}

    # Sometimes the object is not a dict it can be list and also. So 
    # Eg:
    ## '_preconf_set_by_auto': {'result_backend', 'broker_url'}
    ## the above will raise error: AttributeError: 'str' object has no attribute 'items'
    ## list = [1,3,4] To declare a tuple, we use brackets.
    ## tuples = (1, 2, "a") To declare a tuple, we use parentheses.
    ## sets = {1,2,3} declare a set. Use curly braces 
    # So we check whether its a dict and then its a tuple,list,set
    if not isinstance(d, dict):
        if isinstance(d,(tuple,list,set)):
            v = [keys_string(x) for x in d]
            return v
        else:
            return d

    # we have to store the keys in a list else some objects give dictionary
    # changed size during iteration error
    # https://stackoverflow.com/questions/59662479/python-error-dictionary-changed-size-during-iteration-when-trying-to-iterate
    keys = list(d.keys())
    for k in keys:
        v = d[k]
        if isinstance(k,bytes):
            k = k.decode()
        if isinstance(v,dict):
            v = keys_string(v)
        elif isinstance(v,(tuple,list,set)):
            v = [keys_string(x) for x in v]
        rval[k] = v
    return rval


# in json_dumps we can pass a default function
def json_dumps_default(obj):
    repr_obj = repr(obj)
    str_obj = str(obj)

    if repr_obj == str_obj:
        return repr_obj
    else:
        return repr_obj,f"STR: {str_obj}"

# If the obj is not dict.tuple,list,set then we categorize the dir(obj)
def pp_odir_getobject(obj):
    if isinstance(obj,dict):
        return keys_string(obj)
    if isinstance(obj,(tuple,list,set)):
        return keys_string(obj)

    #c_dict = {k: getattr(obj, k) for k in dir(obj)} # this gives all the properties listed using dir(c)

    # we are not using the above is because if there are except it stops
    c_dict = {
                '00_METHODS********************************************************************************':{},
                "01_UNDESCORE******************************************************************************":{},
                "02_OTHERS*********************************************************************************":{},
                "03_EXCEPTIONS*****************************************************************************":{},
                }
    for key in dir(obj):
        try:
            attr_obj = getattr(obj, key)
            if callable(attr_obj):
            #if inspect.ismethod(attr_obj):
                c_dict['00_METHODS********************************************************************************'][key] = attr_obj
            else:
                if key.startswith("_"):
                    c_dict['01_UNDESCORE******************************************************************************'][key] = attr_obj
                else:
                    c_dict['02_OTHERS*********************************************************************************'][key] = attr_obj
        except Exception as x:
            c_dict['03_EXCEPTIONS*****************************************************************************'][key] = x
    return keys_string(c_dict)


# pretty print using dir(obj) and then its properties and also the traceback
def pp_odir(obj,trace):

    ##  json.dumps(queryset) in Jupyter runs lot of sqls if the object is query set so we want to avoid that. It work fine with views.py
    ## .So we want to stop logging before json_str and continue back with its state after
    import logging
    logger_database = logging.getLogger("django.db.backends")
    try:
        log_filt_state=logger_database.filters[0].state
        logger_database.filters[0].close()
    except:
        pass

    # we have to do two things 1) is to convert any byte strings to keys and also segrate into methods,underscore and other and exceptions
    c_dict_flattened = pp_odir_getobject(obj)

    import json
    from pygments import highlight
    from pygments.lexers import JsonLexer
    from pygments.formatters import TerminalTrueColorFormatter
    #Before passing the dict we want to avoid any byte string keys so keys_string(c_dict)
    json_str=json.dumps(c_dict_flattened, indent=4, sort_keys=True, default=json_dumps_default)

    try:
        # based on the logging status continue after    
        if log_filt_state == 'open':
            logger_database.filters[0].open()
    except:
        pass

    highlight_obj = highlight(json_str, JsonLexer(), TerminalTrueColorFormatter(style='monokai'))
    trace_hightligh = pp_traceback(trace)
    str3 = '\n\n'.join([highlight_obj, trace_hightligh])
    return str3

def pp_traceback(traceback_format_stack):
    import pygments
    from pygments.lexers import Python3TracebackLexer
    from pygments.formatters import TerminalTrueColorFormatter
    traceback_string = ''.join(traceback_format_stack)
    traceback_color = pygments.highlight(traceback_string,Python3TracebackLexer(),TerminalTrueColorFormatter(style='trac')) # trac or rainbow_dash
    return traceback_color


#######################
#CREATE A LOGGER AND SET THE LEVEL AND HANDLER
#######################

import logging
import traceback
logger_custom_string = logging.getLogger("custom_string")
logger_custom_string.setLevel(logging.DEBUG)
logger_custom_string.addHandler(handler)
#usage1: To show anything as string
#logger_custom_string.debug(anything("Hare Krishna",traceback.format_stack(limit=5)))
#usage2: to show dict or obj
#logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
#logger_custom_string.debug(pp_odir(obj,traceback.format_stack(limit=5)))  # This will pretty print all the properties from dir(obj)


logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
