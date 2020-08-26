 # HOW TO HAVE CUSTOM LOGGING

 Just Copy paste this code into the beginning of a python file (eg:test.py)

Then do

```python
logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
```

This will print

```bash
$ python test.py
--------------------------------------------------------------------------------------------------------------
2020-08-26 14:59:47,161
XXXDEBUGXXX <module>() test.py[:218] custom_string 
NONE_NO_REQUEST_ABS_PATH        
NONE_NO_REQUEST_METHOD
--------------------------------------------------------------------------------------------------------------

    213: #logger_custom_string.debug(pp_odir(obj,traceback.format_stack(limit=5)))  # This will pretty print all the properties from dir(obj)
    214: 
    215: 
    216: 
    217: doc1 = fitz.open("test.pdf")  # open file 1
 218***: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    219: toc1 = doc1.getToC(False)  # its table of contents (list)
    220: pc1 = len(doc1)  # number of its pages 


{
    "VerFormatter": "<class '__main__.VerFormatter'>",
    "__annotations__": {},
    "__builtins__": "<module 'builtins' (built-in)>",
    "__cached__": null,
    "__doc__": null,
    "__file__": "test.py",
    "__loader__": "<_frozen_importlib_external.SourceFileLoader object at 0x7f17ae731940>",
    "__name__": "__main__",
    "__package__": null,
    "__spec__": null,
    "anything": "<function anything at 0x7f17ae7aa1e0>",
    "doc1": "Document('test.pdf')",
    "exposed_request": null,
    "fitz": "<module 'fitz' from '/usr/lib/python3.7/site-packages/fitz/__init__.py'>",
    "formatter": "<__main__.VerFormatter object at 0x7f17ae633b00>",
    "handler": "<StreamHandler <stderr> (DEBUG)>",
    "json_dumps_default": "<function json_dumps_default at 0x7f17ae1a6840>",
    "keys_string": "<function keys_string at 0x7f17ae1a67b8>",
    "logger_custom_string": "<Logger custom_string (DEBUG)>",
    "logging": "<module 'logging' from '/usr/lib/python3.7/logging/__init__.py'>",
    "pp_odir": "<function pp_odir at 0x7f17ae1a6950>",
    "pp_odir_getobject": "<function pp_odir_getobject at 0x7f17ae1a68c8>",
    "pp_traceback": "<function pp_traceback at 0x7f17ae1a69d8>",
    "traceback": "<module 'traceback' from '/usr/lib/python3.7/traceback.py'>"
}


  File "test.py", line 218, in <module>
    logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))


    213: #logger_custom_string.debug(pp_odir(obj,traceback.format_stack(limit=5)))  # This will pretty print all the properties from dir(obj)
    214: 
    215: 
    216: 
    217: doc1 = fitz.open("test.pdf")  # open file 1
 218***: logger_custom_string.debug(pp_odir(locals(),traceback.format_stack(limit=5)))
    219: toc1 = doc1.getToC(False)  # its table of contents (list)
    220: pc1 = len(doc1)  # number of its pages 
```

Here we can see the locals() and also the line where the logging is called and also stacktrace. This will help
in debugging the values

