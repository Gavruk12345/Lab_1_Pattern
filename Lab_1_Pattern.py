from typing import List, Any
import datetime

class Developer:
    """
    Creating a developer class

    Args:
      id: int, name: str, address: str, phone_number: str, email: str, position: int, rank: int,salary: float: its a parameter.

    Returns:
        Returns a value about the execution of the program or false if the program is not executed
    """
    def __init__(self, id: int, name: str, address: str, phone_number: str, email: str, position: int, rank: int, salary: float) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.assignments = []
        self.projects = List[Any] = []
    """
    Creating a project

    Args:project

        Returns:
        Returns a value if added to our user
    """
    def assigned_projects(self) -> List[Any]:
        return self.projects
    """
   Assignment to the project
   
   Args: project
    
    Returns:
        Returns a value if remove to our user
    """
    def assigned(self, project):
        self.projects.append(project)
    """
    Withdrawal of the project
    
    Returns:
        Returns a value if remove to our user
    """

    def unassigned(self, project):
        self.projects.remove(project)

class Assignment:
    """
    Creating a task class

    Args:
         received_tasks: dict, is_done: bool, description: str, status: str

    Returns:
         This function returns the value of the request that it previously submits and checks if there is a request
    """
    def __init__(self, received_tasks: dict, is_done: bool, description: str, status: str) -> None:
        self.received_tasks = received_tasks
        self.is_done = is_done
        self.status = status
    """
    Testing
        
    """
    def get_tasks_to_date(self, date: datetime):
        return [v for k, v in self.received_tasks.items() if k <= date]


class Project:
    """
    Creating a project class

    Args:
        title: str, start_date: datetime, task_list: list[dict], developers: list[Developer], limit: int):


    Returns:
       This function simply returns a value
    """

    def __init__(self,title: str, start_date: datetime, task_list: list[dict], developers: list[Developer], limit: int):
        self.title = title
        self.task_list = task_list
        self.developers = []
        self.limit = limit
        self.start_date = start_date

    """
    Adding a developer
    
     Args:
       developer: Developer


    Returns:
       This function simply returns a value
    """
    def add_developer(self, developer: Developer) -> None:
        if self.limit > len(self.developers):
            self.developers.append(developer)

            developer.assigned(project=self)
    """
    Remove the developer
    
    Args:
        developer: Developer


     Returns:
         This function simply returns a value
    """
    def remove_developer(self, developer: Developer) -> None:
        for deldev in self.developers:
            if deldev.id == developer.id:
                self.developers.remove(self.developers.index(deldev))
                print(f"Developer {deldev.name} deleted")

                return
        print(f"Developer {deldev.name} does not exist in this project")
        return

class QAEngineer:
    """
    Create a class

    Args:
        id: int, name: str, address: str, phone_number: str, email: str, salary: float, rank: str, position: str

    Returns:
       This function simply returns a value

    """
    def __init__(self, id: int, name: str, address: str, phone_number: str, email: str, salary: float, rank: str, position: str):
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.rank = rank
        self.position = position

    def test_feature(self, test_features, *args) -> None:
        print("Developer id ", {self.id})
        return


class ProjectManajer:
    """
    Create class ProjectManajer

    Args:
       id: int, name: str, address: str, phone_number: str, email: str, salary: float, project: Project

    Returns:
       Returns some value
    """
    def init(self, id: int, name: str,  address: str, phone_number: str, email: str, salary: float, project: Project) ->None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project
    """
    Accepting parameters
    
    Args:
        developer: Developer
    
    Returns:
        simply returns the value
        
    """
    def discuss_progress(self, developer: Developer):
        print(f"The project's {self.project.title} progress has been discussed with {developer.name}")

