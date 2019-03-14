Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first_name= "Consolata"
>>> balance=1000
>>> hello "first_name {} + your balance is ksh {}"
SyntaxError: invalid syntax
>>> first_name="consolata"
>>> balance="1ooo"
>>> sms="hello {} ,\n your balance is {} ".format(first_name,balance)
>>> print(sms)
hello consolata ,
 your balance is 1ooo 
>>> first_name='anto'
>>> balance='10000'
>>> sms='hello {} ,\n your balance is {} '.format(first_name,balance)
>>> print(sms)
hello anto ,
 your balance is 10000 
>>> a='car'
>>> a
'car'
>>> type(a)
<class 'str'>
>>> b=10
>>> type(b)
<class 'int'>
>>> s='AkiraChix'
>>> type(s)
<class 'str'>
>>> s.upper()
'AKIRACHIX'
>>> s.lower.()
SyntaxError: invalid syntax
>>> s.lower()
'akirachix'
>>> s.capitalize()
'Akirachix'
>>> s.endswith('x')
True
>>> s.endswith('k)
	       
SyntaxError: EOL while scanning string literal
>>> s.endswith('k))
	       
SyntaxError: EOL while scanning string literal
>>> s.endswith('k')
	       
False
>>> s.startswith('a')
	       
False
>>> s.startswith('A')
	       
True
>>> s.startswith('k')
	       
False
>>> s.islower()
	       
False
>>> b=s.lower()
	       
>>> b.islower()
	       
True
>>> b
	       
'akirachix'
>>> b.isupper
	       
<built-in method isupper of str object at 0x016FC6B0>
>>> b=s.upper
	       
>>> b.isupper
	       
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.isupper
AttributeError: 'builtin_function_or_method' object has no attribute 'isupper'
>>> b=s.upper()
	       
>>> b.isupper
	       
<built-in method isupper of str object at 0x0171E700>
>>> b.isupper()
	       
True
>>> b=s.alpha()
	       
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b=s.alpha()
AttributeError: 'str' object has no attribute 'alpha'
>>> b.alpha()
	       
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.alpha()
AttributeError: 'str' object has no attribute 'alpha'
>>> b.isalpha()
	       
True
>>> b.isalnum
	       
<built-in method isalnum of str object at 0x0171E700>
>>> b.isalnum()
	       
True
>>> s.replace('x','z')
	       
'AkiraChiz'
>>> s.replace('z','x')
	       
'AkiraChix'
>>> s.replace('a','b')
	       
'AkirbChix'
>>> s[0]
	       
'A'
>>> s[4]
	       
'a'
>>> s[7]
	       
'i'
>>> s[8]
	       
'x'
>>> s[-9]
	       
'A'
>>> s[-1]
	       
'x'
>>> s[-6]
	       
'r'
>>> len(s)
	       
9
>>> s[0:4]
	       
'Akir'
>>> s[2:7]
	       
'iraCh'
>>> s[5:8]
	       
'Chi'
>>> s[5:9]
	       
'Chix'
>>> s[5:10]
	       
'Chix'
>>> s[3:]
	       
'raChix'
>>> s[:4]
	       
'Akir'
>>> s[-9:-6]
	       
'Aki'
>>> s[-9:-5]
	       
'Akir'
>>> s[0:4]==s[-9:-5]
	       
True
>>> s[-4:-2]
	       
'Ch'
>>> s[-4:-1]
	       
'Chi'
>>> s[5:8]==s[-4:-1]
	       
True
>>> s[-5:-1]
	       
'aChi'
>>> s[-1:-5]
	       
''
>>> s[-4:-0]
	       
''
>>> s[-4:]
	       
'Chix'
>>> s[5:9]==s[-4:]
	       
True
>>> s[-6:]
	       
'raChix'
>>> s[3:]
	       
'raChix'
>>> s[:-5]
	       
'Akir'
>>> s[:4]==s[:-5]
	       
True
>>> s[0:4]==s[-9:-5]
	       
True
>>> first_name='poison'
	       
>>> second_name='ivy'
	       
>>> full_name='{} {}'.format(first_name,second_name)
	       
>>> full_name
	       
'poison ivy'
>>> a=full_name[:-4]
	       
>>> a
	       
'poison'
>>> a==first_name
	       
True
>>> b=full_name[0:2]
	       
>>> b
	       
'po'
>>> b=full_name[-3:]
	       
>>> b
	       
'ivy'
>>> b==second_name
	       
True
>>> 
	       
>>> help()
	       

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> symbols
	       
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    symbols
NameError: name 'symbols' is not defined
>>> symbols()
	       
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    symbols()
NameError: name 'symbols' is not defined
>>> sym
	       
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    sym
NameError: name 'sym' is not defined
>>> help()
	       

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          atexit              http                scrolledlist
__main__            audioop             hyperparser         search
_abc                autocomplete        idle                searchbase
_ast                autocomplete_w      idle_test           searchengine
_asyncio            autoexpand          idlelib             secrets
_bisect             base64              imaplib             select
_blake2             bdb                 imghdr              selectors
_bootlocale         binascii            imp                 setuptools
_bz2                binhex              importlib           shelve
_codecs             bisect              inspect             shlex
_codecs_cn          browser             io                  shutil
_codecs_hk          builtins            iomenu              signal
_codecs_iso2022     bz2                 ipaddress           site
_codecs_jp          cProfile            itertools           smtpd
_codecs_kr          calendar            json                smtplib
_codecs_tw          calltip             keyword             sndhdr
_collections        calltip_w           lib2to3             socket
_collections_abc    cgi                 linecache           socketserver
_compat_pickle      cgitb               locale              sqlite3
_compression        chunk               logging             squeezer
_contextvars        cmath               lzma                sre_compile
_csv                cmd                 macosx              sre_constants
_ctypes             code                macpath             sre_parse
_ctypes_test        codecontext         mailbox             ssl
_datetime           codecs              mailcap             stackviewer
_decimal            codeop              mainmenu            stat
_dummy_thread       collections         marshal             statistics
_elementtree        colorizer           math                statusbar
_functools          colorsys            mimetypes           string
_hashlib            compileall          mmap                stringprep
_heapq              concurrent          modulefinder        struct
_imp                config              msilib              subprocess
_io                 config_key          msvcrt              sunau
_json               configdialog        multicall           symbol
_locale             configparser        multiprocessing     symtable
_lsprof             contextlib          netrc               sys
_lzma               contextvars         nntplib             sysconfig
_markupbase         copy                nt                  tabnanny
_md5                copyreg             ntpath              tarfile
_msi                crypt               nturl2path          telnetlib
_multibytecodec     csv                 numbers             tempfile
_multiprocessing    ctypes              opcode              test
_opcode             curses              operator            textview
_operator           dataclasses         optparse            textwrap
_osx_support        datetime            os                  this
_overlapped         dbm                 outwin              threading
_pickle             debugger            paragraph           time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple formatter           pydoc_data          weakref
_testmultiphase     fractions           pyexpat             webbrowser
_thread             ftplib              pyparse             window
_threading_local    functools           pyshell             winreg
_tkinter            gc                  query               winsound
_tracemalloc        genericpath         queue               wsgiref
_warnings           getopt              quopri              xdrlib
_weakref            getpass             random              xml
_weakrefset         gettext             re                  xmlrpc
_winapi             glob                redirector          xxsubtype
abc                 grep                replace             zipapp
aifc                gzip                reprlib             zipfile
antigravity         hashlib             rlcompleter         zipimport
argparse            heapq               rpc                 zlib
array               help                rstrip              zoomheight
ast                 help_about          run                 zzdummy
asynchat            history             runpy               
asyncio             hmac                runscript           
asyncore            html                sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
