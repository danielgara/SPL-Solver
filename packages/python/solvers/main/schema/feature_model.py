import pydantic
import typing
import enum


class Constraint(str, enum.Enum):
    ROOT = "root"
    OPTIONAL = "optional"
    MANDATORY = "mandatory"
    REQUIRES = "requires"
    EXCLUDES = "excludes"
    AND = "and"
    OR = "or"
    XOR = "xor"
    GROUP_CARDINALITY = "group_cardinality"


class ConstraintSchema(pydantic.BaseModel):
    contraint_type: Constraint
    destination: typing.optional[typing.Union[int, typing.List[int]]]
    low_threshold: typing.optional[int]
    high_threshold: typing.optional[int]


class FeatureSchema(pydantic.BaseModel):
    id: int
    name: str
    contraints: typing.List[ConstraintSchema]


class FeatureModelSchema(pydantic.BaseModel):
    name: str
    author: str
    description: str
    features: typing.List[FeatureSchema]
