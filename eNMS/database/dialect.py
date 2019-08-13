from os import environ
from sqlalchemy import PickleType, String, Text
from sqlalchemy.dialects.mysql.base import MSMediumBlob


DIALECT = DATABASE_URL.split(":")[0]


class CustomPickleType(PickleType):
    if DIALECT == "mysql":
        impl = MSMediumBlob


Dict = MutableDict.as_mutable(CustomPickleType)
List = MutableList.as_mutable(CustomPickleType)
LargeString = Text(int(environ.get("LARGE_STRING_LENGTH", 2 ** 15)))
SmallString = String(int(environ.get("SMALL_STRING_LENGTH", 255)))

