 # HOW TO HAVE CUSTOM LOGGING

 Just Copy paste this code into the beginning of a python file (eg:test.py)

After the code try (this example is also added in the code)

```python
#EXAMPLES
cars = ["Ford", "Volvo", "BMW"]

# THIS WILL LOG ANYTHING AS STRING
logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))

# THIS WILL LOG ANY OBJECT
logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))

# THIS WILL LOG ALL LOCALS
logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
```

This will print

```bash
--------------------------------------------------------------------------------------------------------------
2020-08-26 15:12:51,852
XXXDEBUGXXX <module>() python_logging.py[:219] custom_string 
NONE_NO_REQUEST_ABS_PATH        
NONE_NO_REQUEST_METHOD
--------------------------------------------------------------------------------------------------------------

    214: 
    215: #EXAMPLES
    216: cars = ["Ford", "Volvo", "BMW"]
    217: 
    218: # THIS WILL LOG ANYTHING AS STRING
 219***: logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))
    220: 
    221: # THIS WILL LOG ANY OBJECT
    222: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS


['Ford', 'Volvo', 'BMW']

  File "python_logging.py", line 219, in <module>
    logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))


    214: 
    215: #EXAMPLES
    216: cars = ["Ford", "Volvo", "BMW"]
    217: 
    218: # THIS WILL LOG ANYTHING AS STRING
 219***: logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))
    220: 
    221: # THIS WILL LOG ANY OBJECT
    222: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS

--------------------------------------------------------------------------------------------------------------
2020-08-26 15:12:51,860
XXXDEBUGXXX <module>() python_logging.py[:222] custom_string 
NONE_NO_REQUEST_ABS_PATH        
NONE_NO_REQUEST_METHOD
--------------------------------------------------------------------------------------------------------------

    217: 
    218: # THIS WILL LOG ANYTHING AS STRING
    219: logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))
    220: 
    221: # THIS WILL LOG ANY OBJECT
 222***: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS
    225: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    226: 
    227: 


[
    "Ford",
    "Volvo",
    "BMW"
]


  File "python_logging.py", line 222, in <module>
    logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))


    217: 
    218: # THIS WILL LOG ANYTHING AS STRING
    219: logger_custom_string.debug(anything(cars,traceback.format_stack(limit=5)))
    220: 
    221: # THIS WILL LOG ANY OBJECT
 222***: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS
    225: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    226: 
    227: 

--------------------------------------------------------------------------------------------------------------
2020-08-26 15:12:51,865
XXXDEBUGXXX <module>() python_logging.py[:225] custom_string 
NONE_NO_REQUEST_ABS_PATH        
NONE_NO_REQUEST_METHOD
--------------------------------------------------------------------------------------------------------------

    220: 
    221: # THIS WILL LOG ANY OBJECT
    222: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS
 225***: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    226: 
    227: 


{
    "VerFormatter": "<class '__main__.VerFormatter'>",
    "__annotations__": {},
    "__builtins__": "<module 'builtins' (built-in)>",
    "__cached__": null,
    "__doc__": null,
    "__file__": "python_logging.py",
    "__loader__": "<_frozen_importlib_external.SourceFileLoader object at 0x7f3a3097be48>",
    "__name__": "__main__",
    "__package__": null,
    "__spec__": null,
    "anything": "<function anything at 0x7f3a309b61e0>",
    "cars": [
        "Ford",
        "Volvo",
        "BMW"
    ],
    "exposed_request": null,
    "formatter": "<__main__.VerFormatter object at 0x7f3a308409e8>",
    "handler": "<StreamHandler <stderr> (DEBUG)>",
    "json_dumps_default": "<function json_dumps_default at 0x7f3a307851e0>",
    "keys_string": "<function keys_string at 0x7f3a30785158>",
    "logger_custom_string": "<Logger custom_string (DEBUG)>",
    "logging": "<module 'logging' from '/usr/lib/python3.7/logging/__init__.py'>",
    "pp_odir": "<function pp_odir at 0x7f3a307852f0>",
    "pp_odir_getobject": "<function pp_odir_getobject at 0x7f3a30785268>",
    "pp_traceback": "<function pp_traceback at 0x7f3a30785378>",
    "traceback": "<module 'traceback' from '/usr/lib/python3.7/traceback.py'>"
}


  File "python_logging.py", line 225, in <module>
    logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))


    220: 
    221: # THIS WILL LOG ANY OBJECT
    222: logger_custom_string.debug(pp_odir(cars,traceback.format_stack(limit=5)))
    223: 
    224: # THIS WILL LOG ALL LOCALS
 225***: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    226: 
    227: 

```

Here we can see the locals() and also the line where the logging is called and also stacktrace. This will help
in debugging the values

