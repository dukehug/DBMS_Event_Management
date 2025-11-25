2025-11-24 18:42

Tags:  #SQL 

---
SQL Query

````sql
```sql
-- 11/25/2025 Update
-- =============================================
-- 1. Table: Location
-- Parent table, created first.
-- =============================================
CREATE TABLE [Location] (
    -- PK: Auto-increment
    [location_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    [loc_name] VARCHAR(255) NOT NULL,
    [loc_address] VARCHAR(255),
    
    -- Capacity in ERD is string, keeping as VARCHAR
    [loc_capacity] VARCHAR(50), 
    [loc_status] VARCHAR(50),
    [loc_type] VARCHAR(50),
    [loc_contact_person] VARCHAR(100),
    
<<<<<<< HEAD
    -- Changed from INT to VARCHAR to handle leading zeros and formatting
    [loc_contact_phone] VARCHAR(50) 
=======
    -- Change to VARCHAR
    [loc_contact_phone] VARCHAR(50)
>>>>>>> 5f37323087f6b40cdffe5741a9ebaeb13cf52cc5
);

-- =============================================
-- 2. Table: Person
-- Parent table, created early.
-- ** KEY CHANGE **: PK is national_id, manual entry, CHAR(16).
-- =============================================
CREATE TABLE [Person] (
    -- PK: 16-digit fixed length string. NO IDENTITY (Manual Input).
    [national_id] CHAR(16) NOT NULL PRIMARY KEY,
    
    [first_name] VARCHAR(100),
    [mid_name] VARCHAR(100),
    [last_name] VARCHAR(100), 
<<<<<<< HEAD
    
=======
>>>>>>> 5f37323087f6b40cdffe5741a9ebaeb13cf52cc5
    [gender] VARCHAR(20),
    [age] INT,
    [phone] VARCHAR(50),
    [email] VARCHAR(100),
    [person_address] VARCHAR(255)
);

-- =============================================
-- 3. Table: Event
-- Depends on Location.
-- =============================================
CREATE TABLE [Event] (
    -- PK: Auto-increment
    [event_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- FK: Links to Location
    [location_id] INT,
    
    -- Corrected likely typo 'env_name' to 'evn_name' for consistency, or keep as env per ERD
    [evn_name] VARCHAR(255),
    [evn_start_date] DATETIME,
    [evn_end_date] DATETIME,
    [evn_organizer] VARCHAR(100),
<<<<<<< HEAD
    [evn_description] VARCHAR(MAX), -- Using MAX for descriptions
=======
    [evn_description] VARCHAR(MAX), 
>>>>>>> 5f37323087f6b40cdffe5741a9ebaeb13cf52cc5
    [evn_type] VARCHAR(50),
    
    -- Constraint
    CONSTRAINT [fk_event_location] FOREIGN KEY ([location_id]) 
    REFERENCES [Location]([location_id])
);

-- =============================================
-- 4. Table: Event_registration
-- Associative Entity. Depends on Event and Person.
-- =============================================
CREATE TABLE [Event_registration] (
    -- PK: Auto-increment
    [event_register_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- FKs
    [event_id] INT,
    [national_id] CHAR(16), -- Must match Person PK exactly
    
    -- Boolean in MSSQL is BIT (0 or 1)
    [register_confirm] BIT, 
    [at_role] VARCHAR(50),
    
    -- Constraints
    CONSTRAINT [fk_registration_event] FOREIGN KEY ([event_id]) 
    REFERENCES [Event]([event_id]),
    
    CONSTRAINT [fk_registration_person] FOREIGN KEY ([national_id]) 
    REFERENCES [Person]([national_id])
);

-- =============================================
-- 5. Table: Attendance_Records
-- Depends on Event_registration.
-- =============================================
CREATE TABLE [Attendance_Records] (
    -- PK: Auto-increment
    [record_id] INT IDENTITY(1,1) PRIMARY KEY,
    
    -- FK: Links to the registration record
    [event_register_id] INT,
    
    [attendance_date] DATETIME,
    [at_status] VARCHAR(50),
    
    -- Constraint
    CONSTRAINT [fk_record_registration] FOREIGN KEY ([event_register_id]) 
    REFERENCES [Event_registration]([event_register_id])
);
```
````



----
References: 
