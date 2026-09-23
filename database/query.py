from database.connection import DatabaseConnection

def insertusersfromsignup(name,email,password,phone):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            insert_users_query="""insert into users (name,email,password,phone) values(%s,%s,%s,%s)"""
            cursor.execute(insert_users_query,(name,email,password,phone))
            connection.commit()
            cursor.close()
            connection.close()
            return True,"rejested succesfully"
        except Exception as e:
            return  False,f"something went wrong in signup {e}"


def selectusersforlogin(email,password):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            login_query="""select * from users where email=%s and password=%s"""
            cursor.execute(login_query,(email,password))
            user=cursor.fetchone()
            cursor.close()
            connection.close()
            if user:
                return True,"login sucessfull",user
            else:
                return False,"invalid email or password",None
        except Exception as e:
            return False,f'something went wrong in login:{e}',None
        
def parking_slots():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            slots_query="select * from parking_slots"
            cursor.execute(slots_query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"Something went wrong in manaing slots {e}"
        
def get_slot_by_id(id):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            slot_id_query="select * from parking_slots where id=%s"
            cursor.execute(slot_id_query,(id,))
            slot=cursor.fetchone()
            cursor.close()
            connection.close()
            return slot
        except Exception as e:
            return f"Something went wrong in manaing slots {e}"
    
    
def add_parking_slot(slot_number,vehicle_type,status):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            add_slot_query="""insert into parking_slots (slot_number,vehicle_type,status) values(%s,%s,%s)"""
            cursor.execute(add_slot_query,(slot_number,vehicle_type,status))
            connection.commit()
            cursor.close()
            connection.close()
            return True,"slot added sucessfully"
        except Exception as e:
            return False,'something went wrong in add slot {e}'
    
    
def update_parking_slot(id,slot_number,vehicle_ytpe,status):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            update_slot_query="""UPDATE parking_slots SET slot_number = %s, vehicle_type = %s, status = %s
            WHERE id = %s"""
            cursor.execute(update_slot_query,(slot_number,vehicle_ytpe,status,id))
            connection.commit()
            cursor.close()
            connection.close()
            return True,"updated Sucessfully"
        except Exception as e:
            return False,f"something went wrong in updating {e}"
        
def delete_parking_slot(id):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            delete_slot_query="""delete from parking_slots where id=%s"""
            cursor.execute(delete_slot_query,(id,))
            connection.commit()
            cursor.close()
            connection.close()
            return True,'deleted succesfully'
        except Exception as e:
            return False,f"something went wrong in delte slot {e}"

def get_users_from_db():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            get_users_query="""select * from users where role = 'user'"""
            cursor.execute(get_users_query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"somthing went wrong in gettting users {e}"
def get_user_by_id(id):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            user_id_query="select * from users where id=%s"
            cursor.execute(user_id_query,(id,))
            user_id=cursor.fetchone()
            cursor.close()
            connection.close()
            return user_id
        except Exception as e:
            return f"Something went wrong in manaing slots {e}"
        
def update_user(id,name,email,phone):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            update_user_query="""UPDATE users SET name = %s, email = %s, phone = %s
            WHERE id = %s"""
            cursor.execute(update_user_query,(name,email,phone,id))
            connection.commit()
            cursor.close()
            connection.close()
            return True,"Updated Sucessfully"
        except Exception as e:
            return False,f"something went wrong in update User: {e}"
def delete_user_from_db(id):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor()
            delete_user_query="""delete from users where id=%s"""
            cursor.execute(delete_user_query,(id,))
            connection.commit()
            cursor.close()
            connection.close()
            return True,'deleted succesfully'
        except Exception as e:
            return False,f"something went wrong in delte user {e}"
def get_parking_records():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            parking_records_query="""select * from parking_records"""
            cursor.execute(parking_records_query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"Something went wrong in user bookings {e}"
        
def get_total_parking_records_details(id):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            get_toatl_records_query="""
                    SELECT
                        pr.id AS record_id,
                        u.id AS user_id,
                        u.name AS user_name,
                        u.phone,
                        v.id AS vehicle_id,
                        v.vehicle_number,
                        v.vehicle_type,
                        ps.id AS slot_id,
                        ps.slot_number,
                        ps.vehicle_type AS slot_vehicle_type,
                        ps.status AS slot_status,
                        pr.entry_time,
                        pr.exit_time,
                        pr.parking_fee,
                        pr.status AS parking_status
                    FROM parking_records pr
                    JOIN users u
                        ON pr.user_id = u.id
                    JOIN vehicles v
                        ON pr.vehicle_id = v.id
                    JOIN parking_slots ps
                        ON pr.slot_id = ps.id where pr.id=%s"""
            cursor.execute(get_toatl_records_query,(id,))
            result=cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"something went wrong in total_recors {e}"
        
def get_vehicle_type_count():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            get_count_query="""SELECT ps.vehicle_type, COUNT(*) AS total
                                FROM parking_records pr
                                JOIN parking_slots ps ON pr.slot_id = ps.id
                                GROUP BY ps.vehicle_type"""
            cursor.execute(get_count_query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"something went wrong in repotrs {e}"
                        
def slots_count_from_db():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            get_count_query="""select status,count(status) as count from parking_slots group by status"""
            cursor.execute(get_count_query)
            result_count=cursor.fetchall()
            cursor.close()
            connection.close()
            return result_count
        except Exception as e:
            return f"something went wrong in repotrs {e}"
        
        
def get_staff_from_db():
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            get_staff_query="""select * from users where role = 'staff'"""
            cursor.execute(get_staff_query)
            result=cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            return f"somthing went wrong in gettting staff {e}"
        

def get_vehicle_by_number(vehicle_number):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            vehicle_number_query="""select * from vehicles where vehicle_number=%s"""
            cursor.execute(vehicle_number_query,(vehicle_number,))
            result=cursor.fetchone()
            return result
        except Exception as e:
            return f"somthing went wrong in register vehicle {e}"
    
def get_parking_slots_by_type(vehicle_type):
    connection=DatabaseConnection()
    if connection=="Connection Failed":
        return "connection Failed"
    else:
        try:
            cursor=connection.cursor(dictionary=True)
            vehicle_type_query="""select * from parking_slots where vehicle_type=%s and status='Available'"""
            cursor.execute(vehicle_type_query,(vehicle_type,))
            result=cursor.fetchall()
            return result
        except Exception as e:
            return f"something went wrong in getting slots {e}"
    
    
        
    