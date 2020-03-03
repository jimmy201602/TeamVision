# coding=utf-8
'''
Created on 2015-10-23

@author: zhangtiande
'''
from business.business_service import BusinessService
from gatesidelib.common.simplelogger import SimpleLogger
from django.contrib.admin.models import DELETION, CHANGE, ADDITION
from teamvision.home.models import TaskQueue
from teamvision.ci.models import CITaskHistory
from django.contrib.auth.models import User


class CITQService(BusinessService):
    '''
    classdocs
    '''

    @staticmethod
    def update_task_queue_status(tq_id,status,message):
        task_queue = TaskQueue.objects.get(tq_id)
        task_queue.Status = int(status)
        task_queue.ErrorMsg = message
        task_queue.save()

    @staticmethod
    def task_queue_list(command=1, queue_status=(1, 2, 3)):
        return TaskQueue.objects.all().filter(Command=command).filter(Status__in=queue_status).filter(TaskType__in=(1,2,3,4,5))

    @staticmethod
    def start_user(tq_uuid):
        result = "系统"
        try:
            ci_task_history = CITaskHistory.objects.get_history_by_uuid(tq_uuid)
            started_by = User.objects.get(id=ci_task_history.StartedBy)
            result = started_by.last_name + started_by.first_name
        except Exception as ex:
            SimpleLogger.exception(ex)
        return result
