from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base


# create Base Object
Base = declarative_base()
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
Base.to_dict = to_dict

class FutureContract(Base):
    __tablename__ = 'contract'

    交易品种 = Column(Text, primary_key=True)
    交易单位 = Column(Text)
    报价单位 = Column(Text)
    最小变动价位 = Column(Text)
    每日价格波动限制 = Column(Text)
    合约月份 = Column(Text)
    交易时间 = Column(Text)
    最后交易日 = Column(Text)
    最后交割日 = Column(Text)
    交割等级 = Column(Text)
    交割地点 = Column(Text)
    最低交易保证金 = Column(Text)
    交割方式 = Column(Text)
    交易代码 = Column(Text)
    上市交易所 = Column(Text)
    交割单位 = Column(Text)
    交易手续费 = Column(Text)
    合约乘数 = Column(Text)
    可交割国债 = Column(Text)
    报价方式 = Column(Text)
