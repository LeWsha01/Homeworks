from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Student:
    name: str = field(repr=True, compare=False)
    average_mark: float
    age: int = field(default=18, repr=False, compare=False)
    subjects: List[str] = field(default_factory=list, compare=False, repr=False)

    def __post_init__(self):
        self.first_letter = self.name[0]


student2 = Student('john', 4, 22)
student1 = Student('ann', 9, 19, ['pe', 'program'])
student3 = Student('Jack', 10, 19)
print(sorted((student3, student2, student1), reverse=True))
