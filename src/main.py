#!/usr/bin/env python3

# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    run                                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/27 11:36:34 by charles           #+#    #+#              #
#    Updated: 2020/09/27 11:36:34 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

# [x] invalid state switch
# [x] none existant fork
# [x] timestamp not in order
# [ ] crash
# [ ] should be infinity
# [x] argument error
# [x] print lines after died
# [x] bad output format
# [x] should be dead

import sys
import subprocess

import config
from test import Test
from args import parse_args
from suite import suite
from helper import blue
from helper import red


def main():
    args = parse_args()

    if config.BUILD_BEFORE or args.build:
        try:
            print(blue("=====================================BUILD======================================"))
            subprocess.run(
                config.BUILD_CMD.format(path=config.PHILO_PATHS[0]).split(' '),
                check=True
            )
            print(blue("================================================================================"))
        except subprocess.CalledProcessError:
            print(red("Error with makefile"))
        if args.build:
            sys.exit(0)

    config.TIMEOUT = args.timeout

    suite()

    try:
        if args.philo == "all":
            for philo in range(2):
                Test.run_all(config.PHILO_EXEC_PATHS[philo])
        elif args.philo == "philo_bonus":
            Test.run_all(config.PHILO_EXEC_PATHS[1])
        else:
            Test.run_all(config.PHILO_EXEC_PATHS[0])

    except KeyboardInterrupt:
        pass
    finally:
        Test.write_failed()
    if args.pager:
        subprocess.run([*config.PAGER_CMD, config.RESULT_FILE])
    else:
        print()
        Test.print_summary()
        print("Read {} for more information".format(config.RESULT_FILE))


if __name__ == "__main__":
    main()
