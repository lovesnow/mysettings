# sample ipython config.py
#

c= get_config()

c.TerminalIPythonApp.display_banner = False
#c.InteractiveShellApp.log_level = 20
#c.InteractiveShellApp.extensions = [
#    'myextension'
#]

c.InteractiveShellApp.exec_lines = [
    'import os',
    'import sys'
]


#c.InteractiveShellApp.exec_files = [
#    'mycode.py',
#    'fancy.ipy'
#]

c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.deep_reload = True
c.InteractiveShell.editor = 'emacsclient'
c.InteractiveShell.xmode = 'Context'

c.PromptManager.in_template  = 'In [\#]: '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = 'Out[\#]: '
#c.PromptManager.in_template = "(\u)-(\W)\n(! \#)-> "
#c.PromptManager.in_template = "(! \#)-> "
#c.PromptManager.in2_template = '   .\D.: '
#c.PromptManager.out_template = ""
c.PromptManager.justify = False

c.PrefilterManager.multi_line_specials = True

#c.AliasManager.user_aliases = [
# ('la', 'ls -al')
#]
