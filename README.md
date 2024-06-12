# ToDo

# Research
- What is a Release ? Is it in form | Release/0.0.0 <- main | Can we use this in the pipline to push docker containers as cr/repo:0.0.0

# Rules
| Only push to main, test, development via pull request
| Require for each branch successful django tests and docker container build

- Run django tests upon pull request | dev <- issue * |
- Run docker build upon pull request | dev <- issue * |

- Run django tests upon pull request | test <- dev |
- Run docker build upon pull request | test <- dev |

- Run django tests upon pull request | main <- test |
- Run docker build upon pull request | main <- test |
- Run production/deployment pipeline upon push on main (tag=beta)

