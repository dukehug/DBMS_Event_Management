2025-11-24 18:42

Tags:  #SQL 

---
SQL Query

```sql
--SQL query Language

-- Create Location table
CREATE TABLE [Location] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [location_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Location details
    [loc_name] VARCHAR(255) NOT NULL,
    [loc_address] VARCHAR(255),
    
    -- Capacity and details
    [loc_capacity] VARCHAR(50), 
    [loc_status] VARCHAR(50),
    [loc_type] VARCHAR(50),
    [loc_contact_person] VARCHAR(100),
    
    -- Change to VARCHAR
    [loc_contact_phone] VARCHAR(50)
);

-- Create Person table
CREATE TABLE [Person] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [person_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Personal details
    [first_name] VARCHAR(100),
    [mid_name] VARCHAR(100),
    [last_name] VARCHAR(100), 
    [gender] VARCHAR(20),
    [age] INT,
    
    -- Contact info
    [phone] VARCHAR(50),
    [email] VARCHAR(100),
    [person_address] VARCHAR(255)
);


-- Create Event table
CREATE TABLE [Event] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [event_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Foreign Key: Links to Location table
    [location_id] INT,
    
    -- Event details
    [evn_name] VARCHAR(255),
    [evn_start_date] DATETIME,
    [evn_end_date] DATETIME,
    [evn_organizer] VARCHAR(100),
    [evn_description] VARCHAR(MAX), 
    [evn_type] VARCHAR(50),
    
    -- Define Foreign Key Constraint
    CONSTRAINT [fk_event_location] FOREIGN KEY ([location_id]) 
    REFERENCES [Location]([location_id])
);


-- Create Event_Attendee table
CREATE TABLE [Event_Attendee] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [event_attendee_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Foreign Keys
    [event_id] INT,
    [person_id] INT,
    
    -- Attendance details
    -- MSSQL uses BIT for boolean values (0 = False, 1 = True)
    [attendance_confirm] BIT, 
    [at_role] VARCHAR(50),
    
    -- Define Foreign Key Constraints
    CONSTRAINT [fk_attendee_event] FOREIGN KEY ([event_id]) 
    REFERENCES [Event]([event_id]),
    
    CONSTRAINT [fk_attendee_person] FOREIGN KEY ([person_id]) 
    REFERENCES [Person]([person_id])
);


-- Create Event_Attendee table
CREATE TABLE [Event_Attendee] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [event_attendee_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Foreign Keys
    [event_id] INT,
    [person_id] INT,
    
    -- Attendance details
    -- MSSQL uses BIT for boolean values (0 = False, 1 = True)
    [attendance_confirm] BIT, 
    [at_role] VARCHAR(50),
    
    -- Define Foreign Key Constraints
    CONSTRAINT [fk_attendee_event] FOREIGN KEY ([event_id]) 
    REFERENCES [Event]([event_id]),
    
    CONSTRAINT [fk_attendee_person] FOREIGN KEY ([person_id]) 
    REFERENCES [Person]([person_id])
);


-- Create Attendance_Records table
CREATE TABLE [Attendance_Records] (
    -- Primary Key: Auto-incrementing (Identity) and unique
    [record_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- Foreign Key: Links to the Event_Attendee table
    [event_attendee_id] INT,
    
    -- Record details
    [attendance_date] DATETIME,
    [at_status] VARCHAR(50),
    
    -- Define Foreign Key Constraint
    CONSTRAINT [fk_record_attendee] FOREIGN KEY ([event_attendee_id]) 
    REFERENCES [Event_Attendee]([event_attendee_id])
);
```



----
References: 
