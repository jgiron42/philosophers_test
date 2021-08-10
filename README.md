# philosophers test 2021

this repo is a fork of [philosophers_test](https://github.com/cacharle/philosophers_test.git) made by [cacharle](https://github.com/cacharle) adapted to the new subject (2021)

Test for the philosophers project of school 42.

![screenshot](screenshot.png)

## Usage

Clone this repository next to your project directory.
(or change the default path in the [config](src/config.py))

```
.
|- philosophers/
|- philosophers_test/
```

```
$ ./run --help
usage: run [-h] -p {"philo","philo_bonus","all"} [-b] [-g] [-t TIMEOUT]

Philosophers test

optional arguments:
  -h, --help            show this help message and exit
  -p PROGRAM, --philo
                        The philosopher program to test
                         - philo
                         - philo_bonus
                         - all
  -b, --build           Build and exit
  -g, --pager           Open result.log in a pager after the test
  -t TIMEOUT, --timeout TIMEOUT
                        Change the philosopher process time (in seconds)

Tested:
 - Take 2 forks before eating
 - State switch in the correct order
   think -> fork -> fork -> eat n times -> sleep
 - Almost 0 delay between second fork taken and eat
 - Die if the death timeout is expired
 - No output after death
 - Timestamp in order
 - Only take existing fork
 - Error message and status != 0 on argument error
   (not asked by subject but easy to do and cleanner)
```
