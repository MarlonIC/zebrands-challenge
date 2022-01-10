from enum import Enum


class State(Enum):
    ACTIVE = 1
    DEACTIVATE = 0


class Rol(Enum):
    Admin = 1
    Anonymous = 0
