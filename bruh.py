from dataclasses import dataclass
from typing import Literal, Union, Any
from icecream import ic


VeryComplexType = Union[str,int,float]

complex_csv_file = "Wow very complex"



@dataclass
class VeryComplexData:
    complex_var: VeryComplexType


# class VeryComplexFactory:
#     def do_complex_stuff():
#         pass
    
#     def create(very_complex_data: Any) -> VeryComplexData:
#         return VeryComplexData(do_complex_stuff(very_complex_data))