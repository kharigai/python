from enum import IntEnum, auto

class Master(IntEnum):
    CORP = 1
    GROUP = 2
    EMPLOYEE = 3


class CashTimer:
    def __init__(self, category_id, expire_sec):
        self.__category_id = category_id
        self.__expire_sec = expire_sec

    @property
    def category_id(self):
        pass
    @category_id.getter
    def category_id(self):
        return self.__category_id

    @property
    def expire_sec(self):
        pass
    @expire_sec.getter
    def expire_sec(self):
        return self.__expire_sec

CASH_TIMERS = {
    Master.CORP.name: CashTimer(Master.CORP, 20), 
    Master.GROUP.name: CashTimer(Master.GROUP, 30), 
    Master.EMPLOYEE.name: CashTimer(Master.EMPLOYEE, 40), 
}

if __name__ == '__main__':
    for k, v in CASH_TIMERS.items():
        print(f'key: {k}, category_id: {v.category_id}, expire_sec: {v.expire_sec}')
