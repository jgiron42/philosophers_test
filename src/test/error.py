# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    error.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/29 09:09:31 by cacharle          #+#    #+#              #
#    Updated: 2020/09/29 10:08:24 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

class Philo(Exception):
    pass


class ShouldFail(Philo):
    def __init__(self, msg: str):
        self._msg = msg
        Philo.__init__(self)

    @property
    def full_summary(self):
        return self.summary

    @property
    def summary(self):
        return "Should fail: {}".format(self._msg)


class Format(Philo):
    def __init__(self, line: str, msg: str):
        self._line = line
        self._msg  = msg
        Philo.__init__(self)

    @property
    def full_summary(self):
        return """FORMAT ERROR: {}
{}
""".format(self._msg, self._line)

    @property
    def summary(self):
        return "format: {}".format(self._msg)


class Log(Philo):
    def __init__(self, logs: [str], msg: str):
        self._logs = logs
        self._msg  = msg
        Philo.__init__(self)

    @property
    def full_summary(self):
        return """LOG ERROR: {}
{}
""".format(self._msg, '\n'.join([str(l) for l in self._logs]))

    @property
    def summary(self):
        return "log: {}".format(self._msg)
