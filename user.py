from models import TimeStampModel
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import Relationship
from models import model

class User(TimeStampModel):
    __tablename__ ='users'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    first_name =  Column(String(100),nullable=False)
    last_name =  Column(String(100),nullable=False)
    email = Column(String(300), nullable=False,unique=True)
    preference = Relationship('Preference',back_populates='user',uselist=False,passive_deletes=True)
    addresses =Relationship('Address',back_populates='user',passive_deletes=True)
    roles =Relationship('Role',secondary='user_roles', back_populates='users',passive_deletes=True)

    def __repr__(self):
        return f'{self. __class__ . __name__},name: {self.first_name} {self.last_name}'
    
class Preference(TimeStampModel):
    __tablename__ ='preference'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    language =  Column(String(100),nullable=False)
    currency =  Column(String(10),nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'), ondelete="CASCADE", nullable=False,index=True,unique=True)
    user =Relationship('User',back_populates='preference')


class Address(TimeStampModel):
    __tablename__ ='addresses'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    road_name =  Column(String(100),nullable=False)    
    postcode =  Column(String(100),nullable=False)    
    city =  Column(String(100),nullable=False) 
    user_id = Column(Integer(), ForeignKey('users.id'), ondelete="CASCADE", nullable=False,index=True)
    user =Relationship('User',back_populates='addresses')
    

    def __repr__(self):
        return f'{self. __class__ . __name__}, name: {self.city}'
    
class Role(model):
    __tablename__ ='roles'
    id = Column(Integer(), primary_key=True,autoincrement=True)
    name =  Column(String(100),nullable=False)    
    slug =  Column(String(100),nullable=False , unique=True)
    users = Relationship ('User', secondary='user_roles', back_populates='roles',passive_deletes=True )
    def __repr__(self):
        return f'{self. __class__ . __name__}, name: {self.name}'
    
class UserRole(TimeStampModel):
    __tablename__ ='user_roles'
    user_id = Column(Integer(), ForeignKey('users.id'), ondelete="CASCADE", primary_key=True)
    role_id = Column(Integer(), ForeignKey('roles.id'), ondelete="CASCADE", primary_key=True)
