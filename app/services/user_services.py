from app.config.db import users_collection as collection
from pymongo import ReturnDocument
from bson import ObjectId
import bcrypt
import jwt

#___________________________________________________________________________________________________________________

#Get All Users Service
async def get_all_users():
    
    try:

        all_users = list(collection.find({"role": "USER"}))

        if not all_users:
            return {"users": [], "message": "لا يوجد مستخدمين"}
        
        return {"users": all_users}
    
    except Exception as error:
        raise ValueError(str(error))   
#___________________________________________________________________________________________________________________

#Create a New User Service
async def create_user(data):

    try:

        existed_user = collection.find_one({"email": data["email"]})

        if existed_user:
            raise ValueError("المستخدم موجود مسبقا")


        created_user = collection.insert_one(data)

        if created_user:
            return data
        
        else:
            raise ValueError("لا يمكن إنشاء المستخدم")

    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________
    
#Get a User by ID Service
async def get_user(id):

    try:

        object_id = ObjectId(id)

        existed_user = collection.find_one({"_id": object_id})

        if existed_user:
            existed_user
            return existed_user
        
        else:
            raise ValueError("المستخدم غير موجود")
        
    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________
    
#Update User by ID Service
async def update_user(user_data, user_id):

    try:

        existed_user = await get_user(user_id)

        if user_data["name"]:
            existed_user["name"] = user_data["name"]

        if user_data["email"]:
            existed_user["email"] = user_data["email"]

        if user_data["password"]:
            existed_user["password"] = user_data["password"]

        updated_user = collection.find_one_and_update(
            {"_id": existed_user["_id"]}, 
            {"$set": existed_user}, 
            return_document = ReturnDocument.AFTER)
        
        if updated_user:
            return updated_user
        
        else:
            raise ValueError("لا يمكن تحديث المستخدم")
                
    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________
   
#Activate a User By ID Service (Mark as Deleted)
async def activate_user(user_id):

    try:
       
        existed_user = await get_user(user_id)

        if existed_user["is_active"]:
            raise ValueError("المستخدم مفعل مسبقا")

        activated_user = collection.find_one_and_update({"_id": existed_user["_id"]}, {"$set": {"is_active": True}})

        if activated_user:
            return ("تم تفعيل المستخدم بنجاح")
            
        else:
            raise ValueError("المستخدم غير موجود")
    
    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________

#Deactivate a User By ID Service (Mark as Deleted)
async def deactivate_user(user_id):

    try:
       
        existed_user = await get_user(user_id)

        if existed_user["is_active"] == False:
            raise ValueError("المستخدم غير مفعل مسبقا")

        deleted_user = collection.find_one_and_update({"_id": existed_user["_id"]}, {"$set": {"is_active": False}})

        if deleted_user:
            return ("تم إيقاف المستخدم بنجاح")
            
        else:
            raise ValueError("المستخدم غير موجود")
    
    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________

#Login Service
async def login(user):

    try:
        email = user["email"]
        password = user["password"]

        existed_user = collection.find_one({"email": email})

        if not existed_user:
            raise ValueError("المستخدم غير موجود")
        
        if existed_user["is_active"] == False:
            raise ValueError("المستخدم غير مفعل")
        
        password_match = bcrypt.checkpw(password.encode('utf-8'), existed_user["password"].encode('utf-8'))

        if not password_match:
            raise ValueError("كلمة المرور غير صحيحة")
        
        id = str(existed_user["_id"])

        # Generate JWT Token
        token_payload = {"id": id, "role": existed_user["role"]}
        token = jwt.encode(token_payload, "Balkan@123", algorithm = "HS256")

        if token:
            return {"token": token, "id": id, "role": existed_user["role"]}
        
        else:
            raise ValueError("لا يمكن تسجيل الدخول")
    
    except Exception as error:
        raise ValueError(str(error))
#___________________________________________________________________________________________________________________
    
async def create_admin_user():

    existed_admin = collection.find_one({"email": "admin@balkancharity.com"})

    if not existed_admin:

        admin_data = {
            "name": "Admin",
            "email": "admin@balkancharity.com",
            "password": bcrypt.hashpw("Balkan@54%".encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8'),
            "role": "ADMIN",
            "is_active": True,
        }

        collection.insert_one(admin_data)
        print ("Admin User Created")
#___________________________________________________________________________________________________________________