# 🚗 Parking Slot Management System

A web-based **Parking Slot Management System (PSM)** developed using **Python Flask and MySQL** to efficiently manage parking slots, vehicle registrations, bookings, parking entry and exit, users, staff, and parking history.

The system provides separate dashboards and functionalities for **Admin, Staff, and Users**, making parking operations easier, more organized, and efficient.

---

## 📌 Project Overview

Managing parking manually can lead to problems such as:

* Difficulty finding available parking slots
* Manual recording of vehicle entry and exit
* Duplicate or incorrect parking records
* Difficulty tracking occupied and available slots
* Time-consuming fee calculation
* Lack of proper parking history
* Difficulty managing users and staff

The **Parking Slot Management System** solves these problems by providing a centralized web application for managing the complete parking process digitally.

---

## 🎯 Objectives

The main objectives of this project are:

* To manage parking slots efficiently.
* To display available and occupied parking slots.
* To allow users to register their vehicles.
* To provide online parking slot booking.
* To manage vehicle entry and exit.
* To maintain parking records and history.
* To calculate parking fees based on parking duration.
* To provide separate dashboards for Admin, Staff, and Users.
* To reduce manual work and improve parking management.

---

## 👥 User Roles

### 👨‍💼 Admin

The Admin manages the overall parking system.

**Admin functionalities:**

* Admin Dashboard
* Manage Users
* Manage Staff
* Manage Parking Slots
* View Parking Records
* View Bookings
* Monitor Vehicle Entry/Exit
* Manage Parking Information
* View System Statistics

---

### 👷 Staff

Staff members handle day-to-day parking operations.

**Staff functionalities:**

* Staff Dashboard
* Vehicle Entry
* Vehicle Exit
* Search Vehicles
* View Parking Slots
* Manage Parking Records
* View Parking History
* Check Booking Information
* Update Parking Status

---

### 👤 User

Users can manage their vehicles and parking bookings.

**User functionalities:**

* User Dashboard
* Register Vehicle
* Book Parking Slot
* View My Bookings
* View Parking History
* View Profile
* Check Parking Slot Availability
* View Parking Details

---

## ⚙️ Main Features

### 🅿️ Parking Slot Management

The system maintains parking slots based on vehicle type:

* 🏍️ Bike
* 🚗 Car
* 🚚 Truck

Each parking slot has a status:

* `Available`
* `Occupied`

When a vehicle enters, the selected slot becomes **Occupied**.

When the vehicle exits, the slot becomes **Available** again.

---

### 🚘 Vehicle Registration

Users can register their vehicles in the system.

Vehicle information can include:

* Vehicle Number
* Vehicle Type
* User Details
* Registration Information

---

### 📅 Slot Booking

Users can book an available parking slot.

The system:

1. Displays available slots.
2. Allows the user to select a suitable slot.
3. Creates a booking record.
4. Associates the booking with the user's vehicle.
5. Updates parking information.

---

### 🚪 Vehicle Entry

Staff can manage vehicle entry.

The system records:

* Vehicle Number
* Vehicle Type
* Parking Slot
* Entry Time
* Parking Status

After successful entry, the selected parking slot is updated from:

`Available → Occupied`

---

### 🚗 Vehicle Exit

Staff can process vehicle exits.

The system:

1. Finds the parked vehicle.
2. Calculates parking duration.
3. Calculates the parking fee.
4. Records the exit time.
5. Updates the parking record.
6. Changes the parking slot status.

The slot is updated from:

`Occupied → Available`

---

### 💰 Parking Fee Calculation

The system calculates the parking fee based on the duration of parking.

The basic process is:

```text
Entry Time
     ↓
Exit Time
     ↓
Calculate Parking Duration
     ↓
Calculate Parking Fee
     ↓
Store Fee in Database
```

---

### 📊 Dashboard

The dashboard provides useful information such as:

* Total Parking Slots
* Available Slots
* Occupied Slots
* Total Vehicles
* Active Bookings
* Parking Records

This allows users and staff to quickly understand the current parking status.

---

### 📜 Parking History

The system maintains previous parking records.

History can contain:

* Vehicle Number
* Vehicle Type
* Slot Number
* Entry Time
* Exit Time
* Parking Duration
* Parking Fee
* Parking Status

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* Jinja2 Templates

### Backend

* Python
* Flask

### Database

* MySQL

### Development Tools

* Visual Studio Code
* Git
* GitHub
* MySQL Workbench

---

## 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │       User          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   HTML / CSS /      │
                 │   JavaScript /      │
                 │   Bootstrap         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Flask          │
                 │      Backend        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       MySQL         │
                 │      Database       │
                 └─────────────────────┘
```

---

## 🗄️ Database

The project uses **MySQL** for storing application data.

Important tables include:

### `parking_slots`

Stores parking slot information.

| Field        | Description          |
| ------------ | -------------------- |
| id           | Unique slot ID       |
| slot_number  | Parking slot number  |
| vehicle_type | Bike / Car / Truck   |
| status       | Available / Occupied |

Example:

```text
B1 → Bike → Available
B2 → Bike → Occupied
C1 → Car  → Available
C2 → Car  → Occupied
T1 → Truck → Available
```

---

### `parking_records`

Stores vehicle parking information.

| Field          | Description                 |
| -------------- | --------------------------- |
| id             | Record ID                   |
| vehicle_number | Vehicle registration number |
| vehicle_type   | Bike / Car / Truck          |
| slot_id        | Assigned parking slot       |
| entry_time     | Vehicle entry time          |
| exit_time      | Vehicle exit time           |
| parking_fee    | Calculated parking fee      |
| status         | Parked / Exited             |

---

## 📂 Project Structure

```text
Smart-Parking-Slot-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   │
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── users.html
│   │   ├── staff.html
│   │   └── slots.html
│   │
│   ├── staff/
│   │   ├── dashboard.html
│   │   ├── vehicle_entry.html
│   │   ├── vehicle_exit.html
│   │   └── history.html
│   │
│   └── user/
│       ├── dashboard.html
│       ├── book_slot.html
│       ├── my_bookings.html
│       ├── register_vehicle.html
│       ├── parking_history.html
│       ├── profile.html
│       └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── database/
    └── parking_management.sql
```

---

## 🔄 System Workflow

### User Workflow

```text
User Registration
       ↓
Login
       ↓
User Dashboard
       ↓
Register Vehicle
       ↓
Check Available Slots
       ↓
Book Slot
       ↓
View Booking
       ↓
Parking Entry
       ↓
Parking Exit
       ↓
Parking History
```

### Staff Workflow

```text
Staff Login
     ↓
Staff Dashboard
     ↓
Check Booking / Vehicle
     ↓
Vehicle Entry
     ↓
Assign Parking Slot
     ↓
Slot = Occupied
     ↓
Vehicle Exit
     ↓
Calculate Fee
     ↓
Update Parking Record
     ↓
Slot = Available
```

### Admin Workflow

```text
Admin Login
     ↓
Admin Dashboard
     ↓
Manage Users
Manage Staff
Manage Slots
View Bookings
View Parking Records
     ↓
Monitor Parking System
```

---

## 🔐 Environment Variables

For deployment, database credentials are stored using environment variables instead of directly writing sensitive credentials in the source code.

Example:

```env
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=parking_management
DB_PORT=3306
```

The application uses `python-dotenv` to load environment variables.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Parking-Slot-Management-System.git
```

### 2. Open the Project

```bash
cd Smart-Parking-Slot-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create the database:

```sql
CREATE DATABASE parking_management;
```

Then create the required tables using the SQL file provided in the project.

---

### 7. Configure `.env`

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=parking_management
DB_PORT=3306
```

---

### 8. Run the Application

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000/
```

---

## 📱 Responsive Design

The system uses **Bootstrap, CSS, and responsive layouts** to provide a user-friendly interface across different screen sizes.

The interface includes:

* Navigation bar
* Dashboard cards
* Tables
* Forms
* Booking pages
* Vehicle entry/exit pages
* History cards
* Profile pages

---

## 🧪 Testing

The application can be tested for:

* User registration
* User login
* Staff login
* Admin login
* Vehicle registration
* Slot availability
* Slot booking
* Vehicle entry
* Vehicle exit
* Parking fee calculation
* Parking history
* Slot status updates
* Database operations
* Role-based access

---

## 📈 Future Enhancements

The project can be extended with:

* 📍 Real-time parking slot availability
* 📱 Mobile application
* 💳 Online payment integration
* 📧 Email notifications
* 📲 SMS notifications
* 🔔 Booking reminders
* 📊 Advanced analytics dashboard
* 🧾 Automatic receipt generation
* 📷 Number plate recognition
* 🔐 OTP-based authentication
* 🗺️ Parking location/map integration
* 📡 IoT-based smart parking sensors

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Flask web development
* MySQL database management
* CRUD operations
* Jinja templating
* HTML/CSS/JavaScript
* Bootstrap
* Database connectivity
* Form handling
* Session management
* Role-based access
* Parking slot management logic
* Fee calculation
* Git and GitHub
* Deployment concepts

---

## 💡 Challenges Faced

Some of the major challenges during development included:

* Managing parking slot availability.
* Keeping slot status synchronized with vehicle entry and exit.
* Filtering slots according to vehicle type.
* Calculating parking duration and fees.
* Maintaining relationships between parking slots and parking records.
* Handling MySQL foreign key relationships.
* Managing database credentials securely during deployment.
* Designing separate dashboards for different user roles.

---

## 👨‍💻 Developer

**Goutham Gurrapu**

B.Tech – Information Technology
Malla Reddy University, Hyderabad, Telangana

### Technologies

`Python` `Flask` `MySQL` `HTML` `CSS` `JavaScript` `Bootstrap` `Jinja`

---

## ⭐ Project Highlights

```text
✓ Role-Based Parking Management
✓ Parking Slot Management
✓ Vehicle Registration
✓ Slot Booking
✓ Vehicle Entry & Exit
✓ Parking Fee Calculation
✓ Parking History
✓ MySQL Database
✓ Flask Backend
✓ Responsive UI
✓ Jinja Templates
✓ Bootstrap Design
```

---

## 📄 License

This project was developed for **academic and learning purposes**.
