
class Connection_count(object):
    def __init__(self):
        self._conn = 0;
        self._guest = 0;
        self._tot = 0;

    def add_conn(self, flag):
        if flag == 1:
            self._conn = self._conn + 1
        elif flag == 2:
            self._guest = self._guest + 1
        self._tot = self._tot + 1

    def sub_conn(self):
        self._tot = self._tot - 1

    def get_conn(self):
        return self._conn

    def get_guest(self):
        return self._guest

    def get_tot(self):
        return self._tot

