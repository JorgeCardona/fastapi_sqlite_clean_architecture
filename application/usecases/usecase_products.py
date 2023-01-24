from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from domain.interfaces.repositories.repository_products import ProductRepository as repository
from domain.interfaces.business_logic.business_logic_products import ProductsBusinessLogic as business_logic
from domain.interfaces.repositories.repository_products import Session, get_session, Depends, List
from domain.interfaces.repositories.repository_products import get_schema, post_schema, put_schema, patch_schema
from domain.interfaces.repositories.repository_products import model
from configuration.end_points.products import BASE_PATH
from configuration.log.logging import log_api

class ProductsUseCases(repository, business_logic):
    
    def get_response_format(self, data, offset: int = 0, limit: int = 100, page_number : int = 1, page_size : int = 10):
        
        if type(data) == list:
            import math
            start = (page_number - 1) * page_size
            end = start + page_size
            total_data = len(data)
            total_pages = math.ceil(total_data / page_size)
            
            response_data = {
                
                'data':data[start:end],            
                'count':page_size,
                'total':len(data),
                'page': f'{page_number} from {total_pages}',
                'pagination':{
                            'previous':None,
                            'next':None
                            }
            }
                        
            if page_number > 1:
                response_data['pagination']['previous'] = f'{BASE_PATH}/?offset={offset}&limit={limit}&page_number={page_number-1}&page_size={page_size}'
                
            if end < total_data:
                response_data['pagination']['next'] = f'{BASE_PATH}/?offset={offset}&limit={limit}&page_number={page_number+1}&page_size={page_size}'
                 
        elif type(data) == dict:
            response_data = {data} if 'error' not in data else data
            
        else:
            response_data = data
            
        return response_data 
             
    def get_object_list(self, session:Session = Depends(get_session), offset: int = 0, limit: int = 100):
           
        object_ = session.query(model).offset(offset).limit(limit).all()
        return object_
    

    def get_object(self, id:int, session:Session = Depends(get_session)):
        
        object_ = session.query(model).get(id)
        
        if object_:
            return object_ 
        else:
            message = f"Resource with id {id} not found"
            log_api.warning(message)
            
            response = {
                        'error': {
                            'code': status.HTTP_404_NOT_FOUND,
                            'message': message
                        }
            }
            
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)
                        
    def add_object(self, entity:post_schema, session:Session = Depends(get_session)):

        object_data = entity.dict(exclude_unset=True)
        object_ = model(**object_data)

        session.add(object_)
        session.commit()
        session.refresh(object_)
        return object_

    def add_object_list(self, entity:List[post_schema], session:Session = Depends(get_session)):

        list_objects_ = []
        
        for entity_object in entity:
            object_data = entity_object.dict(exclude_unset=True)
            object_ = model(**object_data)
            list_objects_.append(object_)
        
        session.add_all(list_objects_)
        session.commit()
        session.refresh(object_)
        return list_objects_
    
    def __update_rows__(self, id:int, entity:object, session:Session = Depends(get_session)):

        object_ = self.get_object(id=id, session=session)

        if object_.__dict__.get('status_code') != 404:
            object_data = entity.dict(exclude_unset=True)
                
            for key, value in object_data.items():
                setattr(object_, key, value)
            session.add(object_)
            session.commit()
            session.refresh(object_)

        return object_
        
    def update_object(self, id:int, entity:put_schema, session:Session = Depends(get_session)):

        return self.__update_rows__(id=id, entity=entity, session=session)
            
    def patch_object(self, id:int, entity:patch_schema, session:Session = Depends(get_session)):

        return self.__update_rows__(id=id, entity=entity, session=session)

    def delete_object(self, id:int, session:Session = Depends(get_session)):
        
        object_ = self.get_object(id=id, session=session)
             
        if isinstance(object_, model):

            session.delete(object_)
            session.commit()
            session.close()
            
            # delete sqlalchemy key
            object_.__dict__.pop('_sa_instance_state')
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=object_.__dict__)           
            
        else:
            return object_