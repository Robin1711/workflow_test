
# Rules
- Run django tests upon pull request | main <- test |
- Run docker build upon pull request | main <- test |

- Run django tests upon pull request | test <- dev |
- Run docker build upon pull request | test <- dev |

- Run production/deployment pipeline upon push on main (tag=beta)

# Research
- What is a Release ? Is it in form | Release/0.0.0 <- main | Can we use this in the pipline to push docker containers as cr/repo:0.0.0