
import asyncio
from pydbantic import Database

from typing import List, Optional, Union
from pydbantic import DataBaseModel, PrimaryKey

class Department(DataBaseModel):
    department_id: str = PrimaryKey()
    name: str
    company: str
    is_sensitive: bool = False
    positions: List[Optional['Positions']] = []  # One to Many

class Positions(DataBaseModel):
    position_id: str = PrimaryKey()
    name: str
    department: Department = None               # One to One mapping
    employees: List[Optional['Employee']] = []  # One to Many

class EmployeeInfo(DataBaseModel):
    ssn: str = PrimaryKey()
    first_name: str
    last_name: str
    address: str
    address2: Optional[str]
    city: Optional[str]
    zip: Optional[int]
    new: Optional[str]
    employee: Optional[Union['Employee', dict]] = None # One to One

class Employee(DataBaseModel):
    employee_id: str = PrimaryKey()
    employee_info: Optional[EmployeeInfo] = None  # One to One
    position: List[Optional[Positions]] = []      # One to Many
    salary: float
    is_employed: bool
    date_employed: Optional[str]

async def main():
    db = await Database.create(
        'sqlite:///test.db',
        tables=[
            Employee,
            EmployeeInfo,
            Positions,
            Department
        ]
    )

if __name__ == '__main__':
    asyncio.run(main())