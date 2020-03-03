#coding=utf-8
'''
Created on 2016-7-6

@author: Administrator
'''

from teamvision.ci.viewmodels.plugins.vm_ci_plugin import VM_CIPlugin
from business.ci.ci_task_config_service import CITaskConfigService
from teamvision.ci.models import CITaskPlugin
from teamvision.ci.pagefactory.ci_template_path import CIPluginPath

class VM_ShellCommandPlugin(VM_CIPlugin):
    '''
    classdocs
    '''
    plugin_id=3
    
    def __init__(self,plugin_parameter_dict):
        VM_CIPlugin.__init__(VM_ShellCommandPlugin,plugin_parameter_dict)
        self.plugin=CITaskPlugin.objects.get(VM_ShellCommandPlugin.plugin_id)
        self.command_text=self.get_parameter_value('command_text')

    
    def get_template_path(self):
        return CIPluginPath.shell_command
        
        
        
    
    
   
    
    
    
                
        