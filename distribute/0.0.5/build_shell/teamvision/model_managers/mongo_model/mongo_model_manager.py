#coding=utf-8
'''
Created on 2015-10-22

@author: zhangtiande
'''


from gatesidelib.mongodb_helper import MongodbHelper
from teamvision.gatesidelib.common.simplelogger import SimpleLogger


class MongoFileManager(object):
    
    def __init__(self,host,port,db,collection):
        self.host=host
        self.port=port
        self.collection=collection
        self.db=db
    
    def get(self,file_id):
        mongo_helper=MongodbHelper(self.host,self.port)
        grid_out=mongo_helper.get_file_bucket(self.db, self.collection, file_id)
        return grid_out

    def get_value(self,doc_id):
        mongo_helper=MongodbHelper(self.host,self.port)
        grid_out=mongo_helper.get(self.db, self.collection, doc_id)
        return grid_out

    def save_value(self,value):
        mongo_helper=MongodbHelper(self.host,self.port)
        doc_id=mongo_helper.save(self.db, self.collection, value)
        return doc_id

    def update_value(self,doc_id,value):
        mongo_helper=MongodbHelper(self.host,self.port)
        doc_id=mongo_helper.update(self.db, self.collection,doc_id,value)
        return doc_id
        
    
    def get_by_filename(self,file_name):
        pass
    
    def save(self,file_bytes,file_property):
        mongo_helper=MongodbHelper(self.host,self.port)
        file_id=mongo_helper.put_file(self.db,self.collection,file_bytes,file_property)
        return file_id
    
    def delete_file(self,file_id):
        try:
            mongo_helper=MongodbHelper(self.host,self.port)
            mongo_helper.delete_file(self.db,self.collection, file_id)
        except Exception as ex:
            SimpleLogger.exception(ex)
    
    def delete_value(self,file_id):
        mongo_helper=MongodbHelper(self.host,self.port)
        file_id=mongo_helper.remove(self.db,self.collection, file_id)
        return file_id
    
    def save_bucket(self,file_chunks,file_name,file_property):
        mongo_helper=MongodbHelper(self.host,self.port)
        file_bucket_fs=mongo_helper.pub_file_bucket(self.db,self.collection,file_name,file_property)
        for chunk in file_chunks:
            file_bucket_fs.write(chunk)
        file_bucket_fs.close()
        return file_bucket_fs._id
    
    def copy_bucket(self,grid_out):
        mongo_helper=MongodbHelper(self.host,self.port)
        file_bucket_fs=mongo_helper.pub_file_bucket(self.db,self.collection,grid_out.name,grid_out.metadata)
        while True:
            chunk=grid_out.read(size=1024*1024*10)
            if chunk:
                file_bucket_fs.write(chunk)
            else:
                break
        file_bucket_fs.close()
        return file_bucket_fs._id
        

    def save_content(self,content,file_name,file_property):
        mongo_helper=MongodbHelper(self.host,self.port)
        file_bucket_fs=mongo_helper.pub_file_bucket(self.db,self.collection,file_name,file_property)
        file_bucket_fs.write(content.encode(encoding="utf-8"))
        file_bucket_fs.close()
        return file_bucket_fs._id
        
    

    
