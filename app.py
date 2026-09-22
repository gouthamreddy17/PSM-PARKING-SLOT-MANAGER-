from database.connection import DatabaseConnection
from flask import Flask,render_template,request,redirect,url_for,session
from database.query import *
app=Flask(__name__)

app.secret_key = "psm_secret_key"
connection=DatabaseConnection()
if connection=="Connection Failed":
    print("failed")
else:
    print("connected")
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        name= request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        phone=request.form.get('phone')
        confirmpassword=request.form.get('confirmpassword')
        
        if password !=confirmpassword:
            return render_template('signup.html',msg="password not match")
        result,msg=insertusersfromsignup(name=name,email=email,password=password,phone=phone)
        print(result,msg)
        if result==True:
            return render_template('login.html',msg=msg)
        else:
            return render_template('signup.html',msg=msg)
        
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        email=request.form.get('email')
        password=request.form.get('password')
        result,msg,user=selectusersforlogin(email=email,password=password)
        if result==True:
            session['user']=user
            print("USER DATA:", user)
            print("USERNAME:", user['name'])
            if user['role']=='admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role']=='user':
                return redirect(url_for('user_dashboard'))
            elif user['role']=='staff':
                return redirect(url_for('user_dashboard'))
        else:
            return render_template('login.html',msg=msg)

        
        
        
        
@app.route('/user/user_dashboard')
def user_dashboard():
    user=session.get('user')
    return render_template('user_dashboard.html',user=user)
@app.route('/admin/admin_dashboard')
def admin_dashboard():
    user=session.get('user')
    return render_template('admin_dashboard.html',user=user)
@app.route('/admin/manage_slots')
def manage_slots():
    user=session.get('user')
    result=parking_slots()
    print(result)
    return render_template('manage_slots.html',user=user,result=result)

@app.route('/admin/add_slot',methods=['GET','POST'])
def add_slot():
    user=session.get('user')
    if request.method=="GET":
        return render_template('add_slot.html',user=user)
    else:
        slot_number=request.form.get('slot_number')
        vehicle_type=request.form.get('type')
        status=request.form.get('status')
        result,msg=add_parking_slot(slot_number=slot_number,vehicle_type=vehicle_type,status=status)
        if result==True:
            return redirect(url_for('manage_slots'))
        else:
            return render_template('add_slot.html',msg=msg)
@app.route('/admin/edit_slot/<int:id>',methods=['GET','POST'])
def edit_slot(id):
    user=session.get('user')
    if request.method=='GET':
        slot=get_slot_by_id(id)
        return render_template('edit_slot.html',slot=slot,user=user)
    else:
        slot_number=request.form.get('slot_number')
        vehicle_type=request.form.get('type')
        status=request.form.get('status')
        result,msg=update_parking_slot(id,slot_number,vehicle_type,status)
        if result==True:
            return redirect(url_for('manage_slots'))
        else:
            slot=get_slot_by_id(id)
            return render_template('edit_slot.html',slot=slot,user=user,msg=msg)
        
        
@app.route('/admin/manage_slots/delete_slot/<int:id>',methods=['GET','POST'])
def delete_slot(id):
    user=session.get('user')
    if request.method=='GET':
        slot=get_slot_by_id(id)
        return render_template('delete_slot.html',slot=slot,user=user)
    else:
        result,msg=delete_parking_slot(id)
        if result==True:
            return redirect(url_for('manage_slots'))
        else:
            slot=get_slot_by_id(id)
            return render_template('delete_slot.html',slot=slot,user=user,msg=msg)
@app.route('/admin/manage_users')
def manage_users():
    user=session.get('user')
    result=get_users_from_db()
    print(result)
    return render_template('manage_users.html',user=user,result=result)

@app.route('/admin/manage_users/register_user',methods=['GET','POST'])
def register_user():
    user=session.get('user')
    if request.method=='GET':
        
        return render_template('register_user.html',user=user)
    else:
        name= request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        phone=request.form.get('phone')
        confirmpassword=request.form.get('confirmpassword')
        
        if password !=confirmpassword:
            return render_template('register_user.html',user=user,msg="password not match")
        result,msg=insertusersfromsignup(name=name,email=email,password=password,phone=phone)
        print(result,msg)
        if result==True:
            return render_template('manage_users.html',user=user,msg=msg)
        else:
            return render_template('register_user.html',user=user,msg=msg)
@app.route('/admin/manage_users/edit_user/<int:id>',methods=['GET','POST'])
def edit_user(id):
    user=session.get('user')
    user_id=get_user_by_id(id)
    if request.method=="GET":
        return render_template('edit_user.html',user_id=user_id,user=user)
    else:
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        result,msg=update_user(id,name,email,phone)
        if result==True:
            return redirect(url_for('manage_users'))
        else:
            user_id=get_user_by_id(id)
            return render_template('edit_user.html',user_id=user_id,msg=msg,user=user)
@app.route('/admin/manage_users/delete_user/<int:id>',methods=['GET','POST'])
def delete_user(id):
    user=session.get('user')
    
    if request.method=='GET':
        user_id=get_user_by_id(id)
        return render_template('delete_user.html',user_id=user_id,user=user)
    else:
        result,msg=delete_user_from_db(id)
        if result==True:
            return redirect(url_for('manage_users'))
        else:
            user_id=get_user_by_id(id)
            return render_template('delete_user.html',user_id=user_id,msg=msg,user=user)
      
@app.route('/admin/view_bookings')
def view_bookings():
    user=session.get('user')
    result=get_parking_records()
    return render_template('view_bookings.html',user=user,result=result)  

@app.route('/admin/view_bookings/view_booking_details/<int:id>')
def view_booking_details(id):
    user=session.get('user')
    result=get_total_parking_records_details(id)
    return render_template('view_booking_details.html',user=user,result=result) 

@app.route('/admin/reports')
def reports():
    user=session.get('user')
    result=get_vehicle_type_count()
    print(result)
    result_count=slots_count_from_db()
    return render_template('reports.html',user=user,result=result,result_count=result_count) 

    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)