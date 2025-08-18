# MSMS_project
Music School Management System project - 1056 PST

PST1:
    PST1 is the basic framework for the whole project. It initialises the databases, and there are five main parts.

    1.0: Initialised the project.

    1.1: The blueprint and the data stores. I defined the fundamental data structures, such as classes regarding student IDs, names and lists of instruments, and teacher IDs, names and the instruments they teach. THis first edition is meant to store all data in memory, which means that every time the program stops, the data would be erased. 

    1.2: Core helper functions. In the second part of PST1, I added the building blocks of the systems, implementing the "back end" functions. These included the teacher's name and speciality, a list of students, a list of teachers and functions to find individual students and teachers. 

    1.3: Front desk functions. In part 3, I simulated the high-level functions that a receptionist would use for this database. They have a simple, user-friendly interface that call more detailed functions. The helper functions include finding a student's ID which is required for enrolment, registering an existing student with their names and instruments, lookups for both students and teachers and front desk enrolments.

    1.4: The final part of PST1 was the combination of all the earlier parts to make a full and final interactive menu that users will see. This tied all front desk functions, with a main function that entailed the primary application loop. Inside that loop, there is a clear menu of options for the user, and the user can use all of the options until they enter 'q' and the program exits. 